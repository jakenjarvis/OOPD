#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
複数のソースファイルを結合し、単一のファイルにまとめるスクリプト。
各ソースファイルの内容は、言語情報と相対パスを含むMarkdownコードブロックで囲まれる。
"""

import os
import sys
import pathlib
import shutil
import re
from typing import Dict, List, Tuple, TextIO

# スクリプト実行のベースとなるディレクトリ (通常はリポジトリのルート)
# 環境変数 GITHUB_WORKSPACE があればそれを使用、なければカレントディレクトリを解決
try:
    WORKSPACE_PATH: pathlib.Path = pathlib.Path(os.environ.get("GITHUB_WORKSPACE", ".")).resolve(strict=True)
except FileNotFoundError:
    print(f"Error: Workspace path '{os.environ.get('GITHUB_WORKSPACE', '.')}' not found.", file=sys.stderr)
    sys.exit(1)

# ファイル拡張子 (小文字) と Markdown コードブロック言語識別子のマッピング
LANGUAGE_MAP: Dict[str, str] = {
    ".md": "Markdown",
    ".txt": "Text",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".py": "python",
    ".sh": "bash",
}

# ファイルコピー設定: タプルのリスト
COPY_CONFIG: List[Tuple[str, str]] = [
    (
        "docs/ja/translation_rules/ja_rules.md",
        "sources/translation_rules/ja_rules.md",
    ),
    (
        "docs/ja/initial_instructions/language_specification_ja.md",
        "sources/initial_instructions/language_specification_ja.md",
    ),
]

# 結合設定: タプルのリスト
MERGE_CONFIG: List[Tuple[str, bool, ...]] = [
    (
        # for development
        (".github/workflows/version-markdown-merge.yml", True),
        ("scripts/increment_version.sh", True),
        ("scripts/set_tag.sh", True),
        ("scripts/merge_md.py", True),

        "output/github_workflows_all.md"
    ),
    (
        # for development
        ("README.md", True),
        ("docs/ja/core.md", True),
        ("docs/ja/extended_types.md", True),
        ("docs/ja/english_specification.md", True),
        ("docs/ja/formats/format_common.md", True),
        ("docs/ja/formats/format_definition.md", True),
        ("docs/ja/formats/format_user.md", True),
        ("docs/ja/localization_overview.md", True),
        ("docs/ja/translation_rules/README.md", True),
        ("docs/ja/translation_rules/ja_rules.md", True),
        ("docs/ja/initial_instructions/initial_instructions.md", True),
        ("docs/ja/initial_instructions/language_specification_ja.md", False),

        "output/docs/ja/system_instructions_consolidated.md"
    ),
    (
        # for common consolidated
        ("README.md", True),
        ("sources/core.md", True),
        ("sources/extended_types.md", True),
        ("sources/english_specification.md", True),
        ("sources/formats/format_common.md", True),
        ("sources/formats/format_definition.md", True),
        ("sources/formats/format_user.md", True),
        ("sources/localization_overview.md", True),
        ("sources/translation_rules/README.md", True),
        ("sources/translation_rules/ja_rules.md", True),
        ("sources/initial_instructions/initial_instructions.md", True),

        "instructions/system_instructions_consolidated.md"
    ),
    (
        # for en
        ("instructions/system_instructions_consolidated.md", False),
        ("sources/initial_instructions/language_specification_en.md", False),

        "instructions/system_instructions_en.md"
    ),
    (
        # for ja
        ("instructions/system_instructions_consolidated.md", False),
        ("sources/initial_instructions/language_specification_ja.md", False),

        "instructions/system_instructions_ja.md"
    )
]

def copy_file_relative(source_path: str, destination_path: str) -> None:
    """相対パスでファイルをコピーする"""
    try:
        source_full_path = os.path.abspath(source_path)
        destination_full_path = os.path.abspath(destination_path)

        shutil.copy2(source_full_path, destination_full_path)
        print(f"File '{source_path}' copied to '{destination_path}'.")

    except FileNotFoundError:
        print(f"Error: File '{source_path}' not found.")
    except Exception as e:
        print(f"Error: An error occurred during file copy: {e}")

def get_language_name(file_path: pathlib.Path) -> str:
    """ファイルパスの拡張子に基づいて言語識別子を決定する。"""
    extension: str = file_path.suffix.lower()
    # マッピングに存在すればその値を、なければ "Text" を返す
    return LANGUAGE_MAP.get(extension, "Text")

def replace_version_in_file(file_path: pathlib.Path, new_version: str) -> None:
    """ファイル内のバージョン番号を置換する"""
    try:
        content = file_path.read_text(encoding="utf-8")
        updated_content = re.sub(r"v[0-9]+\.[0-9]+\.[0-9]+", new_version, content)
        file_path.write_text(updated_content, encoding="utf-8")
        print(f"Updated version in {file_path.name} to {new_version}")
    except FileNotFoundError:
        print(f"Warning: File {file_path.name} not found.")
    except Exception as e:
        print(f"Error: An error occurred during version replacement in {file_path.name}: {e}")

def write_file_content(
    outfile: TextIO,                # 書き込み先のファイルオブジェクト
    infile_path: pathlib.Path,      # 読み込む入力ファイルのパス
    workspace_path: pathlib.Path,   # 基準となるワークスペースパス
    use_codeblock: bool = True      # コードブロックを使用するかどうか
) -> bool:
    """
    入力ファイルを読み込み、その内容を出力ファイルオブジェクトに書き込む。
    コードブロックを使用するかどうかを選択できる。
    成功した場合は True、失敗した場合は False を返す。
    """
    try:
        # workspaceからの相対パスを取得し、区切り文字を '/' に統一
        relative_path: str = infile_path.relative_to(workspace_path).as_posix()
        language_name: str = get_language_name(infile_path)
        print(f"  Adding {relative_path}...")

        content: str = infile_path.read_text(encoding="utf-8")

        if use_codeblock:
            # 開始コードブロック行 (メタデータ付き)
            outfile.write(f"```{language_name}: {relative_path}\n\n")
            outfile.write(content)
            outfile.write("\n```\n")
        else:
            outfile.write(content)
        return True

    except FileNotFoundError:
        print(f"Error: Input file not found during read - {infile_path}", file=sys.stderr)
        return False
    except IOError as e:
        print(f"Error: Could not read file {infile_path} - {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred processing {infile_path} - {e}", file=sys.stderr)
        return False

def merge_files(
    input_configs: List[Tuple[str, bool]], # 入力ファイル名とコードブロック化フラグのリスト
    output_filename: str,          # 出力ファイル名
    workspace_path: pathlib.Path      # 基準となるワークスペースパス
) -> bool:
    """
    複数の入力ファイルの内容を単一の出力ファイルに結合する。
    成功した場合は True、失敗した場合は False を返す。
    """
    # pathlib.Path オブジェクトに変換
    output_path: pathlib.Path = workspace_path / output_filename
    input_paths: List[pathlib.Path] = [workspace_path / fname for fname, _ in input_configs]

    # 処理対象を表示
    relative_output_path = output_path.relative_to(workspace_path)
    print(f"\nMerging into {relative_output_path}...")

    # --- 事前チェック: 入力ファイルの存在確認 ---
    missing_files: List[pathlib.Path] = [p for p in input_paths if not p.is_file()]
    if missing_files:
        for mf in missing_files:
            print(f"Error: Input file not found or is not a file - {mf.relative_to(workspace_path)}", file=sys.stderr)
        return False

    try:
        # 出力ファイルの親ディレクトリが存在しない場合は作成
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # --- ファイルの書き込み ---
        with output_path.open("w", encoding="utf-8") as outfile:
            all_written_successfully = True
            for i, (infile_path, use_codeblock) in enumerate(zip(input_paths, [use_codeblock for _, use_codeblock in input_configs])):
                # ファイル内容をコードブロックで書き込む
                if not write_file_content(outfile, infile_path, workspace_path, use_codeblock):
                    all_written_successfully = False
                    break

                # 最後のファイルでなければ、ブロック間に改行を追加
                if i < len(input_paths) - 1:
                    outfile.write("\n")

            # 書き込み中にエラーが発生した場合
            if not all_written_successfully:
                print(f"Error: Failed to write one or more blocks to {relative_output_path}.", file=sys.stderr)
                return False

        print(f"Successfully merged files into {relative_output_path}")
        return True

    except IOError as e:
        print(f"Error: Could not open or write output file {relative_output_path} - {e}", file=sys.stderr)
        return False

    except Exception as e:
        print(f"Error: An unexpected error occurred during merging to {relative_output_path} - {e}", file=sys.stderr)
        return False

def main():
    """スクリプトのエントリーポイント。結合設定に基づいてマージ処理を実行する。"""
    print("Starting file merge process...")
    overall_success = True

    # version.txtから新しいバージョン番号を読み取る
    try:
        with open("version.txt", "r") as f:
            new_version = f.read().strip()
    except FileNotFoundError:
        print("Error: version.txt not found.", file=sys.stderr)
        sys.exit(1)

    # for development
    # ファイルコピーを実行
    for source_filename, destination_filename in COPY_CONFIG:
        copy_file_relative(source_filename, destination_filename)

    # 各結合設定に対して merge_files を実行
    for config in MERGE_CONFIG:
        if len(config) < 2:
            print(f"Warning: Skipping invalid merge config (must have at least one input and one output): {config}", file=sys.stderr)
            continue

        output_filename = config[-1]
        input_configs = [(fname, use_codeblock) for fname, use_codeblock in config[:-1]]

        # ファイル内のバージョン番号を置換
        for fname, _ in input_configs:
            file_path = WORKSPACE_PATH / fname
            if file_path.suffix.lower() == ".md":
                replace_version_in_file(file_path, new_version)

        if not merge_files(input_configs, output_filename, WORKSPACE_PATH):
            overall_success = False
            break

    # 最終結果に基づいて終了コードを設定
    if overall_success:
        print("\nAll merge operations completed successfully.")
        sys.exit(0)
    else:
        print("\nOne or more merge operations failed.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
