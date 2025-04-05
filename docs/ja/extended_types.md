## OOPD 拡張型定義 (Extended Types Definition)

### 拡張型とは

このドキュメントは、Object-Oriented Prompt Design (OOPD) における**拡張型 (Extended Types)** を定義します。拡張型は、OOPDのコアとなる**標準型 (Standard Types)** を補完し、特定のドメインや利用シーンにおいてプロンプトの意図をより明確にし、AIとのコミュニケーションを円滑にすることを目的とした、意味的・具体的な型です。

標準型（`String`, `Number`, `Boolean` など）の定義については `core.md` を参照してください。

拡張型の使用は**オプション**ですが、これらを利用することで、より表現豊かで構造化されたプロンプト設計が可能になります。拡張型も標準型と同様に、**プロンプトの記述言語に関わらず、定義された英語表記で記述**します。

### 拡張型リスト (一覧)

AIがこれらの拡張型名を固定キーワードとして認識するために、以下のリストを定義します。

~~~json
{
  "ExtendedTypes": ["ContentString", "Instruction", "Persona", "OutputStyle", "CodeBlock", "Ref", "SchemaDefinition", "JsonString", "YamlString", "XmlString", "Color"]
}
~~~

### 拡張型の実体/表現について

いくつかの拡張型では、後述の「実体/表現」で複数の形式（例: String または Dictionary）が示されています。これは主にAIが内部的に扱う際の柔軟性を示すものです。ユーザーは通常、プロンプト内でその拡張型が意図する内容を自然な形で記述すればよく（例: Persona であればペルソナの説明文、OutputStyle であれば出力形式やトーンに関する指示）、AIが文脈に応じて適切な内部表現を選択・解釈します。ユーザーが明示的に特定の形式（例: Dictionary）で記述することも可能です。

### 各拡張型の詳細

以下に、定義された各拡張型とその詳細を示します。

#### `ContentString`

- **意味 (Meaning):**
  主要な長文テキストコンテンツを表します。記事、レポート、メール本文、物語など、AIが処理・生成する中心的なテキストブロックを示すことを意図しています。
- **用途 (Use Cases):**
  - 記事や文書の要約・翻訳対象の指定。
  - レポートやメールの本文部分の指定。
  - 物語や詩など、創作物の本体部分の指定。
  - コード (`CodeBlock`) や指示 (`Instruction`) と区別して、純粋な内容テキストを示したい場合。
- **実体/表現 (Underlying Representation/Format):**
  - `String`。
  - Markdown形式など、構造化されたテキストを含むこともあります。
- **関連する標準型 (Related Standard Types):**
  - `String`

#### `Instruction`

- **意味 (Meaning):**
  AIに対する具体的な指示、命令、またはタスク記述を表します。プロンプト内の他の部分（データやコンテキスト）と区別して、AIに実行してほしいアクションを明確に示します。
- **用途 (Use Cases):**
  - 複雑なプロンプト内で、AIへの指示部分を構造的に示したい場合。
  - 複数の指示ステップを定義し、順次実行させたい場合。
  - プロンプト自体をデータとして扱い、分析・生成するようなメタプロンプティング。
- **実体/表現 (Underlying Representation/Format):**
  - `String`。自然言語による指示文。
- **関連する標準型 (Related Standard Types):**
  - `String`

#### `Persona`

- **意味 (Meaning):**
  AIに演じさせたい役割、キャラクター、専門家などのペルソナ設定を表します。AIの応答スタイル、口調、知識レベル、思考様式などを規定します。
- **用途 (Use Cases):**
  - 特定の役割（例: 「熟練の編集者」「フレンドリーなアシスタント」「特定の歴史上の人物」）になりきって応答させる。
  - 応答のトーンや専門性を制御する。
  - キャラクター対話やロールプレイングシナリオの定義。
- **実体/表現 (Underlying Representation/Format):**
  - `String`（ペルソナを説明するテキスト）または `Dictionary`（名前、性格、口調などの属性を構造化）。
- **関連する標準型 (Related Standard Types):**
  - `String`, `Dictionary`

#### `OutputStyle`

- **意味 (Meaning):**
  AIが生成する出力の形式、文体、トーンなどを指定するための複合的な型。どのように応答を整形してほしいかを伝えます。
- **用途 (Use Cases):**
  - 出力形式の指定（例: Markdown, JSON, 箇条書き）。
  - 文体の指定（例: フォーマル, カジュアル, 学術的）。
  - トーンの指定（例: 丁寧, 共感的, 断定的）。
  - 文字数制限や要約レベルなどの指定。
- **実体/表現 (Underlying Representation/Format):**
  - `Dictionary`（`format: String`, `tone: String`, `length: Number` のような属性を持つ）。
  - または、単純な `String`（例: "JSON形式で、丁寧な口調で"）。
- **関連する標準型 (Related Standard Types):**
  - `Dictionary`, `String`, `Number`

#### `CodeBlock`

- **意味 (Meaning):**
  特定のプログラミング言語で書かれたコードの断片を表します。言語の種類を属性として持つことが想定されます。
- **用途 (Use Cases):**
  - コードの生成、説明、レビュー、デバッグ、翻訳などの指示対象を指定する。
  - プロンプト内にサンプルコードや参照コードを埋め込む。
  - テキスト部分とコード部分を明確に区別する。
- **実体/表現 (Underlying Representation/Format):**
  - `String`（コードそのもの）。
  - 言語を指定する属性（例: `language: String`）を持つ `Dictionary` としても表現可能。
- **関連する標準型 (Related Standard Types):**
  - `String`, `Dictionary`

#### `Ref`

- **意味 (Meaning):**
  何らかのリソース（Webページ, ファイル, APIエンドポイント, データ, 画像, 音声, 動画など）への参照や位置を示す情報。URI (Uniform Resource Identifier) の概念に近いです。
- **用途 (Use Cases):**
  - WebページのURLを指定する。
  - ローカルまたはリモートのファイルパスを指定する。
  - APIのエンドポイントを指定する。
  - 画像、音声、動画ファイルへのリンクや識別子を指定する。
  - データベースのレコードIDなど、他のデータへの参照を示す。
- **実体/表現 (Underlying Representation/Format):**
  - `String`。URL, ファイルパス, URN, データURIなど様々な形式の文字列。
- **関連する標準型 (Related Standard Types):**
  - `String`, `UniqueID` (参照先がIDの場合)

#### `SchemaDefinition`

- **意味 (Meaning):**
  データの構造定義、スキーマ、データモデルなどを表します。JSON Schema、クラス定義、データベーススキーマなどが該当します。
- **用途 (Use Cases):**
  - 特定のスキーマに基づいたデータ生成を指示する。
  - データ構造の定義や説明をAIに依頼する。
  - データのバリデーションルールを指定する。
- **実体/表現 (Underlying Representation/Format):**
  - `String`（スキーマ定義をテキストで記述したもの）。
  - `JsonString` や `YamlString` で表現されることも多い。
- **関連する標準型 (Related Standard Types):**
  - `String`, `JsonString`, `YamlString`

#### `JsonString`

- **意味 (Meaning):**
  JSON (JavaScript Object Notation) 形式で記述されたデータを表す文字列。
- **用途 (Use Cases):**
  - JSONデータの解析、生成、変換を指示する。
  - 構造化されたデータをJSON形式で入出力することを明示する。
  - APIリクエスト/レスポンスのボディ部分など。
- **実体/表現 (Underlying Representation/Format):**
  - `String` (JSON形式に準拠した文字列)。
- **関連する標準型 (Related Standard Types):**
  - `String`

#### `YamlString`

- **意味 (Meaning):**
  YAML (YAML Ain't Markup Language) 形式で記述されたデータを表す文字列。
- **用途 (Use Cases):**
  - YAMLデータの解析、生成、変換を指示する。
  - 設定ファイルや構造化データをYAML形式で扱うことを明示する。
  - OOPDのインスタンスデータ表現など。
- **実体/表現 (Underlying Representation/Format):**
  - `String` (YAML形式に準拠した文字列)。
- **関連する標準型 (Related Standard Types):**
  - `String`

#### `XmlString`

- **意味 (Meaning):**
  XML (Extensible Markup Language) 形式で記述されたデータを表す文字列。HTMLやXHTMLの表現にも使用できます。
- **用途 (Use Cases):**
  - XML/HTMLデータの解析、生成、変換を指示する。
  - 設定ファイル、データ交換（SOAPなど）、マークアップ文書を扱うことを明示する。
- **実体/表現 (Underlying Representation/Format):**
  - `String` (XML/HTML形式に準拠した文字列)。
- **関連する標準型 (Related Standard Types):**
  - `String`

#### `Color`

- **意味 (Meaning):**
  色を表す値。
- **用途 (Use Cases):**
  - UIデザイン、データ可視化、画像生成指示。
  - シミュレーション環境の色設定（空の色、物の色など）。
  - テキストの装飾（文字色、背景色）の指示。
- **実体/表現 (Underlying Representation/Format):**
  - `String` (推奨)。HEX (`#RRGGBB`, `#RGB`), RGB (`rgb(r,g,b)`), HSL (`hsl(h,s,l)`), 色名 (`red`, `blue`) など、CSS等で一般的に使われる形式を想定。
- **関連する標準型 (Related Standard Types):**
  - `String`
