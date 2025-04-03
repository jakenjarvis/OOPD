### OOPD 英語仕様 (English Specification)

#### はじめに

このドキュメントは、Object-Oriented Prompt Design (OOPD) において、**英語 (`en`)** でプロンプトを記述し、AIがそれを解釈・応答する際の**仕様とガイドライン**を定義します。英語はOOPDの**ハブ言語**であり、他の言語との翻訳の基準となるため、その仕様は特に重要です。

他の言語に共通する基本原則や記述ルールについては `core.md` および `format_common.md` を参照してください。

#### 基本原則

- **ハブ言語:** 英語 (`en`) はOOPDのハブ言語です。全ての翻訳用語は内部的に英語ハブ名に紐付けられます。
- **単一フォーマット:** 英語でOOPD形式を記述する場合、他の言語のような「ユーザーフォーマット」と「定義フォーマット」の**区別は実質的にありません**。常に定義を明確にするため、**`Definition Format` に準拠した記述**を行います。
  - つまり、モジュール定義 (`##`) が必須です。
  - 定義される要素（クラス、メソッド等）は、後述する**英語命名規則に厳密に従う**必要があります。
- **翻訳処理なし:** 入力プロンプトが英語で、出力も英語が指定されている場合、ハブ言語との間の翻訳処理は発生しません。AIは英語の定義を直接解釈し、英語で応答します。
- **他言語併記なし:** 英語で記述する際、括弧 `()` などを用いて他の言語名を併記する必要は**ありません**。

#### 英語命名規則 (English Naming Conventions)

英語でOOPD形式を記述する際は、以下の命名規則を**厳密に適用**してください。AIもこれらの規則に基づいてプロンプトを解釈し、応答や定義を生成します。

- **モジュール名 (Module Names):**
  - **形式:** ドット (`.`) 区切りの階層構造。全体として**小文字**を推奨。
  - **構成要素:** 各階層の要素名には、**英数字 (a-z, 0-9)** および **ハイフン (`-`)**, **アンダースコア (`_`)** を使用できます。
  - **ピリオド:** 階層区切りとしてのみ使用し、要素名内には含めません。
  - **一意性:** グローバルな一意性を確保するため、逆ドメイン名 (`com.example.project`) や `io.github.username.project` 形式を強く推奨します。
  - **例:** `com.example.task_management`, `io.github.username.my_utils`
- **Section名 (Section Names):**
  - **形式:** 自由記述。特別な命名規則や文字制限はありません。文書構造上の見出しとして分かりやすい英語のテキストを推奨します。
  - **例:** `### Core Functionality`, `### Helper Classes`
- **クラス名 (Class Names):**
  - **形式:** `PascalCase`。単語の先頭を大文字にし、連結します。
  - **例:** `UserProfile`, `TaskItem`, `HttpRequestHandler`
- **インターフェース名 (Interface Names):**
  - **形式:** `PascalCase`。クラス名と同様です。（`I` プレフィックスは付けません）
  - **例:** `UserService`, `Runnable`, `ShapeRenderer`
- **列挙型名 (Enum Names):**
  - **形式:** `PascalCase`。
  - **例:** `OrderStatus`, `ColorMode`, `FileAccessLevel`
- **メソッド名 (Method Names):**
  - **形式:** `camelCase`。最初の単語は小文字、後続の単語の先頭を大文字にし、連結します。
  - **Getter:** `get` プレフィックスを推奨 (例: `getName()`, `getTotalPrice()`)。
  - **Setter:** `set` プレフィックスを推奨 (例: `setName(name: String)`, `setPriority(priority: Priority)`)。
  - **Booleanを返す場合:** `is`, `has`, `can` などのプレフィックスを推奨 (例: `isValid()`, `hasChildren()`, `canExecute()`)。
  - **その他のアクション:** 動作を表す動詞で始めることを推奨 (例: `calculateArea()`, `sendNotification()`, `updateDatabase()`)。
- **プロパティ名 (Property Names):**
  - **形式:** `camelCase`。
  - **Booleanの場合:** `is`, `has`, `can` などのプレフィックスを推奨 (例: `isEnabled`, `hasErrors`, `canModify`)。
  - **その他:** 通常は名詞または名詞句 (例: `firstName`, `orderCount`, `backgroundColor`)。
- **イベント名 (Event Names):**
  - **形式:** `PascalCase`。イベントが発生したことを示す過去形や名詞形が多い。
  - **例:** `ButtonClick`, `StatusChanged`, `DownloadComplete`, `InitializationFailed`
- **列挙型の値 (Enum Members):**
  - **形式:** すべて大文字の `SNAKE_CASE`。単語間をアンダースコア (`_`) で区切ります。
  - **例:** `NOT_STARTED`, `IN_PROGRESS`, `COMPLETED`, `LOW`, `MEDIUM`, `HIGH`, `READ_ONLY`
- **定数名 (Constant Names) (参考):**
  - **形式:** すべて大文字の `SNAKE_CASE`。列挙型の値と同様です。
  - **例:** `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT`
- **変数名 / パラメータ名 (Variable/Parameter Names) (参考):**
  - **形式:** `camelCase`。メソッド名やプロパティ名と同様です。
  - **例:** `userName`, `itemIndex`, `targetUrl`

#### 型とリテラルの表記

`core.md` で定義された標準型、拡張型、およびリテラルは、常にその**英語表記**で使用します。

- **型例:** `String`, `Number`, `Boolean`, `List<String>`, `Dictionary<String, Any>`, `UniqueID`, `Instant`, `Void`, `Any`, `ContentString`, `Persona`, `CodeBlock`, `Ref`, `Color`, etc.
- **リテラル例:** `True`, `False`, `Null`

#### 構造と参照

- **モジュール (`##`):** 全ての定義はモジュール内に記述します。
- **セクション (`###` 以下):** 文書構造の整理のために任意で使用できます。参照パスには影響しません。
- **クラス、インターフェース、列挙型 (`####`):** モジュール内で名前が一意になるように定義します。
- **クロスモジュール参照:** 他のモジュールの定義を参照する場合は、必ず完全修飾名 (`module.name.ClassName`) を使用します。

#### AIへの指示

- 英語で記述されたOOPD形式のプロンプトを解釈する際は、上記の命名規則や構造ルールを厳密に適用してください。
- ユーザーが命名規則に違反した記述を行った場合、それを指摘し、修正を促してください。
- 英語で応答を生成する際も、上記の命名規則およびフォーマットルールに従ってください。
- クロスモジュール参照が必要な場面で、ユーザーが完全修飾名を使用していない場合は、どのモジュールの定義か確認するか、文脈から最も可能性の高いものを補完してください（ただし、曖昧さが残る場合は確認を優先）。
