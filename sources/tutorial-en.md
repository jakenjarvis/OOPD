# Introduction to Object-Oriented Prompt Design (OOPD): Streamlining and Enhancing AI Collaboration

## Introduction: What is OOPD? A New Approach to Structuring AI Instructions

When asking Large Language Models (LLMs) to take on complex roles or organize information based on specific structures, have you ever struggled to maintain clarity and consistency in your instructions? Ambiguous instructions can lead to unexpected results, and as conversations lengthen, inconsistencies with previous instructions might arise.

To address these challenges, we propose a new method called **Object-Oriented Prompt Design (OOPD)**. OOPD applies concepts from "Object-Oriented Programming (OOP)" in software engineering, aiming to **structurally design and manage** instructions (prompts) given to AI.

By introducing OOPD, the following benefits can be expected:

- **Clarification of Instructions:** Logically organizes complex requirements and eliminates ambiguity.
- **Improved Consistency:** Based on a once-defined structure, the AI will exhibit more consistent responses and behaviors.
- **Realization of Reusability:** Created definitions (like classes) can be reused in other prompts or conversation sessions.
- **Enhanced Maintainability:** Modifying or extending instruction content becomes easier.
- **Proactive AI Assistance:** Based on the user's high-level instructions, the AI suggests and complements detailed structures.

This article explains the basic concepts of OOPD and provides a hands-on experience of the first steps through a practical example using Google AI Studio: "**Having the AI create a design document (class) for a persona and respond as that persona**."

## Basic Concepts of OOPD: Class, Property, Instance

Even if you're unfamiliar with the term "object-oriented," OOPD utilizes its core ideas. It's helpful to think of it as making the AI understand the structural "**design document (Class)**" of things.

- **Class:** The "design document" or "type" of the concept being targeted. For example, a `Persona` class defines common elements for various characters (name, personality, tone, etc.).
- **Property:** The "attributes" or "data items" that a class possesses. For the `Persona` class, this would include "Name," "Personality," "Tone," "Background Setting," "Expertise," etc.
- **Object/Instance:** Concrete "entities" generated based on the class design document. "Character A with a specific name and personality" or "Character B with different characteristics," created from the `Persona` class, are instances.

A key feature of OOPD is that simply by giving a high-level instruction like "I want a class like this," the **AI suggests a detailed class definition based on these concepts**. This definition is written in Markdown format and functions as an instruction manual to control the AI's own behavior.

## Preparing Google AI Studio and Setting System Instructions

This tutorial uses **Google AI Studio**, an LLM development platform provided by Google. (Other AI platforms can also be used).

1. **Accessing Google AI Studio:**
   Access [Google AI Studio](https://aistudio.google.com/) in your web browser. (A Google account is required).
2. **Creating a New Prompt:**
   After logging in, select "Chat" on the left to prepare for creating a new prompt.
3. **Setting System Instructions (Important):**
   To ensure the AI accurately recognizes the OOPD rules, set the basic OOPD instructions in the **System Instruction** field. This is a crucial step to convey the fundamental prerequisite knowledge and operational rules to the AI.
   - **Obtaining Instruction Content:** You need the content of the [instructions/system\_instructions\_en.md](https://raw.githubusercontent.com/jakenjarvis/OOPD/refs/tags/v0.7.2/instructions/system_instructions_en.md) file from the official OOPD GitHub repository.
     Open the file above and copy its **entire** content.
   - **Pasting into Google AI Studio:** Paste the copied content **directly** into the System Instruction input field in Google AI Studio (click "Edit system instruction" to open).
   - **Saving:** Save the settings, for instance, by clicking outside the input field.

Now, the AI is ready to start the conversation with an understanding of the basic OOPD rule set.

## Practice: Auto-Generating a "Persona Class" with AI

Let's have the AI create a detailed design document (Persona class). The instruction from the user is very simple.

Copy the short instruction below and paste it into the prompt input field in Google AI Studio (the regular prompt input field below the System Instruction field).

```
Create and propose a Persona Class with detailed setting items in OOPD format.
```

Upon receiving this instruction, the AI, based on the OOPD knowledge provided in the System Instruction, will **consider and propose** a class definition containing various properties (items) deemed useful for defining a persona.

Pressing the execution button in Google AI Studio (usually "Run"), the AI will generate a response similar to the following. (The proposed content may vary depending on the AI model and execution time).

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

Although the user gave only a simple instruction, the AI proposed such a detailed class definition. This is one of the advantages of using OOPD.

If the proposal is acceptable, reply with something like "I approve" or "Okay." If modifications are needed, provide specific instructions like "Please remove the secret property" or "Please add a new 'Favorite Music Genre' property," and the AI will revise the definition.

## Generating and Utilizing Persona Instances

Once the class definition (design document) is finalized, the next step is to have the AI create multiple specific personas (instances) based on this design and respond as those personas.

Continue instructing the AI as follows:

```

Based on the approved persona class definition, create three random personas.

```

The AI will set random values for each property of the finalized persona class and present the information for three unique persona instances.

(Example of AI-generated personas - Actual content will be generated randomly)

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

Now, three specific characters based on the class definition have been generated.

Finally, let's have the AI respond as these personas.

```

Please give a brief self-introduction from each of the three personas created.

```

Executing this instruction, the AI will generate self-introductions considering each persona's personality, tone, background, etc.

(Example AI self-introductions)

```

Okay, here are brief self-introductions from each of the three personas:

**Professor Alex:**
"Hello there! It's wonderful to meet you! I'm Professor Alex, and I'm absolutely thrilled to help you explore and understand any topic you're curious about. No question is too small, and no challenge is too big – we'll tackle it together step-by-step. My goal is to make learning clear, engaging, and maybe even fun! What shall we dive into today?"

**Dr. Eleanor Vance:**
"Dr. Eleanor Vance. My area is nineteenth-century European social history. Popular narratives often obscure the past, so I focus on rigorous analysis of primary sources to uncover what *actually* occurred, rather than what we might wish had happened. If you have a specific historical query requiring careful examination of evidence, perhaps I can be of assistance."

**Cosmo Quickquill:**
"Hullo and how d'you do! I'm Cosmo Quickquill, and I love to spin tales like spiders spin webs – only mine are filled with sunshine, giggling critters, and maybe a little bit of everyday magic! Snuggle up, lend an ear, and let's see what wonder unfolds in our story today, shall we? Perhaps a tale about a brave button or a cloud that learned to sing?"

```

Thus, by using OOPD, it becomes possible to have the AI generate complex role settings (class definitions) from simple instructions, create specific information (instances) based on those definitions, and further have it respond consistently as those roles.

## Methods and Events: Giving Personas "Movement"

So far, we have primarily defined persona "attributes (properties)." In OOPD, by additionally defining persona "**operations (methods)**" and "**occurrences (events)**," the AI's behavior can be further enriched and dynamically controlled.

- **Method:**
  - **Meaning:** Represents "actions" or "capabilities" that the persona (object) can perform.
  - **Role in OOPD:** Serves as an instruction for the AI to execute specific "behaviors" or "processes."
  - **Example (Persona Class):**
    - `introduceSelf()`: The persona introduces itself based on its information.
    - `analyzeData(dataToAnalyze: String): String`: Analyzes the given data and returns the result.
    - `expressEmotion(emotionType: String)`: Expresses a specific emotion.
  - **How to Describe (User Format):** Create a section `**Method:**` within the class definition and describe using the format `- methodName(arguments): ReturnType`. (Type specification is recommended but not mandatory).

- **Event:**
  - **Meaning:** A mechanism to notify externally that "something happened" within the persona (object).
  - **Role in OOPD:** Serves as an instruction to make the AI recognize the occurrence of specific "state changes" or "triggers" and prompt corresponding responses or subsequent processes.
  - **Example (Persona Class):**
    - `MoodChanged(newMood: String)`: Indicates that the persona's mood has changed.
    - `NewInfoAcquired(infoContent: String)`: The persona has acquired new knowledge or information.
    - `GoalAchieved()`: The persona has achieved a set goal.
  - **How to Describe (User Format):** Create a section `**Event:**` within the class definition and describe using the format `- eventName(arguments)`. (Usually, there is no return value).

By adding these methods and events to the class definition, it becomes possible to give the AI more specific and context-dependent instructions, such as "Have Kenta Sato analyze this data," or "When Misaki Takahashi achieves her goal, make her say a special line."

**Let's try instructing the AI:**

```

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

By instructing like this, the AI updates the class definition and becomes capable of recognizing these new behaviors and state changes.

## Outputting the Definition

The class definition created and modified through interaction with the AI is internally stored and managed by the AI. You can have this definition outputted in a formatted OOPD format for later review or reuse elsewhere.

To output the current definition content, instruct as follows:

```

Output the current persona class definition in OOPD format.

```

The AI will output the latest class definition (including properties, methods, and events) enclosed in a Markdown code block (`~~~markdown ... ~~~`), adhering to the strict OOPD rules (module definition, English naming conventions, etc.). There is no distinction like User Format/Definition Format when using English, unlike when used in other language environments.

Using this output feature allows you to retrieve the design document crafted through interaction with the AI in an accurate format at any time.

**【Points about the English Specification】**
When using OOPD in English, unlike when using it in other languages such as Japanese, there is no distinction between User Format and Definition Format. You must write according to a strict format with defined naming conventions. Key rules include:

- **Single Format:** Always write in the strict format.
- **Adherence to Naming Conventions:** You must follow the defined English naming conventions, such as `PascalCase` for class names and `camelCase` for property and method names. The AI may point out or correct rule violations.
- **Mandatory Module Definition:** All definitions must be written within a module (`## module.name`).

## Summary: New Possibilities for AI Collaboration with OOPD

Object-Oriented Prompt Design (OOPD) is an effective framework for structuring instructions to AI, enhancing the consistency of its interpretation and responses. Especially in situations requiring complex settings or role assignments, it reduces the user's effort in giving instructions and enables more efficient and advanced AI collaboration by allowing the AI to proactively complement and manage details. Utilizing methods and events allows for designing even more dynamic AI behaviors. Leveraging the definition output feature also enhances the reusability of the created design documents.

We encourage you to try OOPD and experience the new possibilities in dialogue and collaborative work with AI.
```
