#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
複数のソースファイルを結合し、単一のファイルにまとめるスクリプト。
各ソースファイルの内容は、言語情報と相対パスを含むMarkdownコードブロックで囲まれる。
"""

import os
import sys
import pathlib
from typing import Dict, List, Tuple, TextIO

# --- 設定 (Configuration) ---

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

# 結合設定: タプルのリスト
MERGE_CONFIG: List[Tuple[str, ...]] = [
    (
        # for development
        ".github/workflows/version-markdown-merge.yml",
        "scripts/increment_version.sh",
        "scripts/set_tag.sh",
        "scripts/replace_md.sh",
        "scripts/merge_md.py",

        "output/github_workflows_all.md"
    ),
    (
        # for development
        "README.md",
        "docs/ja/core.md",
        "docs/ja/extended_types.md",
        "docs/ja/english_specification.md",
        "docs/ja/formats/format_common.md",
        "docs/ja/formats/format_definition.md",
        "docs/ja/formats/format_user.md",
        "docs/ja/localization_overview.md",
        "docs/ja/translation_rules/README.md",
        "docs/ja/translation_rules/ja_rules.md",
        "docs/ja/initial_instructions/ja_initial_instructions.md",

        "output/docs/ja/system_instructions_consolidated.md"
    ),
    # (
    #     "en/core.md",
    #     "en/format.md",
    #     "en/system_instructions_consolidated.md"
    # ),
    # (
    #     "ja/core.md",
    #     "ja/format.md",
    #     "ja/system_instructions_consolidated.md"
    # ),
]

# --- ヘルパー関数 (Helper Functions) ---

def get_language_name(file_path: pathlib.Path) -> str:
    """ファイルパスの拡張子に基づいて言語識別子を決定する。"""
    extension: str = file_path.suffix.lower()
    # マッピングに存在すればその値を、なければ "Text" を返す
    return LANGUAGE_MAP.get(extension, "Text")

def write_file_content_with_block(
    outfile: TextIO,                # 書き込み先のファイルオブジェクト
    infile_path: pathlib.Path,      # 読み込む入力ファイルのパス
    workspace_path: pathlib.Path    # 基準となるワークスペースパス
) -> bool:
    """
    入力ファイルを読み込み、その内容をコードブロック形式で出力ファイルオブジェクトに書き込む。
    成功した場合は True、失敗した場合は False を返す。
    """
    try:
        # workspaceからの相対パスを取得し、区切り文字を '/' に統一
        relative_path: str = infile_path.relative_to(workspace_path).as_posix()
        language_name: str = get_language_name(infile_path)
        print(f"  Adding {relative_path} as {language_name}...")

        # ファイル内容を読み込む
        content: str = infile_path.read_text(encoding="utf-8")

        # 開始コードブロック行 (メタデータ付き)
        outfile.write(f"```{language_name}: {relative_path}\n\n")
        outfile.write(content)
        outfile.write("\n```\n")
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

# --- メイン処理 (Main Logic) ---

def merge_files(
    input_filenames: Tuple[str, ...], # 入力ファイル名のタプル
    output_filename: str,             # 出力ファイル名
    workspace_path: pathlib.Path      # 基準となるワークスペースパス
) -> bool:
    """
    複数の入力ファイルの内容を単一の出力ファイルに結合する。
    成功した場合は True、失敗した場合は False を返す。
    """
    # pathlib.Path オブジェクトに変換
    output_path: pathlib.Path = workspace_path / output_filename
    input_paths: List[pathlib.Path] = [workspace_path / fname for fname in input_filenames]

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
            # 各入力ファイルを処理
            for i, infile_path in enumerate(input_paths):
                # ファイル内容をコードブロックで書き込む
                if not write_file_content_with_block(outfile, infile_path, workspace_path):
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
        # 出力ファイルのオープンや書き込みに関するエラー
        print(f"Error: Could not open or write output file {relative_output_path} - {e}", file=sys.stderr)
        return False

    except Exception as e:
        # その他の予期せぬエラー
        print(f"Error: An unexpected error occurred during merging to {relative_output_path} - {e}", file=sys.stderr)
        return False

def main():
    """スクリプトのエントリーポイント。結合設定に基づいてマージ処理を実行する。"""
    print("Starting file merge process...")
    overall_success = True

    # 各結合設定に対して merge_files を実行
    for config in MERGE_CONFIG:
        if len(config) < 2:
            print(f"Warning: Skipping invalid merge config (must have at least one input and one output): {config}", file=sys.stderr)
            continue

        output_filename = config[-1]     # タプルの最後の要素が出力ファイル
        input_filenames = config[:-1]    # それ以外の要素が入力ファイル

        if not merge_files(input_filenames, output_filename, WORKSPACE_PATH):
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
