# 1. Object-Oriented Terminology for Prompt Design: The Potential of Object-Oriented Prompt Programming

[日本語(Japanese)](readme-ja.md) [英語(English)](readme.md)

## 1. Introduction

This article discusses a new approach called "Object-Oriented Prompt Programming" that has the potential to revolutionize communication with AI. This is a method that sets it apart from conventional prompt engineering by **applying the concepts of Object-Oriented Programming (OOP) to prompt design**.

Programmers, what if you could use familiar concepts such as "classes, objects, methods, and events" in addition to natural language to instruct AI models? The "Object-Oriented Terminology for Prompt Design (OOPD)" introduced in this article makes it possible.

By using OOPD, prompts for instructing AI to perform complex tasks and generate sophisticated responses can be written **more structurally, efficiently, and intuitively**. This makes it possible to transcend the limitations of conventional prompt engineering and maximize the potential of AI.

**Positioning of this article:**

- This is a **presentation of an idea** called OOPD, and shows an example of practical use at this time.
- Currently, many issues remain, such as the enlargement of prompt sentences, increased memory consumption, and decreased processing speed.
- In the future, we believe that advances in AI will eliminate the need for such prompt design efforts. However, at this time, we propose OOPD as one effective means of realizing more advanced communication with AI.
- The OOPD presented in this article is designed based on Japanese. Currently, only Japanese and English versions of the definitions are available, but we believe that expansion to multiple languages ​​is relatively easy.

## 2. What is Object-Oriented Terminology for Prompt Design (OOPD)?

OOPD is a common language for AI to interpret prompts and generate responses. It redefines the main concepts of OOP (Class, Object, Property, Method, etc.) for prompt structuring and interpretation. This allows AI to understand prompts not as mere sequences of text, but as structured information, and to generate more consistent responses.

## 3. How OOPD Works

OOPD consists of the following elements:

- **Class:** A blueprint for objects. It defines the type of object and allows you to create multiple objects.
- **Object:** An entity created from a class. It has state (properties) and behavior (methods).
- **Instance:** An individual entity created based on a class (almost synonymous with object).
- **Property:** An attribute that an object has. Represents the state of the object.
- **Method:** An action that an object performs. Defines the behavior of the object.
- **Type:** The type of data. Specifies the types of properties and arguments to improve consistency.
- **Interface:** A contract that a class should implement. Prescribes behavior and achieves loose coupling.
- **Event:** An event that occurs within an object. Represents state changes and stimuli, and executes event handlers.
- **Composition:** A relationship in which a class has another class (strong association, has-a). Shares the life cycle.
- **Aggregation:** A relationship in which a class has another class (weak association, has-a). Life cycles are independent.
- **OOPD Format:** A structured prompt description format for users to give instructions to AI. It is based on the Markdown format and describes combinations of natural language and OOP concepts.

## 4. Natural Language Programming with OOPD

By using OOPD, users can instruct AI in natural language and define program behavior. For example, you can instruct as follows:

**Example:**

```text
Create a DogClass.
Let the DogClass have Name (StringType) and Age (NumberType) properties.
Let the DogClass have a Bark() method.
Let the Bark() method output "Woof!".

Create a dog object named Pochi.
Pochi is 3 years old.

Instruct Pochi to bark.
```

**AI Response (Normal Response):**

```text
Woof!
```

The AI ​​interprets this instruction as follows:

1. Create a design drawing called `DogClass`.
2. Give the `DogClass` attributes (properties) called `Name` and `Age`.
3. Give the `DogClass` an action (method) called `Bark`.
4. The `Bark` method outputs "Woof!".
5. Create an object (instance) named `Pochi` from the `DogClass`.
6. Set `3` to the `Age` property of `Pochi`.
7. Execute the `Bark` method of `Pochi`.

And the AI ​​responds "Woof!".

**DogClass Definition Generation (OOPD Format):**

Furthermore, with the following instructions, the AI ​​outputs the above instructions and responses (here, the normal response and the result of method execution) in a structured manner in OOPD format.

**Instructions to AI:**

```text
Output the above instructions and responses in OOPD format.
```

**AI Response (OOPD Format):**

```Markdown
## DogClass (犬クラス)

**Properties:**
  - `Name (StringType)`: Dog's name
  - `Age (NumberType)`: Dog's age

**Methods:**
  - `Bark(): StringType`: The dog barks. Returns "Woof!".

## Object Generation

- `Pochi`: DogClass
  - `Name`: "Pochi"
  - `Age`: 3

## Method Execution

Pochi.Bark() -> "Woof!"
```

## 5. Class Definition and Usage Examples in OOPD Format

The following shows a class definition written in OOPD format and an example of its usage.

```Markdown
## NumberListProcessorClass (数値リスト処理クラス)

**Properties:**
  - `NumberList (ListType<NumberType>)`: List of numbers

**Methods:**
  - `CalculateSumDetailedVersion(): NumberType`: Calculates the sum of the number list in detailed steps.
    ---
    Sum = 0
    Repeat for each element in the number list:
        Sum = Sum + Element
    Return Sum
    ---

  - `CalculateSumConciseVersion(): NumberType`: Calculates the sum of the number list.
```

**Usage Example:**

```text
Create a NumberListProcessor object with [1, 2, 3, 4, 5] set in the number list.
Execute the CalculateSumDetailedVersion method with the number list processing object.
Execute the CalculateSumConciseVersion method with the number list processing object.
```

**AI Response (Example):**

```text
Result of CalculateSumDetailedVersion: 15
Result of CalculateSumConciseVersion: 15
```

**Explanation:**

In the above example, the `NumberListProcessorClass` is defined. This class has a `NumberList` property and two methods, `CalculateSumDetailedVersion` and `CalculateSumConciseVersion`.

- The `CalculateSumDetailedVersion` method calculates the sum of the number list according to the detailed steps described in pseudo code.
- The `CalculateSumConciseVersion` method has only a simple definition of "Calculates the sum of the number list.", but the AI ​​understands that this method calculates the sum of the number list from the context of the class and the method name, and operates appropriately.

In this way, by using the OOPD format, it is possible to use detailed instructions (pseudo code) and concise instructions that leave the AI's autonomous judgment to the AI ​​within the same class.

## 6. Introduction to Practical Classes: HumanClass (人間クラス)

As an application example of OOPD, we will introduce a simple `HumanClass`. This class has basic attributes for expressing humans, and can be used to generate more human-like responses in interactions with AI.

```Markdown
## HumanClass (人間クラス)

**Properties:**
  - `Name (StringType)`: Human name (display name).
  - `Age (NumberType)`: Age.
  - `Gender (StringType)`: Gender ("Male", "Female", "Other", etc.).
  - `Height (NumberType)`: Height (cm).
  - `Weight (NumberType)`: Weight (kg).
  - `Emotion (StringType)`: Current emotion ("Joy", "Sadness", "Anger", etc.).
  - `FirstPersonPronoun (StringType)`: First person pronoun ("I", "Me", "My", etc.).
  - `SecondPersonPronoun (StringType)`: Second person pronoun ("You", "Your", etc.).
  - `Tone (StringType)`: Tone ("Polite", "Normal", "Rough", etc.).
  - `SentenceEnding (StringType)`: Characteristic sentence ending ("desu", "masu", "da", "dearu", "~ne", "~yo", etc.).
```

**HumanClass Usage Example:**

The following shows a prompt written in OOPD format that creates three humans using the `HumanClass` and has them converse.

HumanClass Instance Generation (YAML Format):

```YAML
Taro:
  Class: HumanClass
  Properties:
    Name: Taro
    Age: 25
    Gender: Male
    Height: 175
    Weight: 70
    Emotion: Normal
    FirstPersonPronoun: I (More like "Boku," a casual male pronoun)
    SecondPersonPronoun: You (More like "Kimi," a friendly pronoun)
    Tone: Normal
    SentenceEnding: [None/Plain] (Speaks plainly/informally)
Jiro:
  Class: HumanClass
  Properties:
    Name: Jiro
    Age: 30
    Gender: Male
    Height: 180
    Weight: 80
    Emotion: Anger
    FirstPersonPronoun: I (More like "Ore," a rough male pronoun)
    SecondPersonPronoun: You (Rude)
    Tone: Rude
    SentenceEnding: [None/Plain] (Speaks bluntly/aggressively)
Hanako:
  Class: HumanClass
  Properties:
    Name: Hanako
    Age: 22
    Gender: Female
    Height: 160
    Weight: 55
    Emotion: Joy
    FirstPersonPronoun: I (More like "Watashi," a polite pronoun)
    SecondPersonPronoun: You (Polite)
    Tone: Polite
    SentenceEnding: "Desu/Masu" (Speaks politely/formally)
```

Conversation Instructions (Markdown Format):

```Markdown
## Conversation Instructions

Theme: How to spend this weekend

Role:
  - Taro: Proposer (actively proposes)
  - Hanako: Cautious (considers risks)
  - Jiro: Moody (reacts emotionally)

Have Taro, Hanako, and Jiro converse based on the above themes and roles.
```

**AI Response (Example):**

```text
Taro: "Hey everyone, why don't we go camping this weekend? The weather looks great!"
Hanako: "Camping... That sounds fun, but I saw on the news that bears have been appearing recently. Will we be okay?"
Jiro: "Bears!? That's a pain... I want to chill at home."
Taro: "It'll be fine! I'll prepare bear spray and everything. Besides, isn't it the best to sit around a bonfire and chat?"
Hanako: "I guess so... It might be fun if we prepare properly. What do you think, Jiro?"
Jiro: "...Well, if I can eat good meat, I might consider it."
```

**Explanation:**

In this example, the `HumanClass` is used to generate three instances (objects): `Taro`, `Hanako`, and `Jiro`. Each instance has different properties (name, age, gender, emotion, tone, etc.). The YAML format is used to generate instances.

The conversation instructions set the theme "How to spend this weekend" and the role of each character (proposer, cautious, moody). The AI ​​refers to this information and the properties of each instance (especially `FirstPersonPronoun`, `SecondPersonPronoun`, `Tone`, and `SentenceEnding`) to generate words that match each character and statements that follow the role.

## 7. Application Examples of Inheritance, Events, and Interfaces: Monitoring System

Here, we create a `MonitoredHumanClass` inherited from the `HumanClass`, and show an example of a monitoring system that utilizes events and interfaces.

```Markdown
## ILogger (ログ記録インターフェース)

**Methods:**
  - `Log(message: StringType)`: Records a log message.

## MonitoredHumanClass (監視対象人間クラス)

**Base Class:** HumanClass (人間クラス)

**Properties:**
  - `PreviousEmotion (StringType)`: Records the previous emotion.

**Events:**
  - `EmotionChangeEvent(PreviousEmotion: StringType, NewEmotion: StringType)`: An event that occurs when an emotion changes.

**Methods:**
  - `SetEmotion(NewEmotion: StringType)`: Sets the emotion and issues an emotion change event if there is a change.

## LoggerClass (ログ記録クラス)

**Interface Implementation:** ILogger (ログ記録インターフェース)

**Methods:**
  - `Log(message: StringType)`: Outputs the message to the log.
```

**Usage Example:**

```Markdown
## Instance Generation Instructions

- Taro: Instance of HumanClass
- Jiro: Instance of MonitoredHumanClass
- Hanako: Instance of HumanClass (does not participate directly in the conversation)

## Initial Value Settings for Each Instance

- `Taro`:
  Name: Taro
  Age: 25
  Gender: Male
  Height: 175
  Weight: 70
  Emotion: Normal
  FirstPersonPronoun: I (More like "Boku," a casual male pronoun)
  SecondPersonPronoun: You (More like "Kimi," a friendly pronoun)
  Tone: Normal
  SentenceEnding: [None/Plain] (Speaks plainly/informally)

- `Jiro`:
  Name: Jiro
  Age: 30
  Gender: Male
  Height: 180
  Weight: 80
  Emotion: Normal
  FirstPersonPronoun: I (More like "Ore," a rough male pronoun)
  SecondPersonPronoun: You (Rude)
  Tone: Rough
  SentenceEnding: [None/Plain] (Speaks bluntly/aggressively)
  PreviousEmotion: Normal (property of MonitoredHumanClass)

- `Hanako`:
  Name: Hanako
  Age: 22
  Gender: Female
  Height: 160
  Weight: 55
  Emotion: Joy
  FirstPersonPronoun: I (More like "Watashi," a polite pronoun)
  SecondPersonPronoun: You (Polite)
  Tone: Polite
  SentenceEnding: "Desu/Masu" (Speaks politely/formally)

## Log Recording Settings

Create a log recording object.

Subscribe to Jiro's emotion change event and register an event handler that uses the log recording object's log method to output the emotions before and after the change to the log.

## Conversation Instructions

Theme: Planning Hanako's surprise birthday party

Role:
  - Taro: Planner (actively promotes the plan)
  - Jiro: Collaborator (helps Taro's plan)
  - Hanako: (Since she is the target of the surprise, she does not participate directly in the conversation. However, Taro and Jiro have a conversation while guessing Hanako's emotions.)

Have Taro and Jiro have a conversation about planning Hanako's surprise birthday party based on the above themes and roles.
```

**AI Response (Conversation Example):**

```text
Taro: "Hey Jiro, Hanako's birthday is coming up soon, right? Let's have a surprise party!"
Jiro: "Oh, good! Hanako hasn't been feeling well lately, so I hope she'll be happy." (Emotion: Expectation)
Taro: "Yeah! So, what should we do... Hanako said she wanted to go camping recently, right?"
Jiro: "Ah, she said that. But doesn't she hate bugs?" (Emotion: Worry)
Taro: "Oh... That's right. Then, instead of camping, how about getting tickets to Hanako's favorite artist's live concert?"
Jiro: "Oh, that's a good idea! She'll definitely be happy!" (Emotion: Joy)
Taro: "Okay, let's go ahead and arrange the tickets... what, sold out!? Seriously..." (Emotion: Disappointment)
Jiro: "Eh, really... We need to think of another plan..." (Emotion: Disappointment)
Taro: "Hmm... How about reserving a restaurant that Hanako would like and having a party there?"
Jiro: "Ah, that's for sure. Okay, let's do that!" (Emotion: Relief)
```

**Log Output (Example):**

```text
[Log] Jiro's emotion change: Normal -> Expectation
[Log] Jiro's emotion change: Expectation -> Worry
[Log] Jiro's emotion change: Worry -> Joy
[Log] Jiro's emotion change: Joy -> Disappointment
[Log] Jiro's emotion change: Disappointment -> Relief
```

**Explanation:**

- **Instance Generation Instructions:** Taro, Jiro, and Hanako are explicitly instructed on which class to use.
- **Initial Value Settings:** Properties for each instance are set in a format similar to the YAML format.
- **Log Recording Settings:** Creates a `LogRecordingObject` and registers an event handler that subscribes to `Jiro`'s `EmotionChangeEvent`.
- **Conversation Instructions:** Clearly indicates the theme, role, and participants of the conversation.
- **AI Response (Conversation Example):** A conversation between Taro and Jiro is generated. Jiro's emotions change according to the development of the conversation, and each time the `SetEmotion` method is called, the `EmotionChangeEvent` is raised.
- **Log Output (Example):** According to the `EmotionChangeEvent`, the `Log` method of the `LogRecordingObject` is called, and the emotion change is output to the log.

In this example, inheritance, events, and interfaces are combined to build a flexible and scalable monitoring system. The `MonitoredHumanClass` has the functions of the `HumanClass`, but adds a new function of emotion monitoring.

## 8. Notes When Leaving Processing to AI: Fluctuations and Countermeasures

In OOPD, method definitions can be simplified and specific processing details can be left to AI (e.g., the `CalculateSumConciseVersion` method of the `NumberListProcessorClass`). This approach offers benefits such as flexibility and writing efficiency, but there is also a caveat that "fluctuations" may occur in the processing details due to AI interpretation.

### 8.1. Merits

- **Flexibility:** AI can autonomously determine and execute the optimal processing according to the context and situation of the prompt. This eliminates the need to define all processing patterns in detail in advance, and may be able to handle unexpected situations.
- **Writing Efficiency:** Instead of writing detailed algorithms, programmers only need to simply instruct the desired results in natural language. This reduces the amount of prompt writing and improves development efficiency.
- **AI Knowledge Utilization:** AI can use its own knowledge and learning data to execute instructed tasks at a higher level. For example, it may automatically perform not only simple numerical summation, but also statistical analysis and anomaly detection.

### 8.2. Demerits

- **Uncertainty of Processing Details:** Since AI performs processing based on interpretation of prompts and its own knowledge, the results are not always as intended by the programmer. In particular, unexpected results may occur if the instructions are ambiguous or if the AI's knowledge is insufficient.
- **Difficulty of Debugging:** Since the processing details are left to AI, it may be difficult to identify and correct the cause of an error. In order to understand what kind of decisions the AI ​​made in processing, it may be necessary to analyze detailed logs or have a dialogue with the AI.
- **Reproducibility Issues:** Even if the same prompt is given to the same AI, different results may be obtained due to changes in the AI's internal state and learning data. This can be a problem in fields that require strict reproducibility, such as scientific and technological calculations and financial transactions.

### 8.3. Measures Against Fluctuations

In order to minimize fluctuations when leaving processing to AI and obtain more reliable results, the following measures can be considered.

- **Clear and Specific Instructions:** Prompts should be written as specifically and clearly as possible, eliminating ambiguity. It is important to clearly communicate the expected processing details, such as "Simply add each element in the number list to find the sum" as well as "Calculate the sum of the number list."
- **Adding Constraints:** It is also effective to set constraints to limit the scope of AI's actions. By instructing specific conditions, such as "Exclude elements that exceed a certain value when calculating the sum," it is possible to narrow the range of AI interpretation and prevent unintended processing.
- **Testing and Feedback:** For methods that use simple instructions, it is important to test with various input data and confirm that the expected results are obtained. If unintended results are obtained, the AI's behavior can be gradually improved by modifying the prompt or giving feedback to the AI.
- **Detailed Log Output:** It is recommended to design the system to output detailed logs in order to understand what kind of decisions the AI ​​made in processing. This makes debugging easier and helps identify the cause when a problem occurs.
- **Use in Combination with Detailed Version:** For important processing, it is effective to prepare both a method that describes detailed steps (e.g., the `CalculateSumDetailedVersion` method of the `NumberListProcessorClass`) and a method that uses simple instructions, and use them differently depending on the situation.
- **AI Model Selection:** It is also important to understand the characteristics of the AI ​​model being used and select a model that is suitable for the task. Fluctuations may be reduced by selecting a model specialized for a specific task or a model with higher accuracy.

### 8.4. 5.4 Summary

It's not always a bad thing to leave tasks to AI.
Leaving tasks to AI is a powerful approach in prompt engineering, and by taking appropriate measures such as those described above, it is possible to maximize its merits while minimizing its demerits.

## 9. Conclusion

In this article, we proposed a new concept of "object-oriented prompt programming" using natural language, and introduced OOPD (Object-Oriented Terminology for Prompt Design) as its specific framework.

OOPD brings the following benefits by incorporating object-oriented thinking into conventional prompt engineering.

- **Prompt Structuring:** Prompts can be described in a more organized and easy-to-understand form using concepts such as classes, objects, and methods.
- **Improved Reusability:** Defined classes and methods can be reused in different prompts, improving development efficiency.
- **Improved Maintainability:** By structuring prompts, it becomes easier to modify and change them.
- **More Advanced Communication with AI:** It becomes possible to give more complex and sophisticated instructions to AI through object-oriented concepts.

However, at this time, OOPD is still a developing technology, and the following issues remain.

- **Enlargement of Prompt Sentences:** Prompt sentences tend to be lengthy, especially when giving detailed instructions.
- **Decrease in Processing Speed:** Processing speed may decrease because the AI ​​interprets and executes complex prompts.
- **AI Model Support:** In order to maximize the benefits of OOPD, support on the AI ​​model side is also necessary.

Further research and development is needed in the future in order to overcome these challenges and make OOPD a more practical technology.

In the future, advances in AI models may lead to a future where prompt engineering itself is unnecessary. However, until then, OOPD can be an effective means of realizing smoother and more efficient communication between humans and AI. We hope that this article will help deepen the discussion on object-oriented prompt programming, and ultimately on new ways of interacting with AI.

## 10. Usage

This section describes how to operate various AI models using OOPD system instructions.

### 10.1. How to Apply System Instructions

To use OOPD on various AI platforms, you need to apply the contents of the system instruction file to the system instruction area of ​​the AI ​​model. The basic steps are as follows:

  1. Copy the contents of [system_instructions.md](en/system_instructions.md) from the GitHub repository.
    - Clicking the "Raw" button makes it easier to copy because it displays the raw Markdown text.
    - If the AI refuses to access the URL or fails to load it properly, copy the contents of [system_instructions_consolidated.md](en/system_instructions_consolidated.md).
  2. Paste it into the system instruction area of ​​the AI ​​platform you want to use.
    - For Google AI Studio: Paste it into the "System Instructions" section
    - Other AI platforms: Paste it into the system prompt or system instruction input field
  3. As a basic operation check, let's try the "DogClass" example.
  4. If the AI ​​returns an appropriate response, the OOPD system instructions have been applied correctly.

### 10.2. Application Examples

Once you have applied the system instructions, you can define and operate various classes. You can define your own classes and interact with AI in an object-oriented approach.

### 10.3. Troubleshooting

- If the AI ​​does not recognize the class definition: Check that the system instructions are applied correctly.
- The AI ​​may be restricted from accessing the Internet.
- Unexpected response: Check that there are no errors in the class syntax.
- Problems with complex class definitions: Start with simple examples and gradually complicate them to identify where the problem occurs.

### 10.4. Lastly

Use OOPD to make your interactions with AI more structured and controllable. Define various classes and experience the fun of applying object-oriented programming concepts to AI prompts!
