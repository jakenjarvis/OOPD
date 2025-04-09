### OOPD Format: Definition Format Specification

#### What is the Definition Format?

The Definition Format is a **strict and formal description format for sharing definitions created based on OOPD with others or reusing them across different sessions or environments**. It serves as the finalized version of a definition, aiming to ensure **reversibility** between languages and **consistency** in interpretation.

#### About This Document

This document (`format_definition.md`) explains the strict rules specific to the Definition Format. For common rules, refer to `format_common.md`. The Definition Format must follow the rules below, regardless of the prompt's description language.

#### Mandatory Rules and Formatting

- **Co-notation of English Hub Names (for Non-English Languages):**
  - **(Note: This rule applies when describing in languages other than English. When describing in English, use only the English name; co-notation of the hub name is unnecessary. See `english_specification.md`.)**
  - For "User-Defined Identifiers" subject to AI translation, such as class names, interface names, enum names, etc., the **finalized English hub name must always be co-notated**. See the individual description methods below for details.
  - English hub names follow the **English Naming Conventions** defined in `english_specification.md`.
  - The native language notation for User-Defined Identifiers follows the **standard naming conventions** defined in the translation rules for the target language (within `translation_rules/`).

- **Strict Application of Naming Conventions:**
  - As mentioned above, the **standard naming conventions defined for each language must be strictly applied** to both the native language name and the English hub name. (When describing in English, only the English Naming Conventions defined in `english_specification.md` apply.)
  - Module names must follow the English naming conventions defined in `english_specification.md`, and ensuring global uniqueness is strongly recommended.

- **Recognition of English Hub Name and Native Name:**
  - For elements co-notated in the format `{English Hub Name}::{Native Name}`, the AI **recognizes both the English Hub Name and the Native Name as valid identifiers** pointing to that element.

- **Cross-Reference:**
  - **Within the Same Module:** When referencing class names, etc., **must describe using only the native language name** (e.g., `propertyName: CustomerClass`). Do not describe the English hub name. The AI identifies the definition within the module from context.
  - **Across Different Modules:** If the referenced class, etc., belongs to another module, it **must be specified using the fully qualified name (`module.name.ClassName`)**. The same applies to type specifications. (Example: `creator (com.example.common.User)`)

- **Recommendation for Description Texts:**
  - **It is strongly recommended to write description texts** for each module, section, class, interface, method, property, etc., to clarify their purpose and meaning. This aids AI interpretation and promotes human understanding. Describe description texts in the prompt description language.

- **Module Definition (`##`):**
  - All definitions must be described within a module.
  - Format: `## {EnglishModuleName}`
  - Global uniqueness for module names is recommended (see `english_specification.md`).
  - The module's native name or detailed description text can be described as regular text below the `##` line (optional).

- **Headings (Class `####`, Interface `####`, Section `###`/`####`/..., Structure Definition `####`, Enum Definition `####`):**
  - **Class/Interface (Individual Definition):**
    - Format (Native): `{HeadingLevel} {NativeName} ({EnglishHubName}): {TitleSummary}`
    - Format (English): `{HeadingLevel} {EnglishName}: {TitleSummary}`
    - **【Important】The order of names is `{NativeName} ({EnglishHubName})` or `{EnglishName}`. Be careful not to reverse it.**

    - **【1. Title Summary (after `:` on the heading line)】**
      - **Role:** A title-like summary, as part of the heading, indicating the **core essence of the class/interface in one phrase**.
      - **Content:** Most succinctly expresses **"what"** the element is. Does not include specific feature lists or detailed context.
      - **Mandatory:** **Required**.
      - **Length:** Must be **extremely concise**. Generally described in **one line and as a short sentence**.
      - **Note for AI Generation:** The AI should generate the most concise and accurate expression capturing the essence of this element. Do not include redundant explanations or content that should be in the detailed description below. Also, **as it is a heading, a period should not be placed at the end of the line.** This needs judgment according to each language.
      - **Good Examples:**
        - `E-commerce site customer data model`
        - `Asynchronous task execution contract`
        - `Environment configuration value provider`
        - `3D object geometric transformation`
      - **Bad Examples:**
        - `Class for managing customer profiles and order history of an e-commerce site` (← A bit long, suitable for detailed description)
        - `This is a customer class` (← Meaningless)
        - Omitting it (← Required)

    - **【2. Detailed Description Text (below the heading line)】**
      - **Role:** The place to **explain in detail the purpose, functionality, usage methods, constraints, background, related information, etc.** of the class/interface, as **body text** independent of the heading.
      - **Content:**
        - Specific functions and scope of responsibility
        - Assumed usage scenarios
        - Design decisions and background
        - Important constraints and notes (e.g., thread safety, performance considerations)
        - References to related other classes or interfaces
        - References to external documents
        - Special instructions to the AI (e.g., "Ensure methods of this class guarantee idempotency")
      - **Mandatory:** **Optional**, but **strongly recommended** to deepen understanding of the class/interface. Should be described especially for complex or important elements.
      - **Format:** Can be freely described over multiple lines as regular Markdown text. Lists, emphasis, code blocks (` ``` `), etc., can also be used.
      - **Note for AI Generation:** The AI should describe the information necessary for understanding the element in a structured and easy-to-understand manner. It needs to provide more detailed information rather than simply repeating the content described in the title summary.

            ```markdown
            記述例 (日本語):
            #### 顧客クラス (Customer): ECサイトの顧客データモデル。

            このクラスは、ECサイトにおける顧客の基本情報（氏名、連絡先）、配送先住所リスト、および過去の注文履歴（直近100件）を一元的に管理します。
            データの整合性を保ち、関連サービス（推奨エンジン、サポートシステム）へ最新の情報を提供することが主な責務です。
            個人情報保護の観点から、メールアドレス等の機密情報へのアクセスは厳格に制御されます。
            インスタンス生成時には、必須項目（氏名、メールアドレス）のバリデーションを実行してください。
            ```

            *(Translator's Note: Japanese Markdown block retained as per instruction.)*

            ```markdown
            Description Example (English):
            #### Customer: E-commerce site customer data model

            This class centrally manages customer base information (name, contact), shipping address list, and past order history (latest 100) in the e-commerce site.
            Its primary responsibility is to maintain data integrity and provide up-to-date information to related services (e.g., recommendation engine, support system).
            Access to sensitive information like email addresses is strictly controlled due to privacy concerns.
            Validate required fields (name, email) upon instance creation.
            ```

    *(`Class`, `Interface` Basic Term definitions in `basic_terms.md`)*

  - **Section:**
    - Defined using Markdown headings (`###`, `####`, `#####`, etc.).
    - Format: `{HeadingLevel} {NativeName} ({EnglishHubName})` or `{HeadingLevel} {NativeName} ({EnglishHubName}): {DescriptionText}`
    - **Description text is optional**.
    - **If English is the native language:** Only `{EnglishName}` is used, parentheses for the English hub name are unnecessary. Rules for description text are the same as above.
    - Following the rules in `format_common.md`, multiple levels (nesting) are possible.
    - **【Important】** Class definitions (`#### {IndividualClassName}`), Interface definitions (`#### {IndividualInterfaceName}`), `#### {FixedNameForStructureDefinitions}` group, `#### {FixedNameForEnumDefinitions}` group, etc., can be placed not only directly under the module but also within sections of any level.
    - **【Constraint】However, these definition elements (classes, interfaces, group headings) MUST be described at a level below the Module definition (`##`) (i.e., `###` or lower).** They cannot be placed at the top level or the same level as the Module. (This is to maintain structural consistency when combining multiple definition files.)

  - **`#### {Fixed name for structure definitions}` / `#### {Fixed name for enum definitions}` (Group Headings):**
    - As instructed for reference in `format_common.md`, use the **fixed heading name** for each language defined in **`basic_terms.md`** (e.g., `#### 構造体定義` in Japanese, `#### Structure Definitions` in English).
    - These are group headings for organizing structure definitions and enum definitions, respectively, and can be used optionally.
    - Individual struct or enum definitions must be described under these group headings in list format (`-`).
    - It is not necessary to co-notate the English hub name in parentheses `()` for group headings.
    - If necessary, a description for the entire group can be written below the group heading.
        *(Basic Term definitions in `basic_terms.md`)*

- **Element Names (Property Name, Method Name, Event Name, Enum Definition Name, Enum Value, Struct Definition Name):**
  - Native language name is "primary", English hub name is "secondary".
  - Use the English hub name as a **prefix**, connected to the native language name with double colons `::`.
  - Basic Format: `{EnglishHubName}::{NativeName}`
  - **(For non-English languages)** As above.
  - **If English is the native language:** The prefix (`{EnglishHubName}::`) is unnecessary. Describe only the English name following the rules in `english_specification.md`.

- **Definition of List Format Elements (Property, Method, Event, Enum, Struct):**
  - Start the line with a Markdown list hyphen `-`.

  - **List Start Keyword:** When starting each list (property list, etc.), describe the corresponding **Basic Term** in bold notation, followed by a colon `:`. Refer to **`basic_terms.md`** for the Basic Terms to use.
    - Example (Japanese): `**プロパティ:**`, `**メソッド:**`, `**イベント:**`
    - Example (English): `**Property:**`, `**Method:**`, `**Event:**`

  - **Scope of Backticks (`\``):**
    - (Compliant with `format_common.md`)
    - **Property, Method, Event:** Enclose **only** the main part of the definition (from the space after the hyphen up to the type/return type specification). Do not enclose the description.
    - **Enum, Struct (Individual Definition):** Enclose **only** the element name part (`{EnglishHubName}::{NativeName}` or `{EnglishName}`). Do not enclose the description or value list.

  - **【Common Rule】Description of Explanations and Instructions:**
    - For each element definition (property, method, etc.), you can write an explanation describing its purpose, usage, constraints, instructions, etc.
    - The description text is written **after** the colon `:` at the end of the definition line, or **on the following line(s)**.
    - It can be described over **multiple lines**.
    - Description text is written as **regular Markdown text** and can include Markdown elements like lists (`-`, `*`, `1.`), emphasis (`**bold**`, `*italic*`), etc.
    - You can also omit the brief explanation after the colon `:` on the definition line and start the detailed explanation from the next line.
    - If the description text is short, it is recommended to write it on a single line if possible.
    - **Note:** Whether the description text is required/optional depends on the element type (required for struct, optional for enum). See the definition rules for each element for details.
    - **【Regarding Notation within Description Texts (Strict Adherence - Absolute Prohibition)】**
      - **1. Absolute Non-use of Backticks (`\``):** To ensure the readability of description texts and the accuracy of AI translation/interpretation, the use of **inline backticks within description texts is absolutely prohibited for any reason whatsoever.** Even when referring to other definition elements (property names, method names, type names, enum values, etc.) or technical terms, **must describe them as regular text** without enclosing them in backticks.
      - **2. Absolute Prohibition of English Co-notation:** Description texts should, in principle, be described **only** in the prompt's description language. To avoid critically impairing the accuracy and consistency of AI translation processing, **co-notating English names** within description texts using formats like `{EnglishHubName}::{NativeName}` or parentheses (`(englishName)`) is **absolutely prohibited.** The AI has the capability to determine necessary information from context, making such co-notation unnecessary and harmful.

            ```markdown
            記述例（プロパティの場合。他も同様）:
            **プロパティ:**

            *(最も推奨: 短い記載で済む場合)*
            - `propertyName1::プロパティ名1: Type`: これは一行で完結する説明です。

            *(推奨: 簡易説明に加え、詳細な説明が必要な場合)*
            - `propertyName2::プロパティ名2: Type`: ここに簡易説明を記述します。
              これは簡易説明に加え、複数行にわたる詳細な説明や指示の例です。
              - 詳細な仕様をリストで記述できます。
              - **重要:** この値は必ず正の数にしてください。

            *(詳細な説明や手順が多く必要な場合)*
            - `propertyName3::プロパティ名3: Type`:
              これは複数行にわたる説明や指示の例です。
              1. 詳細な仕様をリストで記述できます。
              2. 詳細な仕様をリストで記述できます。
              3. 詳細な仕様をリストで記述できます。
              4. 詳細な仕様をリストで記述できます。
              5. 詳細な仕様をリストで記述できます。
              6. 詳細な仕様をリストで記述できます。
              7. 詳細な仕様をリストで記述できます。
              8. 詳細な仕様をリストで記述できます。
              - **重要:** この値は必ず正の数にしてください。
            ```

            *(Translator's Note: Japanese example retained for context)*

            ```markdown
            記述例（列挙型の場合）:
            #### 列挙型定義

            *(最も推奨: 短い記載で済む場合)*
            - `ProcessingStatus::処理状態列挙型 = PENDING::待機中, RUNNING::実行中, COMPLETED::完了, FAILED::失敗`: 非同期処理の全体的な状態を示します。
            - `ColorFlag::色フラグ列挙型 = RED::赤, GREEN::緑, BLUE::青`: 基本的な色要素を表すビットフラグです。組み合わせて色を表現します (例: 紫 = 赤 + 青)。

            *(推奨: 簡易説明に加え、詳細な説明が必要な場合)*
            - `ErrorCode::エラーコード列挙型 = NONE::エラーなし, TIMEOUT::タイムアウト, INVALID_INPUT::不正な入力, SERVER_ERROR::サーバーエラー, UNKNOWN::不明なエラー`:
              処理が失敗状態になった場合の具体的な原因を示します。
              - タイムアウト: 規定時間内に処理が完了しなかった場合に設定されます。ネットワーク状況を確認してください。
              - 不正な入力: 入力データ形式が正しくないか、必須項目が欠落している場合に発生します。入力仕様書を参照してください。
              - サーバーエラー: サーバー内部で予期せぬ問題が発生しました。管理者に連絡してください。ログIDを併せて伝えると調査がスムーズです。

            *(説明がなくとも一般的に理解可能な場合)*
            - `Direction::方向列挙型 = NORTH::北, SOUTH::南, EAST::東, WEST::西`
            - `Size::サイズ列挙型 = SMALL::小, MEDIUM::中, LARGE::大`
            - `DayOfWeek::曜日列挙型 = MONDAY::月曜日, TUESDAY::火曜日, WEDNESDAY::水曜日, THURSDAY::木曜日, FRIDAY::金曜日, SATURDAY::土曜日, SUNDAY::日曜日`
            ```

            *(Translator's Note: Japanese example retained for context)*

- **Property Definition:**
  - Format (Native): - \`{EnglishHubName}::{NativeName}: {TypeName}\[, {OptionalSpecifier}]\`: {Description}
  - Format (English): - \`{EnglishName}: {TypeName}\[, {OptionalSpecifier}]\`: {Description}
  - **Type Name:**
    - **Standard/Extended Types:** Must use English notation (`String`, `Number`, `List<String>`, `Color`, etc.) (**Definitions in `basic_terms.md` and `extended_types.md`**).
    - **User-Defined Types (Class, Interface, Enum, Struct):** **【Important】Must reference using only the native language name** (e.g., `顧客クラス`, `色フラグ列挙型`). Do not describe the English hub name.
  - **Optional Item:**
    - In property definitions, optional items can be indicated by appending `, {OptionalSpecifier}` after the type name (Refer to **`basic_terms.md`** for the definition of the Basic Term **`Optional`** (`ja`: `オプション`)).
      - Example (Japanese): - \`プロパティ名: String, オプション\`
      - Example (English): - \`propertyName: String, Optional\`
  - **Description:** Follows **【Common Rule】Description of Explanations and Instructions** above.

- **Method Definition:**
  - Format (Native): - \`{EnglishHubName}::{NativeName}({ArgumentList}): {ReturnTypeName}\`: {Description}
  - Format (English): - \`{EnglishName}({ArgumentList}): {ReturnTypeName}\`: {Description}
  - **Return Type Name:** Same rules as property type names (Standard types in English, User-defined types in native language). `Void` can be omitted, but **description is recommended**.
  - **Argument List:** Comma-separated `{argumentName}: {TypeName}` or `{argumentName}: {TypeName} = {defaultValue}`.
  - **Argument Name:** Use only native language notation; do not attach English hub name. (English notation if English)
  - **Argument Type Name:** Same rules as property type names (Standard types in English, User-defined types in native language).
  - **Default Value (`= {defaultValue}`):**
    - In method definitions, default values can be expressed by appending `= {defaultValue}` after the argument's type name.
    - **Notation for Default Value:**
      - Literals (`True`, `False`, `Null`, numbers, strings) are described as is (**Definitions in `basic_terms.md`**).
      - **Enum Values:** **【Important】Must describe using the native language name** (e.g., `= 赤`, `= 未着手`). Do not describe the English hub name. (English notation if English)
      - Example (Japanese): - \`メソッド名(フラグ: Boolean = True, ステータス: タスク状態 = 未着手): Void\`
      - Example (English): - \`methodName(flag: Boolean = True, status: TaskStatus = NOT_STARTED): Void\` (*Note: Enum value also English if English*)
  - **【Important】Even if there are no arguments, must describe empty parentheses `()`.** (e.g., `methodName()`)
  - **Description:** Follows **【Common Rule】Description of Explanations and Instructions** above.

- **Event Definition:**
  - Format (Native): - \`{EnglishHubName}::{NativeName}({ArgumentList})\`: {Description}
  - Format (English): - \`{EnglishName}({ArgumentList})\`: {Description}
  - **Return Value:** Usually `Void`, but **omitting the description is recommended**.
  - **Argument List:** Follows the same rules as method definition. Argument name, type name, default value are in native language notation (English notation if English).
  - **Argument Name:** Follows the same rules as method definition. Argument name, type name, default value are in native language notation (English notation if English).
  - **【Important】Even if there are no arguments, must describe empty parentheses `()`.** (e.g., `eventName()`)
  - **Description:** Follows **【Common Rule】Description of Explanations and Instructions** above.

- **Enum Definition (Individual):**
  - Must be described under the `#### {Fixed name for enum definitions}` group heading (or within a section under it) in **list format (`-`)**.
  - Format (Native): - \`{EnglishHubName}::{NativeName} = {ValueList}\` \[: {Description}]
  - Format (English): - \`{EnglishName} = {ValueList}\` \[: {Description}]
  - **Separator:** Use `=` (equals sign) between the enum name and the value list.
  - **Value List:** Enumerate values in the format `{EnglishHubName}::{NativeName}` (or English only), separated by commas. Recommending space after comma (e.g., `RED::赤, GREEN::緑`).
  - Backticks: Backticks (\`) start after the space following the hyphen and enclose **up to the end of the value list**. Do not enclose the description text.
  - **Description:** Description can be written after the colon `:` (**optional**). Follows **【Common Rule】Description of Explanations and Instructions** above.

- **Struct Definition (Individual):**
  - Must be described under the `#### {Fixed name for structure definitions}` group heading (or within a section under it) in **list format (`-`)**.
  - Format (Native): - \`{EnglishHubName}::{NativeName}\`: {Description}
  - Format (English): - \`{EnglishName}\`: {Description}
  - **Description:** Description is written after the colon `:` (**required**). Follows **【Common Rule】Description of Explanations and Instructions** above.

    **Guideline for Using Structs**
  - **Simple Data Container Recommended:** Structs are recommended for simple data holding purposes where the AI can infer the content from the name and description, like `Coordinate` struct.
  - **Explicit Definition Discouraged:** Explicitly defining elements using `**Property:**`, etc., like classes, is **strongly discouraged**.
  - **Recommended Specification:** Describe necessary properties in **natural language within the struct's description text** (e.g., "The coordinate struct holds X and Y coordinates"). The AI prioritizes this instruction.

        ```markdown
        記述例（構造体の場合）:
        #### 構造体定義

        *(最も推奨: 短い記載で済む場合)*
        - `RgbColor::Rgb色構造体`: RGB形式の色情報 (赤、緑、青の各値、通常 0-255) を保持します。アルファ値は含みません。
        - `VersionInfo::バージョン情報構造体`: ソフトウェアやコンポーネントのバージョン番号（メジャー、マイナー、パッチ）を格納します。

        *(推奨: 簡易説明に加え、詳細な説明が必要な場合)*
        - `RenderingOptions::描画オプション構造体`: レンダリング時の詳細設定をまとめた構造体です。
          このオプション設定は、リアルタイムレンダリングパイプライン全体に影響します。
          特にアンチエイリアスレベルとテクスチャ品質はパフォーマンスに大きく関わるため、ターゲット環境に応じて慎重に設定してください。
          デフォルト設定については、別ドキュメント「デフォルト描画設定」を参照してください。

        *(プロパティを自然言語で記載する場合)*
        - `Point::座標構造体`: 2次元空間における点の位置を表します。X座標とY座標の2つの数値を持ちます。座標系の原点は左上とします。
        - `Address::住所構造体`: 住所情報を構成する要素を保持します。郵便番号、都道府県、市区町村番地を持ち、オプションで建物名部屋番号を持つことができます。

        *(強く非推奨: プロパティを明確に記載する場合。クラスの使用を検討してください)*
        - `Size::寸法構造体`: オブジェクトの幅と高さを表します。 *(注意: 非推奨の記述方法です。クラスの使用を検討してください)*
          単位はピクセルを基本とします。

          **プロパティ:**
          - `width::幅: Number`: オブジェクトの横幅。
          - `height::高さ: Number`: オブジェクトの縦幅。
        ```

        *(Translator's Note: Japanese example retained for context)*

  - **Using Classes:** If detailed definition of properties or methods is needed, **use a Class** instead of a struct.

- **Implementation of Base Class and Interfaces:**
  - Within the class definition, use the corresponding **Basic Term** in bold notation to indicate the implemented base class or interfaces. Refer to **`basic_terms.md`** for the Basic Terms to use.
  - **Inheritance:**
    - Format (Japanese Example): `**基底クラス:** {BaseClassNameInNative}` (Keyword is Basic Term for `baseclass`)
    - Format (English Example): `**baseclass:** {BaseClassName}` (Keyword is Basic Term for `baseclass`)
    - **【Important】Must reference using only the native language name.**
  - **Interface Implementation:**
    - Format (Japanese Example): `**インターフェース:** {InterfaceName1InNative}, {InterfaceName2InNative}, ...` (Keyword is Basic Term for `Interface`)
    - Format (English Example): `**Interface:** {InterfaceName1}, {InterfaceName2}, ...` (Keyword is Basic Term for `Interface`)
    - **【Important】Must reference using only the native language name.** Use comma separation for multiple specifications.

- **Type References:**
  - When specifying types in properties, arguments, or return values, even when referencing user-defined classes or enums, describe **only the native language name**; do not attach the English hub name.

- **Description Example:**

    ```markdown
    記述例（日本語での定義全体の例）:
    ## com.example.shapes

    このモジュールは、基本的な図形とその操作に関連する定義を含みます。

    ### 定義グループ

    #### 列挙型定義

    - `ShapeType::図形種類列挙型 = CIRCLE::円, RECTANGLE::長方形, TRIANGLE::三角形`: 図形の基本的な種類を示します。
    - `ColorType::色列挙型 = RED::赤, BLUE::青, GREEN::緑, BLACK::黒, WHITE::白`: 図形の色を表します。

    #### 構造体定義

    - `Coordinate::座標構造体`: 2次元空間における点の位置を表します。X座標とY座標の2つの数値を持ちます。

    ### インターフェース定義

    #### 描画可能インターフェース (Drawable): 図形が描画可能であることを示すコントラクト

    このインターフェースを実装するクラスは、自身を描画する機能を持つ必要があります。

    **メソッド:**

    - `draw::描画実行(): Void`: 図形を描画します。具体的な描画処理は実装クラスに依存します。

    ### 基底クラス定義

    #### 基本図形クラス (BaseShape): 全ての図形の基底となるクラス

    図形に共通する基本的なプロパティを提供します。

    **プロパティ:**

    - `id::識別子: UniqueID`: 図形を一意に識別するためのIDです。
    - `creationTime::作成日時: Instant`: この図形オブジェクトが作成された日時（ISO8601形式）です。
    - `shapeType::図形種別: 図形種類列挙型`: 図形の種類を示します。

    ### 図形クラス定義

    #### 円クラス (Circle): 円形を表す図形クラス

    **基底クラス:** 基本図形クラス
    **インターフェース:** 描画可能インターフェース

    このクラスは円を表現し、中心座標と半径を持ちます。基本的な図形操作メソッドを提供します。

    **プロパティ:**

    - `center::中心座標: 座標構造体`: 円の中心点の座標です。
    - `radius::半径: Number`: 円の半径です。負の値は許可されません。
    - `color::色: 色列挙型`: 円を塗りつぶす色です。
    - `isDrawn::描画済みフラグ: Boolean`: 円が既に描画されたかどうかを示すフラグです。
    - `lineStyle::線種: String, オプション`: 円の輪郭線のスタイル（例: 実線、破線）を指定します。指定がない場合はデフォルトの線種が使用されます。
    - `attributes::属性辞書: Dictionary<String, Any>`: 円に関する追加のカスタム属性を格納します。キーは文字列、値は任意型です。
    - `relatedShapes::関連図形リスト: List<UniqueID>`: この円に関連する他の図形の識別子リストです。

    **メソッド:**

    - `calculateArea::面積計算(): Number`: 円の面積を計算して返します。
    - `move::移動(移動先座標: 座標構造体): Void`: 円の中心座標を指定された新しい座標に移動します。
    - `resize::リサイズ(倍率: Number = 1.0): Boolean`: 円の半径を指定された倍率で変更します。成功した場合は真を返します。デフォルト倍率は1.0（変更なし）です。
    - `setColor::色設定(新しい色: 色列挙型 = 赤): Void`: 円の色を指定された新しい色に設定します。デフォルトは赤です。
    - `draw::描画実行(): Void`: 円を描画します。描画可能インターフェースの実装です。描画後、描画済みフラグを真にします。

    **イベント:**

    - `click::クリックイベント()`: 円がクリックされたときに発生します。
    - `sizeChanged::サイズ変更イベント(新半径: Number)`: 円のサイズ（半径）が変更されたときに発生します。新しい半径を引数として渡します。
    - `colorChanged::色変更イベント(旧色: 色列挙型, 新色: 色列挙型)`: 円の色が変更されたときに発生します。変更前の色と変更後の色を引数として渡します。
    ```

    *(Translator's Note: Japanese Markdown block retained as per instruction.)*

    ```markdown
    Description Example (Overall example of definition in English):
    ## com.example.shapes

    This module contains definitions related to basic shapes and their operations.

    ### Definition Groups

    #### Enum Definitions

    - `ShapeType = CIRCLE, RECTANGLE, TRIANGLE`: Indicates the basic types of shapes.
    - `ColorType = RED, BLUE, GREEN, BLACK, WHITE`: Represents the color of a shape.

    #### Structure Definitions

    - `Coordinate`: Represents the position of a point in 2D space. It holds two numeric values: X coordinate and Y coordinate.

    ### Interface Definitions

    #### Drawable: Contract indicating that a shape can be drawn

    Classes implementing this interface must have the capability to draw themselves.

    **Method:**

    - `draw(): Void`: Draws the shape. The specific drawing process depends on the implementing class.

    ### Base Class Definitions

    #### BaseShape: Base class for all shapes

    Provides fundamental properties common to all shapes.

    **Property:**

    - `id: UniqueID`: A unique identifier for the shape.
    - `creationTime: Instant`: The date and time (ISO8601 format) when this shape object was created.
    - `shapeType: ShapeType`: Indicates the type of the shape.

    ### Shape Class Definitions

    #### Circle: Shape class representing a circle

    **baseclass:** BaseShape
    **Interface:** Drawable

    This class represents a circle and holds its center coordinates and radius. It provides basic shape manipulation methods.

    **Property:**

    - `center: Coordinate`: The coordinates of the center point of the circle.
    - `radius: Number`: The radius of the circle. Negative values are not allowed.
    - `color: ColorType`: The color used to fill the circle.
    - `isDrawn: Boolean`: A flag indicating whether the circle has already been drawn.
    - `lineStyle: String, Optional`: Specifies the style of the circle's outline (e.g., solid, dashed). If not specified, a default line style is used.
    - `attributes: Dictionary<String, Any>`: Stores additional custom attributes related to the circle. Keys are strings, values are of any type.
    - `relatedShapes: List<UniqueID>`: A list of identifiers for other shapes related to this circle.

    **Method:**

    - `calculateArea(): Number`: Calculates and returns the area of the circle.
    - `move(destination: Coordinate): Void`: Moves the center of the circle to the specified new coordinates.
    - `resize(scaleFactor: Number = 1.0): Boolean`: Changes the radius of the circle by the specified scale factor. Returns true on success. The default scale factor is 1.0 (no change).
    - `setColor(newColor: ColorType = RED): Void`: Sets the color of the circle to the specified new color. The default is red.
    - `draw(): Void`: Draws the circle. Implementation of the Drawable interface. Sets the isDrawn flag to true after drawing.

    **Event:**

    - `Click()`: Occurs when the circle is clicked.
    - `SizeChanged(newRadius: Number)`: Occurs when the size (radius) of the circle is changed. Passes the new radius as an argument.
    - `ColorChanged(oldColor: ColorType, newColor: ColorType)`: Occurs when the color of the circle is changed. Passes the old color and the new color as arguments.
    ```

#### Output Rules

- If the AI is instructed to output in "Definition Format", it **must enclose the entire OOPD format (Markdown format) output using code blocks "(`~~~Markdown`) ... (`~~~`)"**. (However, code blocks within the OOPD format use "(` ``` `)")
- When outputting instance data, use **YAML format code blocks "(` ```yaml `) ... (` ``` `)"** as the standard. Other formats like JSON may be used if specifically instructed by the user.

#### Definition Format Finalization Process

- Typically, the "Definition Format" is generated by the AI based on content created by the user in "User Format".
- During generation, the AI automatically checks for compliance with the mandatory rules above (English name co-notation, naming conventions, module affiliation, etc.).
- If issues are found during the check (e.g., naming convention violation, unclear English name, undefined module), the AI points out the issues to the user and prompts for correction. The AI may also suggest corrections.
- The "Definition Format" is finalized when the user resolves the issues through dialogue with the AI and confirms/approves the content.
