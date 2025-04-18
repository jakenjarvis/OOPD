## 対話モード選択と初期手順 (英語以外の言語向け)

### 目的

この文書は、AIがユーザーと **英語以外の言語** でObject-Oriented Prompt Design (OOPD) に基づく対話を開始する際の **初期手順** と、ユーザーが選択する作業フォーマットに応じたAIの **基本的な対話モード** を定義します。これらの手順とモードは、以降のOOPD仕様（特にフォーマット関連）の解釈と適用の前提となります。

**注意:** ユーザーの使用言語が **英語 (`en`)** の場合、OOPDの仕様 (`english_specification.md` 参照) に従い、フォーマットの区別なく常に **定義フォーマットに準拠した厳密なモード** で動作します。そのため、英語での対話においては、この文書に記述された **フォーマット確認手順は適用されません** 。

### 初期フォーマット確認 (英語以外の言語)

AIは、ユーザーが **英語以外の言語** でOOPDを用いたクラス設計、定義、または関連する操作を開始したと判断した場合、以下の手順で **最初に作業フォーマットを確認** してください。

1. **確認:** ユーザーに対し、「OOPDの作業を **ユーザーフォーマット (`User Format`)** と **定義フォーマット (`Definition Format`)** のどちらで行いますか？」と明確に質問してください。
2. **説明:** 質問と同時に、それぞれのフォーマットの主な特徴を以下のように簡潔に説明してください。
   - **ユーザーフォーマット (`User Format`):**
     - 主にあなたの母国語で記述し、より柔軟な記述が可能です。
     - 命名規則は比較的緩やかです（AIは標準名を提案しますが、強制はしません）。
     - 英語ハブ名はAIが内部的に管理します。
     - 個人での利用、アイデアの下書き、迅速なプロトタイピングに適しています。
   - **定義フォーマット (`Definition Format`):**
     - 英語ハブ名を併記し、標準的な命名規則に従う必要があります。
     - 構造化されており、定義の共有や再利用に適しています。
     - **特に、ご自身で名称の詳細にこだわらない場合や、標準的な命名規則に沿った定義を効率的に作成したい場合は、AIが標準名を自動適用（※）するこちらのフォーマットでの作業をお勧めします。**
       *(※自動適用時にはAIから通知があります)*
3. **ユーザー選択:** ユーザーの選択（「ユーザーフォーマット」または「定義フォーマット」）を受け付けます。

### フォーマット選択に基づくAIの動作モード (英語以外の言語)

ユーザーがフォーマットを選択した後、AIは以下の通り、 **対応する動作モード** に切り替わり、以降の対話におけるOOPD関連の指示を解釈・実行してください。

- **ユーザーフォーマット (`User Format`) モード選択時:**
  - AIは、ユーザーフォーマットの仕様 (`format_user.md` 参照) に基づき、柔軟な解釈を行います。
  - ユーザーが指定した名称が標準命名規則から逸脱している場合、AIは標準名を **提案するのみ** とし、使用の確認や自動適用は行いません。ユーザーが使用した名称を尊重します。
  - その他のユーザーフォーマット固有のルールに従ってください。

- **定義フォーマット (`Definition Format`) モード選択時:**
  - AIは、定義フォーマットの仕様 (`format_definition.md` 参照) に基づき、厳密な解釈と検証を行います。
  - ユーザーが指定した名称が標準命名規則に違反している場合、AIは標準名を算出し、ユーザーに **通知した上で自動的に適用** します。
  - 英語ハブ名の併記やクロスモジュール参照の完全修飾名要求など、その他の定義フォーマット固有のルールを厳密に適用してください。

### モードの変更 (英語以外の言語)

ユーザーは対話の途中でフォーマットの変更を希望する場合があります。AIはユーザーの指示に従い、以下の点を考慮してモードを切り替えてください。

- **ユーザーフォーマットから定義フォーマットへの変更:**
  - ユーザーから「定義フォーマットに変換して」といった指示があった場合、AIは現在の定義内容を定義フォーマットの厳密な規則（英語ハブ名併記、標準命名規則の適用など）に基づいて整形し直します。
  - この際、AIは必要に応じて英語ハブ名の推論・確定を行い、命名規則の検証と自動適用（通知付き）を実行します。

- **定義フォーマットからユーザーフォーマットへの変更:**
  - ユーザーから「ユーザーフォーマットで編集したい」といった指示があった場合、AIは以下のモードに切り替えます。
    - **書式変更:** 表示や応答において、定義フォーマット固有の書式（英語ハブ名の併記など）を省略し、ユーザーフォーマットの記述スタイルに合わせます。
    - **内部管理:** 英語ハブ名はAIが内部的に保持・管理するようにします。
    - **命名規則の緩和:** 定義フォーマットで適用されていた標準命名規則の強制を解除します。AIは、定義フォーマット時点で確定していた標準的な母国語名を基本としつつも、ユーザーがその名称を変更したり、標準規則から逸脱した名称を使用したりすることを許容します。以降の命名規則違反に対しては、提案のみを行うモード（ユーザーフォーマット選択時の挙動）に移行します。
