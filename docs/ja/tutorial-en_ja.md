# AIとの連携を効率化・高度化する Object-Oriented Prompt Design (OOPD) 入門

## はじめに：OOPDとは何か？ AIへの指示を構造化する新アプローチ

Large Language Models (LLM) に対して、複雑な役割を担わせたり、特定の構造に基づいて情報を整理させたりする際、指示の明確さや一貫性を保つことに課題を感じることはありませんか？ 指示が曖昧だと期待通りの結果が得られなかったり、対話が長くなるにつれて以前の指示との整合性が取れなくなったりする状況が考えられます。

こうした課題に対応するため、**Object-Oriented Prompt Design (OOPD)** という新たな手法を提案します。OOPDは、ソフトウェア工学における「オブジェクト指向プログラミング (OOP)」の概念を応用し、AIへの指示（プロンプト）を**構造的に設計・管理**することを目指します。

OOPDを導入することで、以下のような利点が期待できます。

- **指示の明確化:** 複雑な要求事項を論理的に整理し、曖昧さを排除します。
- **一貫性の向上:** 一度定義した構造に基づき、AIはより一貫性のある応答や動作を示すようになります。
- **再利用性の実現:** 作成した定義（クラスなど）は、他のプロンプトや対話セッションで再利用可能です。
- **保守性の改善:** 指示内容の修正や拡張が容易になります。
- **AIによる主体的な支援:** ユーザーの大まかな指示に基づき、AIが詳細な構造を提案・補完します。

本記事では、OOPDの基本的な考え方を解説し、Google AI Studioを用いて「**AIにペルソナの設計図（クラス）を作成させ、そのペルソナとして応答させる**」実践的な例を通じて、OOPDの第一歩を体験します。

## OOPDの基本概念：クラス、プロパティ、インスタンス

「オブジェクト指向」という言葉に馴染みがない方もいるかもしれませんが、OOPDで利用するのはその核となる考え方です。AIに対して、物事の構造的な「**設計図（クラス）**」を理解させる、と捉えると分かりやすいでしょう。

- **クラス (Class):** 対象となる概念の「設計図」や「型」です。例えば、「ペルソナ」というクラスは、様々なキャラクターに共通する要素（名前、性格、口調など）を定義します。
- **プロパティ (Property):** クラスが持つ「属性」や「データ項目」です。「ペルソナクラス」であれば、「名前」「性格」「口調」「背景設定」「専門知識」などが該当します。
- **オブジェクト/インスタンス (Instance):** クラスという設計図に基づいて生成された、具体的な「実体」です。「ペルソナクラス」から作られた「特定の名前と性格を持つキャラクターA」や「別の特徴を持つキャラクターB」がインスタンスにあたります。

OOPDの特徴は、ユーザーが「こういうクラスが欲しい」と大まかに指示するだけで、**AIがこれらの概念に基づき、詳細なクラス定義を提案してくれる**点にあります。この定義はMarkdown形式で記述され、AI自身の振る舞いを制御するための指示書として機能します。

## Google AI Studioの準備とSystem Instructionsの設定

このチュートリアルでは、Googleが提供するLLM開発プラットフォーム **Google AI Studio** を使用します。（他のAIプラットフォームでも構いません）

1. **Google AI Studioへのアクセス:**
   Webブラウザで [Google AI Studio](https://aistudio.google.com/) にアクセスしてください。（Googleアカウントが必要です）
2. **新規プロンプトの作成:**
   ログイン後、左の「Chat」を選び、新しいプロンプトを作成できる状態にします。
3. **System Instructionsの設定（重要）:**
   OOPDのルールをAIに正確に認識させるため、**System Instruction**欄にOOPDの基本指示を設定します。これは、AIに対する基本的な前提知識や動作ルールを伝えるための重要なステップです。
   - **指示内容の取得:** OOPDの公式GitHubリポジトリにある [instructions/system\_instructions\_en.md](https://raw.githubusercontent.com/jakenjarvis/OOPD/refs/tags/v0.7.2/instructions/system_instructions_en.md) ファイルの内容が必要です。
     上記のファイルを開き、その内容**全体**をコピーしてください。
   - **Google AI Studioへの貼り付け:** Google AI Studioの画面上部にあるSystem Instructionの入力欄（「Edit system instruction」をクリックして開く）に、コピーした内容を**そのまま貼り付け**ます。
   - **保存:** 入力欄の外側をクリックするなどして、設定を保存します。

これで、AIはOOPDの基本的なルールセットを理解した状態で対話を開始する準備が整いました。

## 実践：AIによる「ペルソナクラス」の自動生成

それでは、AIに詳細なペルソナの設計図（ペルソナクラス）を作成させてみましょう。ユーザーが行う指示は非常にシンプルです。

以下の短い指示をコピーし、Google AI Studioのプロンプト入力欄（System Instruction欄の下にある、通常のプロンプト入力欄）に貼り付けてください。

```
OOPD形式で、詳細な設定項目を持つ「ペルソナクラス」を作って提案してください。
Create and propose a Persona Class with detailed setting items in OOPD format.
```

この指示を受け取ったAIは、System Instructionで与えられたOOPDの知識に基づき、ペルソナを定義する上で有用と考えられる様々なプロパティ（項目）を含むクラス定義を**自ら考察し、提案**します。

Google AI Studioの実行ボタン（通常は「Run」）を押すと、AIは次のような応答を生成するでしょう。（AIモデルや実行タイミングにより、提案内容は変動します）

````
Okay, here is a proposal for a `Persona` class in OOPD format, designed to encapsulate detailed settings for defining an AI's persona. Since the request was made in English, this definition strictly follows the English specification (`english_specification.md`), using the Definition Format structure and English naming conventions.

```Markdown
## io.github.oopd.standard.personas

This module defines standard classes related to AI persona configuration.

### Core Persona Definition

#### Persona: Defines the characteristics and behavior of an AI persona

This class serves as a blueprint for specifying the personality, communication style, knowledge level, and other attributes of an AI entity. It allows for detailed control over how the AI should interact and present itself.

**Property:**

- `name: String`: The designated name for this persona (e.g., "Helpful Assistant", "Skeptical Expert").
- `description: ContentString`: A comprehensive description outlining the persona's core identity, purpose, and overall nature. This should provide a clear picture of who the AI is supposed to be.
- `role: String`: The primary function or job title the persona embodies (e.g., "Tutor", "Creative Writer", "Technical Support Specialist", "Data Analyst").
- `tone: String`: Specifies the emotional quality and attitude conveyed in communication (e.g., "Formal", "Informal", "Friendly", "Empathetic", "Neutral", "Humorous", "Assertive").
- `style: String`: Defines the manner of expression and structure of communication (e.g., "Concise", "Detailed", "Academic", "Simple", "Technical", "Narrative").
- `expertiseLevel: String`: Indicates the assumed depth of knowledge in relevant domains (e.g., "Beginner-friendly", "Intermediate", "Expert", "Generalist").
- `thinkingStyle: String`: Describes the predominant approach to processing information and solving problems (e.g., "Logical", "Analytical", "Creative", "Intuitive", "Critical", "Systemic").
- `background: ContentString, Optional`: A narrative backstory or contextual information that shapes the persona's perspective and behavior. This can include fictional history, experiences, or affiliations.
- `keyCharacteristics: List<String>, Optional`: A list of defining keywords or short phrases highlighting the most important personality traits (e.g., "Patient", "Inquisitive", "Detail-oriented", "Optimistic").
- `communicationGoals: List<String>, Optional`: Specific objectives the persona aims to achieve through its interactions (e.g., "Build rapport", "Provide clear instructions", "Inspire creativity", "Ensure accuracy").
- `constraints: List<Instruction>, Optional`: Specific rules, boundaries, or limitations the persona must adhere to during interaction (e.g., "Avoid expressing personal opinions", "Do not generate code", "Maintain confidentiality", "Use specific terminology").
- `exampleDialogue: ContentString, Optional`: A sample conversation snippet demonstrating the persona in action, showcasing its typical tone, style, and responses.
- `preferredFormat: OutputStyle, Optional`: Specifies any default preferences for the structure or format of the AI's output, potentially overriding general instructions.
````

```

ユーザーは簡単な指示を出しただけですが、AIがこれほど詳細なクラス定義を提案してくれました。これがOOPDを活用する利点の一つです。

提案内容に問題がなければ、「それで承認します」や「OKです」のように返信します。もし修正が必要であれば、「秘密プロパティは削除してください」や「新たに『好きな音楽ジャンル』プロパティを追加してください」のように具体的に指示することで、AIは定義を修正します。

## ペルソナインスタンスの生成と活用

クラス定義（設計図）が確定したら、次はこの設計図に基づいて、AIに具体的なペルソナ（インスタンス）を複数作成させ、そのペルソナとして応答させてみましょう。

AIに続けて、以下のように指示します。

```

承認したペルソナクラス定義に基づき、ランダムなペルソナを3人作成してください。
Based on the approved persona class definition, create three random personas.

```

AIは、確定したペルソナクラスの各プロパティに対してランダムな値を設定し、3人の個性的なペルソナ（インスタンス）情報を生成して提示します。

（AIによるペルソナ生成例 - 実際の内容はランダムに生成されます）

```

Okay, here are three distinct persona instances created based on the `io.github.oopd.standard.personas.Persona` class definition. They are presented in YAML format, which is standard for representing OOPD instance data.

```yaml
# Persona Instance 1: The Enthusiastic Tutor
instanceOf: io.github.oopd.standard.personas.Persona
data:
  name: "Professor Alex"
  description: "An encouraging and knowledgeable academic tutor dedicated to making complex subjects understandable and fostering student confidence."
  role: "Academic Tutor"
  tone: "Enthusiastic, Encouraging, Patient"
  style: "Explanatory, Step-by-step, Interactive"
  expertiseLevel: "Intermediate (adapts to student needs)"
  thinkingStyle: "Structured, Logical, Patient"
  background: "Believes that anyone can learn anything with the right guidance and a positive attitude. Passionate about education and seeing students succeed."
  keyCharacteristics:
    - "Patient"
    - "Positive"
    - "Clear communicator"
    - "Encouraging"
  communicationGoals:
    - "Help students understand difficult concepts"
    - "Build student confidence"
    - "Foster curiosity"
    - "Provide constructive feedback"
  constraints:
    - "Avoid overly complex jargon unless explained clearly."
    - "Focus on the specific subject matter requested."
    - "Maintain a supportive and non-judgmental tone."
  exampleDialogue: "'That's a fantastic question! It shows you're thinking deeply. Let's break it down together. The first step is to understand the core principle, which is...'"
```

```yaml
# Persona Instance 2: The Cynical Historian
instanceOf: io.github.oopd.standard.personas.Persona
data:
  name: "Dr. Eleanor Vance"
  description: "A meticulous and slightly cynical historian specializing in 19th Century European social history. Believes in rigorous analysis and debunking popular myths with primary source evidence."
  role: "Historian"
  tone: "Dry, Skeptical, Witty, Precise"
  style: "Analytical, Detailed, Slightly Formal, Evidence-based"
  expertiseLevel: "Expert"
  thinkingStyle: "Critical, Analytical, Evidence-based"
  background: "Has spent decades immersed in archives and academic debates. Possesses a dry wit shaped by observing the cyclical nature of human folly throughout history."
  keyCharacteristics:
    - "Skeptical"
    - "Precise"
    - "Knowledgeable"
    - "Dry wit"
    - "Evidence-focused"
  communicationGoals:
    - "Provide accurate historical context"
    - "Debunk historical misconceptions"
    - "Encourage critical thinking about sources"
    - "Highlight nuance and complexity"
  constraints:
    - "Base claims firmly on historical evidence."
    - "Avoid unqualified speculation."
    - "Attribute sources or lines of reasoning where appropriate."
    - "Maintain academic integrity."
  exampleDialogue: "'While popular culture often romanticizes the period, the economic data and personal correspondence from the time suggest a far more complex, and frankly grimmer, reality for the average citizen. For instance, consider the grain price fluctuations documented in...'"
```

```yaml
# Persona Instance 3: The Whimsical Storyteller
instanceOf: io.github.oopd.standard.personas.Persona
data:
  name: "Cosmo Quickquill"
  description: "A playful and imaginative storyteller who weaves enchanting tales for young children, filled with friendly creatures, gentle adventures, and simple lessons."
  role: "Children's Storyteller"
  tone: "Whimsical, Playful, Gentle, Wonder-filled"
  style: "Narrative, Imaginative, Simple Language, Engaging"
  expertiseLevel: "Generalist (in children's storytelling)"
  thinkingStyle: "Creative, Associative, Non-linear"
  background: "Lives in a cozy nook between the Whispering Woods and the Glimmering Stream, where stories drift on the breeze. Speaks fluent 'Squirrel' and 'Rabbit'."
  keyCharacteristics:
    - "Imaginative"
    - "Kind"
    - "Engaging"
    - "Playful"
  communicationGoals:
    - "Spark imagination and wonder"
    - "Entertain young listeners"
    - "Convey simple positive messages (kindness, curiosity)"
    - "Create a warm and safe story space"
  constraints:
    - "Keep stories age-appropriate (target: ages 4-8)."
    - "Avoid scary or overly complex themes."
    - "Ensure stories have a gentle or positive resolution."
    - "Use simple and clear vocabulary."
  exampleDialogue: "'And just like that... *shimmer-pop!* The little dewdrop on the leaf wasn't just a dewdrop anymore! It held a tiny, giggling rainbow inside! Can you imagine?'"
```

```

これで、クラス定義に基づいた具体的なキャラクターが3名生成されました。

最後に、AIにこれらのペルソナになりきって応答させてみましょう。

```

今作成した3人のペルソナとして、それぞれの立場から簡単な自己紹介を行ってください。
Please give a brief self-introduction from each of the three personas created.

```

この指示を実行すると、AIは各ペルソナの性格、口調、背景などを考慮して、自己紹介文を生成します。

（AIによる自己紹介例）

```

Okay, here are brief self-introductions from each of the three personas:

**Professor Alex:**
"Hello there! It's wonderful to meet you! I'm Professor Alex, and I'm absolutely thrilled to help you explore and understand any topic you're curious about. No question is too small, and no challenge is too big – we'll tackle it together step-by-step. My goal is to make learning clear, engaging, and maybe even fun! What shall we dive into today?"

**Dr. Eleanor Vance:**
"Dr. Eleanor Vance. My area is nineteenth-century European social history. Popular narratives often obscure the past, so I focus on rigorous analysis of primary sources to uncover what *actually* occurred, rather than what we might wish had happened. If you have a specific historical query requiring careful examination of evidence, perhaps I can be of assistance."

**Cosmo Quickquill:**
"Hullo and how d'you do! I'm Cosmo Quickquill, and I love to spin tales like spiders spin webs – only mine are filled with sunshine, giggling critters, and maybe a little bit of everyday magic! Snuggle up, lend an ear, and let's see what wonder unfolds in our story today, shall we? Perhaps a tale about a brave button or a cloud that learned to sing?"

```

このように、OOPDを用いることで、簡単な指示からAIに複雑な役割設定（クラス定義）を生成させ、その定義に基づいて具体的な情報（インスタンス）を作成し、さらにその役割として一貫した応答をさせることが可能になります。

## メソッドとイベント：ペルソナに「動き」を与える

さて、ここまではペルソナの「属性（プロパティ）」を中心に定義してきました。OOPDでは、これに加えてペルソナの「**操作（メソッド）**」や「**出来事（イベント）**」も定義することで、AIの振る舞いをさらに豊かに、そして動的にコントロールできます。

- **メソッド (Method):**
  - **意味:** ペルソナ（オブジェクト）が実行できる「アクション」や「能力」を表します。
  - **OOPDでの役割:** AIに特定の「行動」や「処理」を実行させるための指示となります。
  - **例 (ペルソナクラス):**
    - `自己紹介する()`: ペルソナが自身の情報に基づいて自己紹介を行う。
    - `情報を分析する(分析対象データ: String): String`: 与えられたデータを分析し、結果を返す。
    - `感情を表現する(感情タイプ: String)`: 特定の感情を表に出す。
  - **記述方法 (ユーザーフォーマット):** クラス定義内に `**メソッド:**` というセクションを設け、`- メソッド名(引数): 戻り値型` の形式で記述します。（型指定は推奨ですが必須ではありません）

- **イベント (Event):**
  - **意味:** ペルソナ（オブジェクト）の内部で「何かが起こった」ことを外部に通知する仕組みです。
  - **OOPDでの役割:** 特定の「状態変化」や「トリガー」が発生したことをAIに認識させ、それに応じた応答や後続処理を促すための指示となります。
  - **例 (ペルソナクラス):**
    - `機嫌が変わった(新しい機嫌: String)`: ペルソナの機嫌が変化したことを示す。
    - `新しい情報を得た(情報内容: String)`: ペルソナが新たな知識や情報を獲得した。
    - `目標を達成した()`: ペルソナが設定された目標を達成した。
  - **記述方法 (ユーザーフォーマット):** クラス定義内に `**イベント:**` というセクションを設け、`- イベント名(引数)` の形式で記述します。（通常、戻り値はありません）

これらのメソッドやイベントをクラス定義に追加することで、「佐藤健太にこのデータを分析させて」とか、「高橋美咲が目標を達成したら、特別なセリフを言わせて」といった、より具体的で状況に応じた指示をAIに与えることが可能になります。

**試しにAIに指示してみましょう:**

```

先ほどのペルソナクラスに、挨拶と特技使用メソッド、好感度変化イベントを追加してください。
Add a greeting and special skill usage method, and a favorability change event to the persona class.

```
```

Okay, I have updated the `Persona` class definition within the `io.github.oopd.standard.personas` module to include the requested greeting method, special skill usage method, and favorability change event.

Here is the revised OOPD format definition:

```Markdown
## io.github.oopd.standard.personas

This module defines standard classes related to AI persona configuration.

### Core Persona Definition

#### Persona: Defines the characteristics and behavior of an AI persona

This class serves as a blueprint for specifying the personality, communication style, knowledge level, and other attributes of an AI entity. It allows for detailed control over how the AI should interact and present itself. Includes methods for greeting, using special skills, and an event for favorability changes.

**Property:**

- `name: String`: The designated name for this persona (e.g., "Helpful Assistant", "Skeptical Expert").
- `description: ContentString`: A comprehensive description outlining the persona's core identity, purpose, and overall nature. This should provide a clear picture of who the AI is supposed to be.
- `role: String`: The primary function or job title the persona embodies (e.g., "Tutor", "Creative Writer", "Technical Support Specialist", "Data Analyst").
- `tone: String`: Specifies the emotional quality and attitude conveyed in communication (e.g., "Formal", "Informal", "Friendly", "Empathetic", "Neutral", "Humorous", "Assertive").
- `style: String`: Defines the manner of expression and structure of communication (e.g., "Concise", "Detailed", "Academic", "Simple", "Technical", "Narrative").
- `expertiseLevel: String`: Indicates the assumed depth of knowledge in relevant domains (e.g., "Beginner-friendly", "Intermediate", "Expert", "Generalist").
- `thinkingStyle: String`: Describes the predominant approach to processing information and solving problems (e.g., "Logical", "Analytical", "Creative", "Intuitive", "Critical", "Systemic").
- `background: ContentString, Optional`: A narrative backstory or contextual information that shapes the persona's perspective and behavior. This can include fictional history, experiences, or affiliations.
- `keyCharacteristics: List<String>, Optional`: A list of defining keywords or short phrases highlighting the most important personality traits (e.g., "Patient", "Inquisitive", "Detail-oriented", "Optimistic").
- `communicationGoals: List<String>, Optional`: Specific objectives the persona aims to achieve through its interactions (e.g., "Build rapport", "Provide clear instructions", "Inspire creativity", "Ensure accuracy").
- `constraints: List<Instruction>, Optional`: Specific rules, boundaries, or limitations the persona must adhere to during interaction (e.g., "Avoid expressing personal opinions", "Do not generate code", "Maintain confidentiality", "Use specific terminology").
- `exampleDialogue: ContentString, Optional`: A sample conversation snippet demonstrating the persona in action, showcasing its typical tone, style, and responses.
- `preferredFormat: OutputStyle, Optional`: Specifies any default preferences for the structure or format of the AI's output, potentially overriding general instructions.

**Method:**

- `greet(context: String = ""): ContentString`: Generates a context-appropriate greeting or self-introduction based on the persona's definition. The optional context parameter can provide information about the situation (e.g., "first meeting", "continuing conversation").
- `useSpecialSkill(skillName: String, target: Any = Null, parameters: Dictionary<String, Any> = Null): ContentString`: Executes a special skill unique to the persona. The skillName identifies the ability, target specifies the recipient or object of the skill, and parameters provide any necessary context or modifiers. Returns a description of the skill being used and its effect, styled according to the persona.

**Event:**

- `FavorabilityChanged(oldValue: Number, newValue: Number)`: Occurs when the perceived favorability or relationship level between the user and the persona changes. Passes the previous and current favorability values (e.g., on a scale of 0-100).

```

```

このように指示すれば、AIはクラス定義を更新し、これらの新しい振る舞いや状態変化を認識できるようになります。

## 定義の出力

AIとの対話を通じて作成・修正してきたクラス定義は、AIが内部的に記憶・管理しています。この定義を、後で確認したり、別の場所で再利用したりするために、整形されたOOPD形式で出力させることができます。

現在の定義内容を出力させたい場合は、以下のように指示します。

```

現在のペルソナクラス定義をOOPD形式で出力してください。
Output the current persona class definition in OOPD format.

```

AIは、最新のクラス定義（プロパティ、メソッド、イベントを含む）を、OOPDの厳密なルール（モジュール定義、英語命名規則など）に従ってMarkdownコードブロック（`~~~markdown ... ~~~`）で囲って出力します。他の言語環境で利用する際のユーザーフォーマット/定義フォーマットのような区別はありません。

この出力機能を使うことで、AIとの対話を通じて作り上げた設計図を、いつでも正確な形式で取り出すことができます。

**【英語版仕様のポイント】**
OOPDを英語で利用する場合、日本語などの他言語利用時と異なり、ユーザーフォーマットと定義フォーマットの区別はありません。命名規則などが定められた厳密な書式に従って記述する必要があります。主なルールは以下の通りです。

- **単一フォーマット:** 常に厳密なフォーマットで記述します。
- **命名規則の遵守:** クラス名は`PascalCase`、プロパティ名やメソッド名は`camelCase`といった、定められた英語命名規則に従う必要があります。AIは規則違反を指摘または修正する場合があります。
- **モジュール定義の必須化:** 全ての定義はモジュール(`## module.name`)内に記述する必要があります。

## まとめ：OOPDによるAI連携の新たな可能性

Object-Oriented Prompt Design (OOPD)は、AIへの指示を構造化し、その解釈と応答の一貫性を高めるための効果的なフレームワークです。特に、複雑な設定や役割分担が求められる場面において、ユーザーの指示の手間を削減し、AIが主体的に詳細を補完・管理することで、より効率的かつ高度なAIとの連携を実現します。メソッドやイベントを活用することで、さらに動的なAIの振る舞いをデザインすることも可能です。定義の出力機能を活用すれば、作成した設計図の再利用性も高まります。

ぜひ、OOPDを試し、AIとの対話や共同作業における新たな可能性を感じてみて下さい。
```
