### OOPD 英語仕様 (English Specification)

#### はじめに

このドキュメントは、Object-Oriented Prompt Design (OOPD) において、**英語 (`en`)** でプロンプトを記述し、AIがそれを解釈・応答する際の**仕様とガイドライン**を定義します。英語はOOPDの**ハブ言語**であり、他の言語との翻訳の基準となるため、その仕様は特に重要です。

他の言語に共通する基本原則や記述ルールについては `core.md`, `format_common.md`, **`basic_terms.md`** を参照してください。

#### 基本原則

**重要:** 以下の原則は、英語 (`en`) でOOPD形式を記述し、AIがそれを解釈・応答する際の **絶対的なルール** です。他の文書で定義される「ユーザーフォーマット」の柔軟性 (`format_user.md` 参照) や、「対話モード選択」のプロセス (`interaction_mode_selection.md` 参照) は、**英語での対話には一切適用されません**。

- **ハブ言語:** 英語 (`en`) はOOPDのハブ言語です。全ての翻訳用語は内部的に英語ハブ名に紐付けられます。
- **単一フォーマット（定義フォーマットのみ適用）:** 英語でOOPD形式を記述する場合、他の言語のような「ユーザーフォーマット」と「定義フォーマット」の**概念的な区別は存在せず、常に `format_definition.md` で定義される規則に準拠した記述** を行います。このため、`format_user.md` で記述される緩やかなルール（例: 命名規則の逸脱許容や提案のみの対応）は **英語には適用されません**。
  - つまり、モジュール定義 (`##`) が必須です。
  - **【重要】配置制約:** クラス定義、インターフェース定義、グループ見出し (`#### Structure Definitions`, `#### Enum Definitions`) などの主要な定義要素は、**必ずモジュール定義 (`##`) よりも下の階層 (`###` 以下) に記述する必要があります。**
  - 定義される要素（クラス、メソッド等）は、後述する **英語命名規則に厳密に従う** 必要があります。命名規則に違反した場合、AIはその違反を指摘し、標準的な英語名をユーザーに **通知した上で自動的に適用** します。ユーザーがその名称を修正しない限り、AIは標準名を内部的に使用し続けます。
- **フォーマット確認のスキップ:** 上記の「単一フォーマット」原則に基づき、AIは英語での対話開始時に `interaction_mode_selection.md` で定義されるフォーマット確認手順を **実行しません**。
- **翻訳処理なし:** 入力プロンプトが英語で、出力も英語が指定されている場合、ハブ言語との間の翻訳処理は発生しません。AIは英語の定義を直接解釈し、英語で応答します。
- **ハブ名接頭辞の省略:** 英語で記述する場合、要素名（プロパティ、メソッド等）の前に `{英語ハブ名}::` という接頭辞を付ける必要は **ありません**。英語名のみを記述します。
- **他言語併記なし:** 見出しなどで、括弧 `()` などを用いて他の言語名を併記する必要は **ありません**。

#### 予約語との衝突禁止 (最重要)

**重要:** 英語でOOPD形式を記述する際も、ユーザー定義名（モジュール名、クラス名、メソッド名、プロパティ名など）は、OOPDの **予約語と絶対に衝突してはなりません。** これは `format_common.md` で詳細に定義されている **全言語共通の最重要ルール** であり、英語（ハブ言語）での記述においては特に厳守される必要があります。

**予約語** には主に以下が含まれます（ **衝突禁止対象となる予約語の完全な定義と、全言語横断的な適用の厳密なルールについては、必ず `format_common.md` の「予約語との衝突禁止」セクションを参照してください** ）：

- **基本用語** (`basic_terms.md` 参照): 例として `Class`, `Property`, `Module`, `baseclass`, `Optional` など。
- **標準型** (`basic_terms.md` 参照): 例として `String`, `Number`, `Boolean`, `List`, `Void`, `Any` など。
- **拡張型** (`extended_types.md` 参照): 例として `ContentString`, `Persona`, `CodeBlock`, `Color`, `Ref` など。
- **リテラル** (`basic_terms.md` 参照): 例として `True`, `False`, `Null`。

**注意:** `format_common.md` で定義されている通り、このルールは `basic_terms.md` に記載されている **全ての言語の固定キーワード** を含みます。

AIは、ユーザーがこれらの予約語（`format_common.md` の定義に基づく全予約語）を識別子として使用しようとした場合、 **必ず警告** し、異なる名前を使用するよう促してください。AI自身も、 **絶対にこれらの予約語をユーザー定義名として生成してはなりません。** 曖昧さを排除し、仕様の正確な解釈を保証するための **最重要ルール** です。

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
- **構造体名 (Struct Names):**
  - **形式:** `PascalCase`。クラス名と同様。
  - **例:** `Appearance`, `Coordinate`
- **定数名 (Constant Names) (参考):**
  - **形式:** すべて大文字の `SNAKE_CASE`。列挙型の値と同様です。
  - **例:** `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT`
- **変数名 / パラメータ名 (Variable/Parameter Names) (参考):**
  - **形式:** `camelCase`。メソッド名やプロパティ名と同様です。
  - **例:** `userName`, `itemIndex`, `targetUrl`

#### 型とリテラルの表記

`basic_terms.md` で定義された標準型、リテラル、および `extended_types.md` で定義された拡張型は、常にその**英語表記**で使用します。

- **型例:** `String`, `Number`, `Boolean`, `List<String>`, `Dictionary<String, Any>`, `UniqueID`, `Instant`, `Void`, `Any`, `ContentString`, `Persona`, `CodeBlock`, `Ref`, `Color`, etc.
- **リテラル例:** `True`, `False`, `Null`

#### 構造と参照

- **モジュール (`##`):** 全ての定義はモジュール内に記述します。
- **セクション (`###` など):** 文書構造の整理のために任意で使用できます。参照パスには影響しません。
- **見出し (`####`):**
  - **個別クラス/インターフェース:** `#### ClassName: Description` または `#### InterfaceName: Description` (簡易説明文必須) の形式。
    - 見出し下に詳細説明を記述可能。
  - **グループ見出し:** `#### Structure Definitions` または `#### Enum Definitions` を使用します。これらは **`basic_terms.md`** で定義された固定の英語名です。
    - 見出し下に詳細説明を記述可能。
- **リスト形式要素 (`-`):** プロパティ、メソッド、イベント、列挙型、構造体を定義します。
  - **リスト開始キーワード:** リストを開始する際は、**`basic_terms.md`** で定義された基本用語 (`Property`, `Method`, `Event`) をボールド表記で使用します (例: `**Property:**`, `**Method:**`, `**Event:**`)。
  - **プロパティ:** - \`propertyName: Type\`: Description (オプションの場合 `, Optional` を追加。`Optional` は `basic_terms.md` 参照)
  - **メソッド:** - \`methodName(argName: Type = defaultValue): ReturnType\`: Description (戻り値が `Void` の場合は省略非推奨)
  - **イベント:** - \`eventName(argName: Type)\`: Description (戻り値が `Void` の場合は省略推奨、引数なしでも `()` は必須)
  - **列挙型:** - \`EnumName = VALUE\_ONE, VALUE\_TWO, ...\` \[: Description] (リスト形式、`#### Enum Definitions` 下に記述。区切りは `=`、バッククォートは値リストまで)
  - **構造体:** - \`StructName\`: Description (リスト形式、`#### Structure Definitions` 下に記述)
- **基底クラス/インターフェース実装:**
  - クラス定義内で、対応する基本用語 (**`basic_terms.md`** 参照) をボールド表記で使用します。
  - **継承:** `**baseclass:** BaseClassName`
  - **インターフェース実装:** `**Interface:** InterfaceName1, InterfaceName2, ...`
- **クロスモジュール参照:** 他のモジュールの定義を参照する場合は、必ず完全修飾名 (`module.name.ClassName`) を使用します。

#### AIへの指示

- 英語で記述されたOOPD形式のプロンプトを解釈する際は、上記の命名規則や構造ルールを厳密に適用してください。
- ユーザーが命名規則に違反した記述を行った場合、それを指摘し、修正を促してください。
- **予約語との衝突禁止ルール**を厳守し、ユーザーが予約語を使用しようとした場合は警告してください。AI自身も予約語を識別子として使用しないでください。
- 英語で応答を生成する際も、上記の命名規則およびフォーマットルールに従ってください。要素名の `{英語ハブ名}::` 接頭辞は不要です。
- クロスモジュール参照が必要な場面で、ユーザーが完全修飾名を使用していない場合は、どのモジュールの定義か確認するか、文脈から最も可能性の高いものを補完してください（ただし、曖昧さが残る場合は確認を優先）。
