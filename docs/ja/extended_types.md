## OOPD 拡張型定義 (Extended Types Definition)

### 拡張型とは

このドキュメントは、Object-Oriented Prompt Design (OOPD) における**拡張型 (Extended Types)** を定義します。拡張型は、OOPDのコアとなる**標準型 (Standard Types)**（**`basic_terms.md`** で定義）を補完し、特定のドメインや利用シーンにおいてプロンプトの意図をより明確にし、AIとのコミュニケーションを円滑にすることを目的とした、意味的・具体的な型です。

標準型の定義については `basic_terms.md` を参照してください。

拡張型の使用は**オプション**ですが、これらを利用することで、より表現豊かで構造化されたプロンプト設計が可能になります。

**【重要】** 拡張型も標準型と同様に、**基本用語**として扱われます。つまり、プロンプトの記述言語に関わらず、**必ずここで定義された英語表記 (`ContentString`, `Persona` など) で記述**し、**翻訳されません**。

### 拡張型リスト (一覧)

AIがこれらの拡張型名を **基本用語（常に英語表記で使用される固定キーワード）**として認識するために、以下のリストを定義します。

```json
{
  "ExtendedTypes": ["ContentString", "Instruction", "Persona", "OutputStyle", "CodeBlock", "Ref", "SchemaDefinition", "JsonString", "YamlString", "XmlString", "Color"]
}
```

### 各拡張型の詳細

以下に、定義された各拡張型とその詳細を示します。

AI向け注記: 拡張型の『実体/表現』における複数形式の記述は、AIの内部解釈の柔軟性を示します。AIは、ユーザーが自然言語で記述しても、構造化データを示唆する形で記述しても、その拡張型の意味に沿って内容を理解し、処理に反映させること。

#### `ContentString`

- **意味 (Meaning):**
  AIが処理・生成する中心的なテキストブロック、例えば記事本文、レポート内容、メール本文、物語の本文など、主要な長文テキストコンテンツそのものを表します。他のメタデータ（指示やペルソナなど）と区別して、内容としてのテキストを指定するために使用します。
- **用途 (Use Cases):**
  - 記事や文書の要約・翻訳対象の指定。
  - レポートやメールの本文部分の指定。
  - 物語や詩など、創作物の本体部分の指定。
  - コード (`CodeBlock`) や指示 (`Instruction`) と区別して、純粋な内容テキストを示したい場合。
- **実体/表現 (Underlying Representation/Format):**
  - `String`。
  - Markdown形式など、構造化されたテキストを含むこともあります。
- **関連する基本用語 (Related Basic Terms):**
  - `String` (from `basic_terms.md`)

#### `Instruction`

- **意味 (Meaning):**
  AIに対して実行してほしい具体的な指示、命令、またはタスク内容を自然言語で記述したものを表します。プロンプト内の他の情報（データやコンテキスト）と区別し、AIへのアクション要求を明確に示すための型です。単なる説明ではなく、具体的な行動を促す内容を記述します。
- **用途 (Use Cases):**
  - 複雑なプロンプト内で、AIへの指示部分を構造的に示したい場合。
  - 複数の指示ステップを定義し、順次実行させたい場合。
  - プロンプト自体をデータとして扱い、分析・生成するようなメタプロンプティング。
- **実体/表現 (Underlying Representation/Format):**
  - `String`。自然言語による指示文。
- **関連する基本用語 (Related Basic Terms):**
  - `String` (from `basic_terms.md`)

#### `Persona`

- **意味 (Meaning):**
  AIに演じさせたい特定の役割、キャラクター像、専門家の立場などのペルソナ設定を表します。これには、AIの応答スタイル（例: 'フォーマル', 'フレンドリー'）、口調（例: '丁寧語', '断定調'）、想定される知識レベル（例: '初心者向け', '専門家レベル'）、思考様式（例: '論理的', '創造的'）、あるいは特定の背景（例: '18世紀の哲学者'）などが含まれます。これらの要素を説明的に記述することで、AIの振る舞いを規定します。
- **用途 (Use Cases):**
  - 特定の役割（例: 「熟練の編集者」「フレンドリーなアシスタント」「特定の歴史上の人物」）になりきって応答させる。
  - 応答のトーンや専門性を制御する。
  - キャラクター対話やロールプレイングシナリオの定義。
- **実体/表現 (Underlying Representation/Format):**
  - `String`（ペルソナを説明するテキスト）または `Dictionary`（名前、性格、口調などの属性を構造化）。
- **関連する基本用語 (Related Basic Terms):**
  - `String`, `Dictionary` (from `basic_terms.md`)

#### `OutputStyle`

- **意味 (Meaning):**
  AIが生成する最終的な出力の形式、体裁、文体、トーンなどを指定するための複合的な情報を表します。例えば、「Markdown形式で箇条書きにしてほしい」「JSON形式で出力してほしい」「丁寧語を使い、共感的なトーンで」「全体で約500文字に要約してほしい」といった、応答の整形やスタイルに関する要求を記述します。
- **用途 (Use Cases):**
  - 出力形式の指定（例: Markdown, JSON, 箇条書き）。
  - 文体の指定（例: フォーマル, カジュアル, 学術的）。
  - トーンの指定（例: 丁寧, 共感的, 断定的）。
  - 文字数制限や要約レベルなどの指定。
- **実体/表現 (Underlying Representation/Format):**
  - `Dictionary`（`format: String`, `tone: String`, `length: Number` のような属性を持つ）。
  - または、単純な `String`（例: "JSON形式で、丁寧な口調で"）。
- **関連する基本用語 (Related Basic Terms):**
  - `Dictionary`, `String`, `Number` (from `basic_terms.md`)

#### `CodeBlock`

- **意味 (Meaning):**
  特定のプログラミング言語で書かれたコードの断片そのものを表します。AIにコードの生成、説明、レビュー、デバッグなどを依頼する際に、対象となるコードを指定したり、参考としてコード例を示したりするために使用します。言語の種類（例: 'Python', 'JavaScript'）を併記することが推奨されますが、必須ではありません。
- **用途 (Use Cases):**
  - コードの生成、説明、レビュー、デバッグ、翻訳などの指示対象を指定する。
  - プロンプト内にサンプルコードや参照コードを埋め込む。
  - テキスト部分とコード部分を明確に区別する。
- **実体/表現 (Underlying Representation/Format):**
  - `String`（コードそのもの）。
  - 言語を指定する属性（例: `language: String`）を持つ `Dictionary` としても表現可能。
- **関連する基本用語 (Related Basic Terms):**
  - `String`, `Dictionary` (from `basic_terms.md`)

#### `Ref`

- **意味 (Meaning):**
  外部リソースや他のデータへの参照情報や位置を示す識別子を表します。具体的には、WebページのURL、ファイルシステム上のパス、APIエンドポイント、データベースのレコードID、あるいは画像や動画ファイルへのリンクなどが該当します。AIがこれらのリソースにアクセスしたり、それらについて言及したりする際の参照先として使用します。
- **用途 (Use Cases):**
  - WebページのURLを指定する。
  - ローカルまたはリモートのファイルパスを指定する。
  - APIのエンドポイントを指定する。
  - 画像、音声、動画ファイルへのリンクや識別子を指定する。
  - データベースのレコードIDなど、他のデータへの参照を示す。
- **実体/表現 (Underlying Representation/Format):**
  - `String`。URL, ファイルパス, URN, データURIなど様々な形式の文字列。
- **関連する基本用語 (Related Basic Terms):**
  - `String`, `UniqueID` (from `basic_terms.md`)

#### `SchemaDefinition`

- **意味 (Meaning):**
  データの構造定義、スキーマ、あるいはデータモデルそのものをテキスト形式で記述したものを表します。例えば、JSON Schema定義、データベースのテーブル定義（CREATE TABLE文など）、あるいはクラスの構造定義などが該当します。AIに特定の構造に基づいたデータを生成させたり、データ構造自体を分析・説明させたりする際に使用します。
- **用途 (Use Cases):**
  - 特定のスキーマに基づいたデータ生成を指示する。
  - データ構造の定義や説明をAIに依頼する。
  - データのバリデーションルールを指定する。
- **実体/表現 (Underlying Representation/Format):**
  - `String`（スキーマ定義をテキストで記述したもの）。
  - `JsonString` や `YamlString` で表現されることも多い。
- **関連する基本用語 (Related Basic Terms):**
  - `String` (from `basic_terms.md`), `JsonString`, `YamlString` (defined in this file)

#### `JsonString`

- **意味 (Meaning):**
  JSON (JavaScript Object Notation) 形式に準拠した文字列を表します。JSONとして有効なデータ構造（オブジェクト {} または配列 [] で始まる）を文字列値として持つことを示します。APIの応答データや設定情報など、構造化データをJSON形式で直接扱いたい場合に使用します。
- **用途 (Use Cases):**
  - JSONデータの解析、生成、変換を指示する。
  - 構造化されたデータをJSON形式で入出力することを明示する。
  - APIリクエスト/レスポンスのボディ部分など。
- **実体/表現 (Underlying Representation/Format):**
  - `String` (JSON形式に準拠した文字列)。
- **関連する基本用語 (Related Basic Terms):**
  - `String` (from `basic_terms.md`)

#### `YamlString`

- **意味 (Meaning):**
  YAML (YAML Ain't Markup Language) 形式に準拠した文字列を表します。YAMLとして有効なデータ構造を文字列値として持つことを示します。設定ファイルの内容や、人間が読みやすい構造化データなどをYAML形式で直接扱いたい場合に使用します。
- **用途 (Use Cases):**
  - YAMLデータの解析、生成、変換を指示する。
  - 設定ファイルや構造化データをYAML形式で扱うことを明示する。
  - OOPDのインスタンスデータ表現など。
- **実体/表現 (Underlying Representation/Format):**
  - `String` (YAML形式に準拠した文字列)。
- **関連する基本用語 (Related Basic Terms):**
  - `String` (from `basic_terms.md`)

#### `XmlString`

- **意味 (Meaning):**
  XML (Extensible Markup Language) 形式、またはHTML (HyperText Markup Language) 形式に準拠した文字列を表します。XML/HTMLとして有効なマークアップ構造を文字列値として持つことを示します。XMLデータの断片、設定ファイル、あるいはHTMLコンテンツなどを直接扱いたい場合に使用します。
- **用途 (Use Cases):**
  - XML/HTMLデータの解析、生成、変換を指示する。
  - 設定ファイル、データ交換（SOAPなど）、マークアップ文書を扱うことを明示する。
- **実体/表現 (Underlying Representation/Format):**
  - `String` (XML/HTML形式に準拠した文字列)。
- **関連する基本用語 (Related Basic Terms):**
  - `String` (from `basic_terms.md`)

#### `Color`

- **意味 (Meaning):**
  色を表す値を文字列で指定します。CSSなどで一般的に認識される形式（例: 色名 'red', HEX値 '#FF0000', RGB値 'rgb(255, 0, 0)', HSL値 'hsl(0, 100%, 50%)' など）での記述を想定しています。UIの色指定や、画像生成時の色指示などに使用します。
- **用途 (Use Cases):**
  - UIデザイン、データ可視化、画像生成指示。
  - シミュレーション環境の色設定（空の色、物の色など）。
  - テキストの装飾（文字色、背景色）の指示。
- **実体/表現 (Underlying Representation/Format):**
  - `String` (推奨)。HEX (`#RRGGBB`, `#RGB`), RGB (`rgb(r,g,b)`), HSL (`hsl(h,s,l)`), 色名 (`red`, `blue`) など、CSS等で一般的に使われる形式を想定。
- **関連する基本用語 (Related Basic Terms):**
  - `String` (from `basic_terms.md`)
