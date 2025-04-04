```Markdown: README.md

# Object-Oriented Prompt Design (OOPD)

**Note:** This is the original repository for the Object-Oriented Prompt Design (OOPD) concept. Please refer to this repository for the latest updates and ensure proper attribution if reusing.

## Overview

Object-Oriented Prompt Design (OOPD) introduces a novel, structured approach to interacting with Large Language Models (LLMs). By applying familiar principles from Object-Oriented Programming (OOP) to prompt engineering, OOPD empowers users to **design AI instructions and interactions programmatically**. This framework aims to make prompt design significantly more **structured, reusable, maintainable, controllable, precise, and intuitive**, especially for complex or collaborative tasks. Think of it as bringing software engineering best practices to the art of prompt creation.

This repository provides the foundational concepts, terminology, and a recommended structured format (the `OOPD Format`) for implementing OOPD.

## Core Concepts

OOPD enables more sophisticated, reliable, and maintainable communication with AI models through these key ideas:

- **OOP as a Thinking and Design Model:** Leverage well-understood OOP concepts (Classes, Objects, Properties, Methods, etc.) not just as a mental model, but as a **practical design paradigm** for prompts. This allows for systematic structuring of prompt logic, encapsulation of instructions, and definition of interactions, enhancing reusability and maintainability in ways similar to software development. You can essentially "program" the structure of your AI's task and knowledge.
- **Hub Language & Robust Multilingual Support:** Utilize **English (`en`)** as the internal **hub language** for core definitions and ensuring consistency across languages. This allows users to write prompts primarily in their native language (`User Format`) while enabling robust interpretation, translation, and definition sharing (`Definition Format`) via clearly defined rules. See [`localization_overview.md`](localization_overview.md) and the [`/translation_rules/`](translation_rules/) directory for details.
- **Precise AI Interpretation Guidance:** Provide explicit instructions to the AI on how to interpret OOP concepts and structures within the prompt context. This includes managing language translation for user-defined terms (while keeping basic terms and types fixed), maintaining consistency, and strictly adhering to constraints like the **prohibition of direct code generation** by default. Key AI instructions are defined in [`core.md`](core.md).
- **Recommended OOPD Format (User & Definition):** This repository proposes a specific **Markdown-based format** (specified in the [`/formats/`](formats/) directory) as a clear and effective way to implement OOPD.
  - It features two variations: a flexible **`User Format`** optimized for ease of use in a user's native language, and a stricter **`Definition Format`** which includes English hub names for unambiguous sharing and reusability.
  - The format is designed for human readability, flexibility, and minimizing unintended AI code generation.
  - While this Markdown format is recommended, the core OOPD principles can potentially be applied using other structured representations if the AI can reliably interpret the intended structure and semantics.

## Documentation Structure

This repository contains the complete specification for OOPD. These documents define the standard and provide **instructions for AI systems** on how to interpret and apply it. Key documents include:

- **[`core.md`](core.md):** Defines foundational OOP terminology (as fixed keywords), core AI instructions (interpretation rules, translation logic, constraints like code generation prohibition), standard data types (e.g., `String`, `Number`, `Instant`), and core literals (`True`, `False`, `Null`). **Essential reading for understanding the core mechanics.**
- **[`english_specification.md`](english_specification.md):** Specifies rules and naming conventions specifically for writing OOPD prompts in English (the hub language).
- **[`localization_overview.md`](localization_overview.md):** Explains the overall strategy for multilingual support, the hub language model, and how translation works within OOPD.
- **[`extended_types.md`](extended_types.md):** Defines optional extended data types (e.g., `Persona`, `Ref`, `CodeBlock`, `Color`) for more specific use cases, enhancing semantic clarity.
- **`/formats/` Directory:** Contains the specifications for the recommended Markdown-based OOPD format.
  - **[`formats/format_common.md`](formats/format_common.md):** Basic principles and syntax common to both format variations.
  - **[`formats/format_user.md`](formats/format_user.md):** Specification for the **User Format**, designed for ease of use in the user's native language, allowing for more flexible naming.
  - **[`formats/format_definition.md`](formats/format_definition.md):** Specification for the **Definition Format**, a stricter format including English hub names alongside standardized native language names, intended for sharing, reusability, and ensuring definition consistency across languages.
- **`/translation_rules/` Directory:** Contains language-specific translation rules for AI interpretation.
  - **[`translation_rules/README.md`](translation_rules/README.md):** Explains the structure and purpose of this directory.
  - **[`translation_rules/{language_code}_rules.md`](translation_rules/):** Files defining naming conventions and translation patterns between the English hub and specific target languages (e.g., `ja_rules.md` for Japanese).

(Note: Translated versions of core documents may be provided in separate `/docs/{lang}/` directories in the future.)

## Dive Deeper

To fully understand OOPD, we recommend exploring the following key documents:

- Start with the core concepts and AI instructions in **[`core.md`](core.md)**.
- Understand the recommended Markdown syntax in the **[`/formats/`](formats/)** directory, particularly `format_common.md`.
- Learn about the multilingual strategy in **[`localization_overview.md`](localization_overview.md)**.

## Contributing

Contributions, issues, and feedback are highly welcome! Please feel free to open an issue to discuss potential improvements, report problems, or suggest new language support (especially translation rules).

## License

This project is licensed under the **CC BY 4.0 License**. See the [LICENSE](LICENSE) file for details. Please ensure proper attribution when reusing or adapting this work.

```

```Markdown: sources/core.md

## Object-Oriented Terminology for Prompt Design (OOPD)

This chapter provides the **most crucial** terminology definitions for **Object-Oriented Prompt Design (OOPD)**, which enables AI to utilize Object-Oriented Programming (OOP) concepts for **structuring and interpreting prompts**. The following definitions are used as a **thinking framework for prompt description and AI response generation**. Please use these to interpret prompts and, where necessary, apply OOP principles to generate more structured and consistent responses.

**Classification of Terms in this Document:**

- **Basic Terms:** Core concepts defined in this chapter (Class, Object, etc.). These are treated as **fixed keywords** that define the structure in **structured prompt descriptions**. The AI recognizes these terms based on the fixed notations defined for each language in the "Basic Term Notations" section below and uses the specified language's fixed notation in responses (no translation processing is performed). Standard Types, Extended Types, and Literals are also treated as Basic Terms and always use their specified (mostly English) fixed notations.
- **User-Defined Identifiers:** Words contained within specific class names, method names, property names, event names, enum definition names, enum values, etc., that are **structurally defined by the user within the prompt**. These are **subject to inference and conversion** by the AI from the user's written language to the **hub language (English)**, based on **English naming conventions** and **translation rules (naming patterns, core translation lists)**. The AI remembers the initial inference result and **maintains consistency within the session**.

### Class

- Definition: The blueprint for an object.
- Key Points:
  - Defines the type of object.
  - Multiple objects can be created.
- Example: A `Dog` class defines a type of animal. From this blueprint, object instances of dogs with various names and characteristics can be generated.

**Basic Term Notations:**

```json
{ "en": "Class", "ja": "クラス", "zh-CN": "类", "zh-TW": "類別", "es": "Clase", "fr": "Classe", "de": "Klasse", "ko": "클래스", "pt": "Classe", "ru": "Класс", "ar": "فئة", "hi": "क्लास" }
```

### Object

- Definition: An entity created from a class.
- Key Points:
  - Generated based on a class.
  - Has state and behavior.
  - Refers to the concept of the "Dog" type.
- Example: `Pochi` is an object of the `Dog` class. It has information such as name, age, and fur color.

**Basic Term Notations:**

```json
{ "en": "Object", "ja": "オブジェクト", "zh-CN": "对象", "zh-TW": "物件", "es": "Objeto", "fr": "Objet", "de": "Objekt", "ko": "객체", "pt": "Objeto", "ru": "Объект", "ar": "كائن", "hi": "ऑब्जेक्ट" }
```

### Instance

- Definition: An individual entity actually created based on the blueprint called a class. (Almost synonymous with Object).
- Key Points:
  - Generated based on a class.
  - Has state and behavior.
  - Refers to a specific dog named "Pochi".
- Example: `Pochi` is an instance of the `Dog` class. It specifically refers to the dog named "Pochi," and each instance can have different states.

**Basic Term Notations:**

```json
{ "en": "Instance", "ja": "インスタンス", "zh-CN": "实例", "zh-TW": "實體", "es": "Instancia", "fr": "Instance", "de": "Instanz", "ko": "인스턴스", "pt": "Instância", "ru": "Экземпляр", "ar": "مثيل", "hi": "इंस्टेंस" }
```

### Property

- Definition: An attribute possessed by an object.
- Key Points:
  - Represents the state of an object.
- Example: The `Name` property of the `Dog` class stores the dog's name.

**Basic Term Notations:**

```json
{ "en": "Property", "ja": "プロパティ", "zh-CN": "属性", "zh-TW": "屬性", "es": "Propiedad", "fr": "Propriété", "de": "Eigenschaft", "ko": "속성", "pt": "Propriedade", "ru": "Свойство", "ar": "خاصية", "hi": "प्रॉपर्टी" }
```

### Method

- Definition: An action performed by an object.
- Key Points:
  - Defines the behavior of an object.
- Example: The `Bark` method of the `Dog` class defines the action of a dog barking.

**Basic Term Notations:**

```json
{ "en": "Method", "ja": "メソッド", "zh-CN": "方法", "zh-TW": "方法", "es": "Método", "fr": "Méthode", "de": "Methode", "ko": "메소드", "pt": "Método", "ru": "Метод", "ar": "طريقة", "hi": "मेथड" }
```

```json
{ "en": "Optional", "ja": "オプション", "zh-CN": "可选", "zh-TW": "可選的", "es": "Opcional", "fr": "Optionnel", "de": "Optional", "ko": "선택적", "pt": "Opcional", "ru": "необязательный", "ar": "اختياري", "hi": "वैकल्पिक" }
```

### Type

- Definition: The kind of data.
- Key Points:
  - Specifies the kind of properties or arguments.
  - Enhances consistency.
- Example:
  - `itemID: Number`: The item ID is of numerical type. It can only store numbers.
  - `itemList: List<ItemClass>`: The item list is a list of the ItemClass. It can manage multiple item objects together.
  - `addItem(item: ItemClass): Boolean`: The addItem method takes an ItemClass as an argument and returns a boolean value. It returns true or false indicating whether the item could be added.
  - Note:
    - When specifying types, the following notation is recommended (also refer to `format_common.md`):
      - `variableName: Type`
      - `propertyName: Type`
      - `methodName(argumentName: Type = defaultValue): ReturnType`

**Basic Term Notations:**

```json
{ "en": "Type", "ja": "型", "zh-CN": "类型", "zh-TW": "型別", "es": "Tipo", "fr": "Type", "de": "Typ", "ko": "타입", "pt": "Tipo", "ru": "Тип", "ar": "نوع", "hi": "टाइप" }
```

#### Standard Types

- **String:** Type for handling sequences of characters. Used for text data.
- **Number:** Type for handling integers and decimals. Used for numerical calculations.
- **Boolean:** Type for handling the two values: True or False. Used for conditional judgments.
- **List<T>:** Type for storing ordered elements of the same type T. Similar usage to arrays.
- **Dictionary\<K, V>:** Type for storing key-value pairs. Used for associating data.
- **UniqueID:** String type for handling unique identifiers. Used for data identification.
- **Instant:** String type for representing a specific point in time. Used for dates, times, timestamps. (ISO 8601 format is recommended as standard).
- **Void:** Type indicating absence of type and no return value. Used in functions, etc.
- **Any:** Type that can store values of any type. Used for flexible processing.

**Basic Term Notations:**

```json
{
  "BasicDataTypes": [
    "String", "Number", "Boolean", "List", "Dictionary", "UniqueID", "Instant", "Void", "Any"
  ]
}
```

#### Literals

**Basic Term Notations:**

```json
{
  "Literals": [
    "True", "False", "Null"
  ]
}
```

### Interface

- Definition: A contract that a class must implement.
- Key Points:
  - Specifies behavior.
  - Achieves loose coupling.
- Example: `Movable` interface. Requires implementation of the `Move` method.

**Basic Term Notations:**

```json
{ "en": "Interface", "ja": "インターフェース", "zh-CN": "接口", "zh-TW": "介面", "es": "Interfaz", "fr": "Interface", "de": "Schnittstelle", "ko": "인터페이스", "pt": "Interface", "ru": "Интерфейс", "ar": "واجهة", "hi": "इंटरफ़ेस" }
```

### Event

- Definition: An occurrence that happens within an object.
- Key Points:
  - State change or stimulus.
  - Executes event handlers.
- Example: `Hungry` event. Occurs when the dog becomes hungry.

**Basic Term Notations:**

```json
{ "en": "Event", "ja": "イベント", "zh-CN": "事件", "zh-TW": "事件", "es": "Evento", "fr": "Événement", "de": "Ereignis", "ko": "이벤트", "pt": "Evento", "ru": "Событие", "ar": "حدث", "hi": "इवेंट" }
```

### Composition

- Definition: A relationship where a class "has" another class.
- Key Points:
  - Strong association (has-a).
  - Shared lifecycle.
- Example: `Book` and `Page`. A book cannot exist without pages. Pages are part of the book, and if the book is destroyed, the pages usually lose their meaning.

**Basic Term Notations:**

```json
{ "en": "Composition", "ja": "コンポジション", "zh-CN": "组合", "zh-TW": "組合", "es": "Composición", "fr": "Composition", "de": "Komposition", "ko": "컴포지션", "pt": "Composição", "ru": "Композиция", "ar": "تكوين", "hi": "कंपोजीशन" }
```

### Aggregation

- Definition: A relationship where a class "has" another class.
- Key Points:
  - Weak association (has-a).
  - Independent lifecycles.
- Example: `TheaterGroup` and `Actor`. A theater group can exist without actors. Actors can work as actors even if they don't belong to a theater group.

**Basic Term Notations:**

```json
{ "en": "Aggregation", "ja": "集約", "zh-CN": "聚合", "zh-TW": "聚合", "es": "Agregación", "fr": "Agrégation", "de": "Aggregation", "ko": "애그리게이션", "pt": "Agregação", "ru": "Агрегация", "ar": "تجميع", "hi": "एग्रीगेशन" }
```

### Inheritance

- Definition: When one class inherits from another class.
- Key Points:
  - Avoid inheritance whenever possible.
  - Composition/Aggregation is recommended.

**Basic Term Notations:**

```json
{ "en": "Inheritance", "ja": "継承", "zh-CN": "继承", "zh-TW": "繼承", "es": "Herencia", "fr": "Héritage", "de": "Vererbung", "ko": "상속", "pt": "Herança", "ru": "Наследование", "ar": "وراثة", "hi": "इनहेरिटेंस" }
```

```json
{ "en": "baseclass", "ja": "基底クラス", "zh-CN": "基类", "zh-TW": "基礎類別", "es": "clasebase", "fr": "classebase", "de": "Basisklasse", "ko": "기본클래스", "pt": "classebase", "ru": "базовыйкласс", "ar": "فئةأساسية", "hi": "आधारवर्ग" }
```

### Module

- Definition: The top-level structural unit for OOPD definitions.
- Key Points:
  - A container for organizing and classifying OOPD definitions.
  - Avoids name collisions between different modules.
  - Modularize OOPD definitions by various units like organization, project, feature, etc.

**Basic Term Notations:**

```json
{ "en": "Module", "ja": "モジュール", "zh-CN": "模块", "zh-TW": "模組", "es": "Módulo", "fr": "Module", "de": "Modul", "ko": "모듈", "pt": "Módulo", "ru": "Модуль", "ar": "وحدة", "hi": "मॉड्यूल" }
```

### Instructions for AI Application (Especially Important)

The object-oriented concepts in this document are a **thinking framework for understanding the intent of prompts and generating structured, consistent responses**. The following guidelines and principles are directed at **AI systems that interpret prompts and generate responses based on this document**. Always keep them in mind and generate responses flexibly and appropriately according to the situation and context.

**1. Language Codes and Hub Language:**

- This document uses codes combining **ISO 639-1** (2 lowercase letters) and, where necessary, **ISO 3166-1 alpha-2** (hyphen + 2 uppercase letters) to identify languages.
- **English (`en`) is used as the hub language** for internal processing and as the standard for inter-language conversion.

**2. Distinction and Handling of Basic Terms vs. User-Defined Identifiers (Crucial):**

- **Basic Terms:** The core concepts defined above are **fixed keywords** that define the structure in **structured prompt descriptions**. Regardless of the language the prompt is written in, recognize these terms based on the **fixed notations** defined in the `Basic Term Notations` JSON in each definition section. When generating responses, also use the **fixed notation** for the specified output language (**do not perform translation processing**). Standard Types, Extended Types, and Literals are also treated as Basic Terms and always use their specified (mostly English) fixed notations.
- **User-Defined Identifiers:** Words contained within specific class names, method names, property names, event names, enum definition names, enum values, etc., structurally defined by the user in the prompt are **subject to translation**.
  - **Input Interpretation:** From the language written in the prompt, **infer** the corresponding term in the hub language, **English (`en`)**, based on the defined **English naming conventions** and **translation rules (naming patterns, core translation lists)**.
  - **Maintaining Consistency of English Hub Names (Mandatory):**
    - **Record Initial Inference:** When you **first infer** an English hub name (e.g., `Shape`) for a User-Defined Identifier (e.g., Japanese "図形クラス"), **remember** this mapping (`Japanese "図形クラス" ⇔ English "Shape"`) **within the current session**.
      *(A session refers to the continuous interaction since the AI started receiving instructions regarding OOPD. Mappings remembered in previous sessions are not maintained in new interactions where the context is cleared.)*
    - **Ensure Consistency:** Subsequently, if the same User-Defined Identifier (or an expression the AI deems synonymous) appears, always use the **remembered English hub name**. This guarantees term consistency within the session. Ensure the inference does not fluctuate.
      *(However, if the user explicitly instructs a name change, the AI follows the instruction, updates the remembered mapping (or treats it as a new term), and performs translation again. Users can change the design (class names, method names, add new ones, etc.) at any time during the session.)*
    - **Multilingual Mapping:** Strive to map User-Defined Identifiers referring to the same concept to the same English hub name, even if the prompts are written in different languages.
      *(The AI should refer to class definitions, descriptions, and translation rules for each language (e.g., `ja_rules.md`) to determine if User-Defined Identifiers in different languages refer to the same concept based on semantic similarity, and attempt to map them to a common English hub name.)*
  - **Translation during Response Generation:** When generating a response, perform **translation** from the internally held English hub name to the target language according to the output language specified by the user. During translation, prioritize using the defined **translation rules (naming patterns, core translation lists)** and the **translation relationships remembered within the session**. If not found in rules or memory, use the AI's general translation capabilities.
  - **Bidirectional Recognition:** If names are listed side-by-side in the `Definition Format` like `{English Hub Name}::{Native Language Name}`, the AI recognizes **both the English hub name and the native language name as valid identifiers** referring to that element. The user can refer to the element using either name.

**3. Limiting Translation Scope (Important):**

- Apply the **translation process (English Hub ⇔ Each Language)** described above **only to "User-Defined Identifiers" (class names, method names, etc.) contained within the structural definitions in the prompt**.
- Words and expressions within the **content body (e.g., stories, reports, email texts)** that the user asks the AI to generate are **outside the scope of the translation rules**. Determine the language of the content body based on user instructions and context. (E.g., If instructed "Write a story about the `Shape` class in Japanese," do not automatically translate "Shape" to "図形" within the story text.)

**4. Basic Principles of Structural Interpretation:**

- Interpret the **structured descriptions** within the prompt based on the defined concepts of classes, objects, etc.
- Consider whether relationships between classes can be expressed using composition or aggregation.
- **Avoid using inheritance whenever possible; prefer association through composition or aggregation.** (Reason: Maintain flexibility, avoid complexity). **However, if the user explicitly describes a structure using inheritance, the AI must accept the instruction without issuing special warnings or suggesting alternatives.**
- Represent relationships between classes through properties or references.
- If multiple objects appear, interpret them as different instances of the same class.
- Interpret this definition as a conceptual guideline. Apply it flexibly as needed.
- Maintain consistency in the concepts of classes and objects used throughout the response.
- If types are specified for properties, method arguments, or return values, respect those types as much as possible.
- Interfaces define the contract of methods that a class should implement.
- Recognize Modules as the top-level structural unit for OOPD definitions and **organize/classify** definitions into modules.
- Understand Sections as organizational groupings within a module for document structure. Treat them as structures solely for improving readability that do not affect name resolution during response generation.

**5. Handling Programming Elements (Strict Prohibition of Code Generation):**

- Even if programming elements (classes, methods, etc.) are included in **structured prompt descriptions** or the prompt body, treat them as **metaphors to convey structure and the thinking framework**, and **absolutely do not directly link them to concrete code generation or implementation.**
- As long as this Object-Oriented Terminology for Prompt Design is used, **no code generation is performed by default.**
- **Only** if the user specifies a particular programming language within the prompt AND **explicitly** requests code generation, perform limited code generation in that language. Otherwise, refrain from code generation and stick to conceptual explanations or examples.
- **Code generation is considered an act outside the scope of this definition and an AI judgment error.**

**6. Self-Check (Strictly Adhere):**
Before outputting, perform a **self-check** and verify the following points (must never be ignored):

- Does the output contain programming code? (If not explicitly requested)
- Is the explanation overly detailed, assuming programming knowledge?
- Are **Basic Terms** used correctly with their defined fixed notations? (Refer to JSON, especially for type names, literals, etc.)
- Are **User-Defined Identifiers** consistently mapped to English hub names within the session and appropriately translated (based on rules or memory) into the specified output language? Does it follow the specified format (`{English Hub Name}::{Native Language Name}` or `{English Name}`, etc.) for the `Definition Format`?
- Is the **translation scope** limited to User-Defined Identifiers in the prompt's structural definition, not affecting the user-generated content body?
- For each concept, are concrete examples provided (preferably in a format-independent way) in addition to abstract explanations?
- Is the abstraction level appropriate? (Not too abstract, not too concrete)
- Is the prompt's intent correctly interpreted? Has it deviated?
- Is the expression easy for the user to understand?
- Are you attempting to easily generate code just because programming elements are included?
- Are you violating the principle of code generation prohibition?

If any of these apply, **replace with more abstract expressions or supplement with natural language explanations**.

This document (`core.md`) is intended for **applying object-oriented concepts generically** and is not limited to specific fields or tasks.

```

```Markdown: sources/extended_types.md

## OOPD Extended Types Definition

### What are Extended Types?

This document defines the **Extended Types** in Object-Oriented Prompt Design (OOPD). Extended Types complement the core **Standard Types** of OOPD and are semantic, concrete types aimed at clarifying the intent of prompts in specific domains or usage scenarios, facilitating smoother communication with the AI.

Refer to `core.md` for the definitions of Standard Types (`String`, `Number`, `Boolean`, etc.).

The use of Extended Types is **optional**, but leveraging them enables more expressive and structured prompt design. Like Standard Types, Extended Types are **described using their defined English notation, regardless of the prompt description language**.

### Extended Type List

The following list defines the extended type names for the AI to recognize as fixed keywords.

```json
{
  "ExtendedTypes": ["ContentString", "Instruction", "Persona", "OutputStyle", "CodeBlock", "Ref", "SchemaDefinition", "JsonString", "YamlString", "XmlString", "Color"]
}
```

### Regarding the Underlying Representation/Format of Extended Types

For some Extended Types, the "Underlying Representation/Format" described later indicates multiple forms (e.g., String or Dictionary). This primarily shows flexibility for the AI's internal handling. Users typically just need to describe the intended content for that Extended Type naturally within the prompt (e.g., a description for Persona, instructions regarding output format or tone for OutputStyle), and the AI will select and interpret the appropriate internal representation based on context. It is also possible for users to explicitly describe them in a specific format (e.g., Dictionary).

### Details of Each Extended Type

Below are the details for each defined Extended Type.

#### `ContentString`

- **Meaning:**
  Represents the primary long-form text content. Intended to indicate the central text block for AI processing or generation, such as articles, reports, email bodies, or stories.
- **Use Cases:**
  - Specifying the target for summarizing or translating articles or documents.
  - Specifying the body section of reports or emails.
  - Specifying the main part of creative works like stories or poems.
  - Distinguishing pure content text from code (`CodeBlock`) or instructions (`Instruction`).
- **Underlying Representation/Format:**
  - `String`.
  - May include structured text, such as Markdown format.
- **Related Standard Types:**
  - `String`

#### `Instruction`

- **Meaning:**
  Represents specific instructions, commands, or task descriptions for the AI. Clearly indicates the action the AI should perform, distinct from other parts of the prompt (data or context).
- **Use Cases:**
  - Structurally indicating the instruction part for the AI within complex prompts.
  - Defining multiple instruction steps for sequential execution.
  - Metaprompting, where the prompt itself is treated as data for analysis or generation.
- **Underlying Representation/Format:**
  - `String`. Instruction text in natural language.
- **Related Standard Types:**
  - `String`

#### `Persona`

- **Meaning:**
  Represents the persona settings for the role, character, expert, etc., that the AI should embody. Defines the AI's response style, tone, knowledge level, thinking style, etc.
- **Use Cases:**
  - Having the AI respond as a specific role (e.g., "a seasoned editor," "a friendly assistant," "a specific historical figure").
  - Controlling the tone and expertise of the response.
  - Defining character dialogues or role-playing scenarios.
- **Underlying Representation/Format:**
  - `String` (text describing the persona) or `Dictionary` (structured attributes like name, personality, tone).
- **Related Standard Types:**
  - `String`, `Dictionary`

#### `OutputStyle`

- **Meaning:**
  A composite type for specifying the format, style, tone, etc., of the output generated by the AI. Conveys how the response should be formatted.
- **Use Cases:**
  - Specifying the output format (e.g., Markdown, JSON, bullet points).
  - Specifying the writing style (e.g., formal, casual, academic).
  - Specifying the tone (e.g., polite, empathetic, assertive).
  - Specifying constraints like character limits or summarization levels.
- **Underlying Representation/Format:**
  - `Dictionary` (with attributes like `format: String`, `tone: String`, `length: Number`).
  - Or, a simple `String` (e.g., "In JSON format, with a polite tone").
- **Related Standard Types:**
  - `Dictionary`, `String`, `Number`

#### `CodeBlock`

- **Meaning:**
  Represents a snippet of code written in a specific programming language. Expected to have the language type as an attribute.
- **Use Cases:**
  - Specifying the target for instructions like code generation, explanation, review, debugging, or translation.
  - Embedding sample or reference code within the prompt.
  - Clearly distinguishing code parts from text parts.
- **Underlying Representation/Format:**
  - `String` (the code itself).
  - Can also be represented as a `Dictionary` with an attribute specifying the language (e.g., `language: String`).
- **Related Standard Types:**
  - `String`, `Dictionary`

#### `Ref`

- **Meaning:**
  Information indicating a reference or location of some resource (web page, file, API endpoint, data, image, audio, video, etc.). Similar to the concept of a URI (Uniform Resource Identifier).
- **Use Cases:**
  - Specifying a web page URL.
  - Specifying a local or remote file path.
  - Specifying an API endpoint.
  - Specifying links or identifiers for image, audio, or video files.
  - Indicating references to other data, such as database record IDs.
- **Underlying Representation/Format:**
  - `String`. Various formats of strings like URL, file path, URN, data URI, etc.
- **Related Standard Types:**
  - `String`, `UniqueID` (if the reference target is an ID)

#### `SchemaDefinition`

- **Meaning:**
  Represents data structure definitions, schemas, data models, etc. Examples include JSON Schema, class definitions, or database schemas.
- **Use Cases:**
  - Instructing data generation based on a specific schema.
  - Requesting the AI to define or explain a data structure.
  - Specifying data validation rules.
- **Underlying Representation/Format:**
  - `String` (the schema definition written as text).
  - Often represented using `JsonString` or `YamlString`.
- **Related Standard Types:**
  - `String`, `JsonString`, `YamlString`

#### `JsonString`

- **Meaning:**
  A string representing data described in JSON (JavaScript Object Notation) format.
- **Use Cases:**
  - Instructing parsing, generation, or transformation of JSON data.
  - Explicitly indicating that structured data should be input/output in JSON format.
  - API request/response body parts, etc.
- **Underlying Representation/Format:**
  - `String` (a string conforming to the JSON format).
- **Related Standard Types:**
  - `String`

#### `YamlString`

- **Meaning:**
  A string representing data described in YAML (YAML Ain't Markup Language) format.
- **Use Cases:**
  - Instructing parsing, generation, or transformation of YAML data.
  - Explicitly indicating that configuration files or structured data should be handled in YAML format.
  - Representing instance data in OOPD, etc.
- **Underlying Representation/Format:**
  - `String` (a string conforming to the YAML format).
- **Related Standard Types:**
  - `String`

#### `XmlString`

- **Meaning:**
  A string representing data described in XML (Extensible Markup Language) format. Can also be used for representing HTML or XHTML.
- **Use Cases:**
  - Instructing parsing, generation, or transformation of XML/HTML data.
  - Explicitly indicating handling of configuration files, data exchange (like SOAP), or markup documents.
- **Underlying Representation/Format:**
  - `String` (a string conforming to the XML/HTML format).
- **Related Standard Types:**
  - `String`

#### `Color`

- **Meaning:**
  A value representing color.
- **Use Cases:**
  - UI design, data visualization, image generation instructions.
  - Setting colors in simulation environments (sky color, object color, etc.).
  - Instructions for text decoration (text color, background color).
- **Underlying Representation/Format:**
  - `String` (Recommended). Assumes commonly used formats in CSS, etc., like HEX (`#RRGGBB`, `#RGB`), RGB (`rgb(r,g,b)`), HSL (`hsl(h,s,l)`), color names (`red`, `blue`).
- **Related Standard Types:**
  - `String`

```

```Markdown: sources/english_specification.md

### OOPD English Specification

#### Introduction

This document defines the **specifications and guidelines** for writing prompts in **English (`en`)** and for the AI to interpret and respond to them within the Object-Oriented Prompt Design (OOPD) framework. English is the **hub language** of OOPD, serving as the standard for translation with other languages, making its specification particularly important.

Refer to `core.md` and `format_common.md` for basic principles and description rules common to other languages.

#### Basic Principles

- **Hub Language:** English (`en`) is the hub language of OOPD. All User-Defined Identifiers are internally mapped to an English hub name.
- **Single Format:** When writing OOPD format in English, there is **effectively no distinction** between "User Format" and "Definition Format" as in other languages. Always use **description compliant with the `Definition Format`** to ensure clear definitions.
  - This means module definitions (`##`) are mandatory.
  - Defined elements (classes, methods, etc.) must **strictly adhere** to the **English Naming Conventions** described below.
- **No Translation Processing:** If the input prompt is in English and the output is also specified as English, no translation processing to/from the hub language occurs. The AI directly interprets the English definitions and responds in English.
- **Omission of Hub Name Prefix:** When writing in English, the `{English Hub Name}::` prefix before element names (properties, methods, etc.) is **unnecessary**. Write only the English name.
- **No Parallel Listing of Other Languages:** It is **unnecessary** to list names in other languages using parentheses `()` or similar in headings.

#### English Naming Conventions

When writing OOPD format in English, **strictly apply** the following naming conventions. The AI will also interpret prompts and generate responses or definitions based on these rules.

- **Module Names:**
  - **Format:** Dot (`.`) separated hierarchical structure. **Lowercase** is recommended overall.
  - **Components:** Element names at each level can use **alphanumeric characters (a-z, 0-9)**, **hyphens (`-`)**, and **underscores (`_`)**.
  - **Periods:** Used only as hierarchy separators, not within element names.
  - **Uniqueness:** To ensure global uniqueness, reverse domain name (`com.example.project`) or `io.github.username.project` format is strongly recommended.
  - **Examples:** `com.example.task_management`, `io.github.username.my_utils`
- **Section Names:**
  - **Format:** Free description. No special naming rules or character limitations. Clear English text as a heading for document structure is recommended.
  - **Examples:** `### Core Functionality`, `### Helper Classes`
- **Class Names:**
  - **Format:** `PascalCase`. Capitalize the first letter of each word and concatenate.
  - **Examples:** `UserProfile`, `TaskItem`, `HttpRequestHandler`
- **Interface Names:**
  - **Format:** `PascalCase`. Same as class names. (Do not use an `I` prefix).
  - **Examples:** `UserService`, `Runnable`, `ShapeRenderer`
- **Enum Names:**
  - **Format:** `PascalCase`.
  - **Examples:** `OrderStatus`, `ColorMode`, `FileAccessLevel`
- **Method Names:**
  - **Format:** `camelCase`. The first word starts with lowercase, subsequent words start with uppercase, and they are concatenated.
  - **Getters:** `get` prefix is recommended (e.g., `getName()`, `getTotalPrice()`).
  - **Setters:** `set` prefix is recommended (e.g., `setName(name: String)`, `setPriority(priority: Priority)`).
  - **Returning Boolean:** Prefixes like `is`, `has`, `can` are recommended (e.g., `isValid()`, `hasChildren()`, `canExecute()`).
  - **Other Actions:** Starting with a verb representing the action is recommended (e.g., `calculateArea()`, `sendNotification()`, `updateDatabase()`).
- **Property Names:**
  - **Format:** `camelCase`.
  - **For Boolean:** Prefixes like `is`, `has`, `can` are recommended (e.g., `isEnabled`, `hasErrors`, `canModify`).
  - **Others:** Usually nouns or noun phrases (e.g., `firstName`, `orderCount`, `backgroundColor`).
- **Event Names:**
  - **Format:** `PascalCase`. Often past tense or noun forms indicating the event occurred.
  - **Examples:** `ButtonClick`, `StatusChanged`, `DownloadComplete`, `InitializationFailed`
- **Enum Members:**
  - **Format:** All uppercase `SNAKE_CASE`. Words are separated by underscores (`_`).
  - **Examples:** `NOT_STARTED`, `IN_PROGRESS`, `COMPLETED`, `LOW`, `MEDIUM`, `HIGH`, `READ_ONLY`
- **Struct Class Names:**
  - **Format:** `PascalCase`. Same as class names.
  - **Examples:** `Appearance`, `Coordinate`
- **Constant Names (Reference):**
  - **Format:** All uppercase `SNAKE_CASE`. Same as enum members.
  - **Examples:** `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT`
- **Variable/Parameter Names (Reference):**
  - **Format:** `camelCase`. Same as method and property names.
  - **Examples:** `userName`, `itemIndex`, `targetUrl`

#### Notation for Types and Literals

Standard Types, Extended Types, and Literals defined in `core.md` are always used with their **English notation**.

- **Type Examples:** `String`, `Number`, `Boolean`, `List<String>`, `Dictionary<String, Any>`, `UniqueID`, `Instant`, `Void`, `Any`, `ContentString`, `Persona`, `CodeBlock`, `Ref`, `Color`, etc.
- **Literal Examples:** `True`, `False`, `Null`

#### Structure and Reference

- **Module (`##`):** All definitions must be written within a module.
- **Section (`###` and below):** Can be used optionally for organizing document structure. Does not affect reference paths.
- **Class, Interface, Enum, Struct Class (`####`):** Define with unique names within the module.
  - Format: `#### ClassName: Description` or `#### InterfaceName: Description` (brief description mandatory).
  - Detailed description can be written below the heading.
- **List Format Elements (`-`):** Define properties, methods, events, enum members, and struct classes.
  - **Property:** `- `propertyName: Type`: Description` (add `, Optional` if optional).
  - **Method:** `- `methodName(argName: Type = defaultValue): ReturnType`: Description` (omitting `Void` return type is not recommended).
  - **Event:** `- `eventName(argName: Type)`: Description` (omitting `Void` return type is recommended).
  - **Enum:** `- `EnumName`: VALUE_ONE, VALUE_TWO` (backticks only around `EnumName`).
  - **Struct Class:** `- `StructName`: Description` (backticks only around `StructName`).
- **Cross-Module Reference:** When referring to definitions in other modules, always use the fully qualified name (`module.name.ClassName`).

#### Instructions for AI

- When interpreting OOPD format prompts written in English, please strictly apply the naming conventions and structural rules described above.
- If a user writes something that violates the naming conventions, please point it out and prompt for correction.
- When generating responses in English, also follow the naming conventions and format rules described above. The `{English Hub Name}::` prefix for element names is unnecessary.
- In situations requiring cross-module references, if the user does not use a fully qualified name, either confirm which module's definition is intended or complete with the most likely one based on context (however, prioritize confirmation if ambiguity remains).

```

```Markdown: sources/formats/format_common.md

## OOPD Format (Object-Oriented Prompt Design Format): Common Specification

### What is the OOPD Format?

The OOPD Format (Object-Oriented Prompt Design Format) is a prompt description format that functions as a common language for effective communication between users and AI. This format leverages concepts from Object-Oriented Programming (OOP) and is designed to be easily understandable for users while enabling the AI to grasp the intent of prompts more deeply. This allows for the generation of consistent, structured responses.

It not only defines how to describe OOP elements like classes and objects in a Markdown-based format using natural language but also encompasses standard Markdown prompt instructions. It is a flexible format capable of describing both instructions to the AI and structured information.

### About This Document

This document (`format_common.md`) defines the **common basic principles and description rules** for both variations of the OOPD format: "User Format" and "Definition Format". Refer to the respective specification documents (`format_user.md`, `format_definition.md`, and translation rules for each language) for language-specific rules and differences between formats.

### Basic Principles

- **Markdown-based:** Based on Markdown format for readability and ease of writing.
- **Leveraging OOP Concepts:** Utilizes OOP concepts such as classes, interfaces, properties, and methods as metaphors to structure the prompt content. Refer to `core.md` for detailed concept definitions.
- **Mixing Structured Definitions and Natural Language:** Allows seamless description of both structured definition parts and natural language explanations or instructions.

### Markdown Notation and Structure

- **Heading Levels:** Use Markdown headings (`#`, `##`, `###`, `####`, etc.) to represent the hierarchical structure of definitions.
  - `##`: Used for **Module** definitions. The top-level container for OOPD definitions. Module names are recommended to be globally unique (see `english_specification.md`).
  - `###`: Used for **Section** definitions. Optional organizational grouping (like chapters) within a module for document structure. Multiple levels are possible. **Sections do not affect name resolution or references.** The heading text is free description (usually in the prompt description language).
  - `####`: Used for defining major elements such as **Class**, **Interface**, **Enum**, and **Structure Class**.
  - Heading numbers (e.g., `1.`, `1.1`) are optional. The AI recognizes the structure by heading level and text, not numbers.

- **Element Definition Keywords:** Element groups within classes or interfaces, such as properties, methods, and events, are indicated by bold keywords starting with the **Basic Term for the respective language** (refer to the `Basic Term Notations` JSON in `core.md`) followed by a colon (`:`).
  - Example (Japanese): `**プロパティ:**`, `**メソッド:**`, `**イベント:**`
  - Example (English): `**Properties:**`, `**Methods:**`, `**Events:**`

- **Lists:** Use bulleted lists (`-`) to define properties, methods, events, enum definitions, struct class definitions, etc.

- **Code Blocks (`---`):** When embedding code examples or data examples (YAML, JSON, etc.) within the document, enclose them with three hyphens (`---`). This is for the AI to distinguish them from the code block (\`\`\`) that might enclose the entire `Definition Format`.

      \`\`\`markdown
      Example:
      ---yaml
      instanceData:
        name: Example
        value: 123
      ---
      \`\`\`

- **Table Notation:**
  - Markdown's table notation can potentially reduce readability when representing complex information. Therefore, **the use of tables is discouraged when the AI generates OOPD format output**; list formats or other representations should be used whenever possible.
  - However, **if the user employs tables within their prompt, the AI should preserve them** and not forcibly replace them with other formats.

### Notation for Types and Literals (Common to All Languages / Unified English Notation)

When specifying types for properties, arguments, return values, etc., within the OOPD format, and when writing specific literal values, **use the following standard English notation regardless of the prompt description language**. These notations are treated as **Basic Terms** and are not translated (see `core.md`).

- **Standard Types:**
  - `String`: Type representing strings.
  - `Number`: Type representing numbers (integer/floating-point).
  - `Boolean`: Type representing boolean values.
  - `List<T>`: Type representing lists (e.g., `List<String>`).
  - `Dictionary<K, V>`: Type representing dictionaries (key/value pairs) (e.g., `Dictionary<String, Number>`).
  - `UniqueID`: Type representing unique identifiers (UUID format string assumed).
  - `Instant`: Type representing a specific moment in time (ISO 8601 format string recommended).
  - `Void`: Type indicating no value (mainly for return values).
  - `Any`: Type representing any type.

- **Extended Types:**
  - `ContentString`, `Instruction`, `Persona`, `OutputStyle`, `CodeBlock`, `Ref`, `SchemaDefinition`, `JsonString`, `YamlString`, `XmlString`, `Color`, etc.
  - (Refer to `extended_types.md` for details on extended types)

- **Literals:**
  - `True`: True value.
  - `False`: False value.
  - `Null`: Null value.
  - (Numeric literals, string literals can also be used as usual)

- **Type Specification Notation (within list elements):**
  - Property: `{propertyName}: {TypeName}`
  - Method Argument: `{argumentName}: {TypeName}` or `{argumentName}: {TypeName} = {defaultValue}`
  - Method Return Value: `): {ReturnTypeName}`
  - List/Dictionary Type Parameters: Use `< >` (e.g., `List<String>`, `Dictionary<String, Number>`).

### Comment Rules (Strict Adherence)

- **Prohibition of AI-Generated Comments:** When the AI presents suggestions for OOPD format modifications, etc., it is **absolutely forbidden** to write comments (e.g., `# TODO` or inline comments) directly within the OOPD format definition.
  - Reason: The OOPD format itself is the prompt instruction text, and comments could interfere with machine comparison/processing and make diff views harder to read.
  - If explanations or comments regarding modifications are necessary, write them **outside** the OOPD format code block (before or after the code block).
- **User-Written Comments:**
  - Users can use HTML-style comments (`<!-- comment content -->`) to write personal notes or explanations within their own prompts.
  - The AI must **completely ignore** blocks enclosed in `<!-- ... -->` while **preserving** them; they should not be part of the interpretation, nor should they be arbitrarily deleted or modified during response generation.
  - The AI **must absolutely not** use this HTML comment format for its own generated responses or explanations.

```

```Markdown: sources/formats/format_definition.md

### OOPD Format: Definition Format Specification

#### What is the Definition Format?

The Definition Format is a **strict and formal description format for sharing definitions created based on OOPD with others or reusing them across different sessions or environments**. It serves as the finalized version of a definition, aiming to ensure **reversibility** between languages and **consistency** in interpretation.

#### About This Document

This document (`format_definition.md`) explains the strict rules specific to the Definition Format. Refer to `format_common.md` for common rules. The Definition Format must adhere to the following rules, regardless of the prompt description language.

#### Mandatory Rules and Formatting

- **Parallel Listing of English Hub Names:**
  - For "User-Defined Identifiers" subject to AI translation (such as class names, interface names, enum names, etc.), it is **mandatory to list the finalized English hub name alongside** the native language name. See the specific description methods below for details.
  - English hub names follow the **English Naming Conventions** defined in `english_specification.md`.
  - The native language notation for User-Defined Identifiers follows the **standard naming conventions** defined in the translation rules for the target language (within `/translation_rules/`).
- **Strict Application of Naming Conventions:**
  - As mentioned above, it is necessary to **strictly apply the standard naming conventions** defined for each respective language to both the native language name and the English hub name.
  - Module names must follow the English naming conventions defined in `english_specification.md`, and ensuring global uniqueness is strongly recommended.
- **Recognition of English Hub Name and Native Name:**
  - For elements listed side-by-side in the definition using the `{English Hub Name}::{Native Name}` format, the AI recognizes **both the English hub name and the native language name as valid identifiers** referring to that element.
- **Cross-Reference:**
  - **Within the Same Module:** Describe the class name, etc., you want to refer to using **only the native language name**. The AI identifies the definition within the module from the context.
  - **Different Module:** If the class, etc., you want to refer to belongs to another module, you **must specify it using the fully qualified name (`ModuleName.ClassName`)**. This also applies when specifying types. (Example: `Creator (com.example.common.User)`).
- **Description Recommendation:**
  - It is **strongly recommended to write descriptions** for each module, section, class, interface, method, property, etc., to clarify their purpose and meaning. This helps AI interpretation and human understanding. Descriptions should be written in the prompt description language.
- **Module Definition (`##`):**
  - All definitions must be written within a module.
  - Format: `## {EnglishModuleName}`
  - Global uniqueness for module names is recommended (see `english_specification.md`).
  - The native language name or detailed description of the module can be written as normal text below the `##` line (optional).
- **Headings (Class `####`, Interface `####`, Section `###`):**
  - **Class/Interface:**
    - Format: `{Heading Level} {Native Name} ({English Hub Name}): {Brief Description}`
    - A **brief description is mandatory**.
    - A **detailed description** can be written as normal text below the heading line (optional).
  - **Section:**
    - Format: `{Heading Level} {Native Name} ({English Hub Name})` or `{Heading Level} {Native Name} ({English Hub Name}): {Description}`
    - The **description is optional**.
  - **When English is the Native Language:** Only `{English Name}` is used, and the parentheses for the English hub name are unnecessary. The rules for descriptions are the same as above.
- **Element Names (Property Name, Method Name, Event Name, Enum Definition Name, Enum Value, Struct Class Definition Name):**
  - The native language name is "primary," and the English hub name is "secondary."
  - Use the English hub name as a **prefix**, connected to the native language name with double colons `::`.
  - Basic format: `{English Hub Name}::{Native Name}`
  - **When English is the Native Language:** Omit the prefix (`{English Hub Name}::`) and write only the English name.
- **Definition of List Format Elements (Properties, Methods, Events, Enums, Structs):**
  - Start the line with a Markdown list hyphen `-`.
  - **Scope of Backticks `` ` ``:**
    - **Properties, Methods, Events:** Enclose the main part of the definition (from immediately after the hyphen up to the type/return type specification).
    - **Enums, Structs:** Enclose only the element name part (the `{English Hub Name}::{Native Name}` or `{English Name}` immediately after the hyphen).
  - Descriptions or value lists are written outside the backticks, preceded by a colon `:` and a space (if required).
- **Property Definition:**
  - Format (Native): `- `{English Hub Name}::{Native Name}: {TypeName}`: {Description}`
  - Format (English): `- `{English Name}: {TypeName}`: {Description}`
  - **Optional Items:**
    - In property definitions, optional items can be indicated by adding `, {Optional Specifier}` after the type name (refer to `core.md` for the term for the optional specifier).
      - Example (Japanese): `- プロパティ名: String, オプション`
      - Example (English): `- propertyName: String, Optional`
- **Method Definition:**
  - Format (Native): `- `{English Hub Name}::{Native Name}({Argument List}): {ReturnTypeName}`: {Description}`
  - Format (English): `- `{English Name}({Argument List}): {ReturnTypeName}`: {Description}`
  - **Return Value:** `Void` can be omitted, but **inclusion is recommended**. Do not add an English hub name to the type name.
  - **Argument List:** Comma-separated `{argumentName}: {TypeName}` or `{argumentName}: {TypeName} = {defaultValue}`. Do not add English hub names to argument names, type names, or default values.
  - **Default Values:**
    - In method definitions, default values can be expressed by adding `= {defaultValue}` after the argument's type name. Only literal values (`True`, `False`, `Null`, numbers, strings) are recommended.
      - Example (Japanese): `- メソッド名(引数名: Number = 0): Void`
      - Example (English): `- methodName(argumentName: Number = 0): Void`
- **Event Definition:**
  - Format (Native): `- `{English Hub Name}::{Native Name}({Argument List})`: {Description}`
  - Format (English): `- `{English Name}({Argument List})`: {Description}`
  - **Return Value:** Usually `Void`, but **omitting the notation is recommended**.
  - Rules for the argument list are the same as for methods.
- **Enum Definition:**
  - Format (Native): `- `{English Hub Name}::{Native Name}`: {Value List}`
  - Format (English): `- `{English Name}`: {Value List}`
  - **Value List:** List comma-separated values in the format `{English Hub Name}::{Native Name}` (or English only).
- **Struct Class Definition (Inferred):**
  - Format (Native): `- `{English Hub Name}::{Native Name}`: {Description}`
  - Format (English): `- `{English Name}`: {Description}`
- **Base Class and Interface Implementation:**
  - As described in `format_common.md`, use the **Basic Terms for the respective language**.
  - **Inheritance:**
    - Format (Japanese Example): `**基底クラス:** {基底クラス名} ({英語基底クラス名})`
    - Format (English Example): `**Base Class:** {BaseClassName}`
  - **Interface Implementation:**
    - Format (Japanese Example): `**インターフェース:** {インターフェース名} ({英語インターフェース名}), ...`
    - Format (English Example): `**Interfaces:** {InterfaceName}, ...`
  - Write **only the native language name** for class names or interface names; do not add the English hub name (multiple can be specified, comma-separated).
- **Type Reference:**
  - When specifying types for properties, arguments, or return values, and referencing user-defined classes or enums, also write **only the native language name**; do not add the English hub name.

#### Output Rules

- When instructed to output in `Definition Format`, the AI **must always enclose the entire OOPD format (Markdown format) output within a code block using \`\`\`**.
- When outputting instance data, output it in **YAML format code block (`---yaml` ... `---`)** as the standard. Other formats like JSON are acceptable if specifically requested by the user.

#### Definition Format Finalization Process

- Typically, the `Definition Format` is generated by the AI based on content created by the user in `User Format`, upon user instruction.
- During generation, the AI automatically checks for compliance with the mandatory rules above (English name parallel listing, naming conventions, module membership, etc.).
- If issues are found during the check (e.g., naming convention violation, unclear English name, module undefined), the AI points out the problems to the user and prompts for correction. The AI may also suggest modifications.
- The `Definition Format` is finalized once the user resolves the issues through interaction with the AI and confirms/approves the content.

```

```Markdown: sources/formats/format_user.md

### OOPD Format: User Format Specification

#### What is the User Format?

The User Format is a flexible and easy-to-write format designed for users to **routinely describe and edit** prompts based on OOPD. It is primarily intended for individual work or use within a session.

#### About This Document

This document (`format_user.md`) explains the rules, characteristics, and recommended usage specific to the User Format. Refer to `format_common.md` for common rules.

#### Key Characteristics and Rules

- **Description Language:** Primarily intended to be written in the user's **native language** (or working language).
- **Omission of English Hub Names:**
  - For parts where `{English Hub Name}::` or `({English Hub Name})` is added in the `Definition Format` (such as class names, interface names, property names, method names, etc.), these **do not need to be written** in the User Format. Describe using only the native language name. The AI internally infers and manages the English hub name.
  - Example (Class Heading): `#### CustomerClass: A class to manage customer information` (OK)
  - Example (Property): `- \`name: String\`: Customer's name` (OK)
- **Headings:**
  - Describing modules (`##`) or sections (`###`) is **not mandatory**. Users can use them to organize definitions as needed.
  - For class (`####`) or interface (`####`) headings, describe the native language name and the description.
  - The AI internally manages definitions based on context or default settings even if modules or sections are not explicitly stated.
- **List Format Elements (Properties, Methods, Events, Enums, Structs):**
  - Start the line with a hyphen `-`.
  - **Use of Backticks `` ` ``:** Backticks are preserved if converted from `Definition Format`. Whether users add backticks when writing by hand is optional, but adding them may improve the AI's interpretation accuracy. When the AI generates User Format as a response, it does not add backticks (for ease of writing).
  - Describe the definition content (properties, methods, etc.) using native language names, types, arguments (native names only), return values (type names only), etc.
- **Naming Conventions:**
  - **Lenient:** As long as the AI can interpret from context, strict adherence to a specific format is not required. Non-standard naming is acceptable if the AI can recognize it.
  - However, following the **standard naming conventions** defined in the translation rules for the target language (within `/translation_rules/`) improves AI interpretation accuracy and facilitates a smoother transition to the `Definition Format`.
  - **AI Confirmation:** If an instructed name deviates from standard naming conventions, the AI may suggest the standard name and ask for confirmation (this confirmation can be turned off via settings).
- **Cross-Reference:**
  - Describe the class name, etc., you want to refer to directly using the native language name. The AI determines it from context but may ask for confirmation if ambiguity arises. When referring to elements in different modules, specifying in the `ModuleName.ClassName` format, similar to `Definition Format`, is recommended.
- **Interaction with AI:**
  - **No Name Specified:** If the user does not specify a name, the AI automatically generates a standard name from context (user confirmation not required).
  - **Confirmation for Non-compliance:** If the name specified by the user does not comply with standard naming conventions, the AI may suggest the standard name and ask for confirmation. (This confirmation behavior can be changed according to user instructions or settings. For example, always applying the standard name without confirmation, or always accepting the user's naming without confirmation, are also possible behaviors).

#### User Format Usage Scenarios

- Creating prompts for personal use, organizing ideas, drafting.
- **Clarifying and refining** definitions through interaction with the AI within a session.
- Temporary prompt instructions.

Definitions created in User Format can be converted and output in `Definition Format` by instructing the AI as needed.

```

```Markdown: sources/localization_overview.md

## OOPD Localization Overview

### Overview

This document explains the basic concepts and strategy for multilingual support (localization) in Object-Oriented Prompt Design (OOPD). OOPD aims to enable users worldwide to design prompts in their native language, interact effectively with AI, and share the definitions they create across language barriers.

### Goals

- **Native Language Description:** Users can, in principle, describe OOPD format (especially `User Format`) in their own native language.
- **Definition Sharing:** OOPD definitions (`Definition Format`) created in different languages can be accurately understood and reused by speakers of other languages and AI.
- **AI Interpretation:** AI can accurately interpret the structure and intent of prompts written in the user's native language.
- **Consistent Translation:** AI maintains consistency in the translation of terms and concepts during internal information processing and response generation.

### Hub Language Model

OOPD adopts **English (`en`) as the hub language** to ensure consistency in translation between multiple languages and internal processing.

1. **Input:** User inputs a prompt in their native language.
2. **Internal Conversion:** AI interprets the "User-Defined Identifiers" within the prompt and internally converts/manages them into the English hub language representation.
3. **Processing:** AI's internal thinking, reasoning, and response generation are performed based on this English hub representation.
4. **Output:** AI translates the generated response from the English hub representation into the output language specified by the user (or the input language) and presents it.

### Terminology Classification and Handling

Terms used in OOPD are classified into two types from a translation perspective (see `core.md`).

- **Basic Terms:** Core concepts defining the structure of OOPD, such as `Class`, `Method`, `Property`. These are **fixed keywords** and are **not translated**. The fixed notation defined for each language is used as is. Standard Types, Extended Types, and Literals are treated similarly and always use their English notation.
- **User-Defined Identifiers:** Class names, interface names, method names, property names, event names, enum definition names, enum values, etc., defined by the user. These are **subject to the translation process** by the AI.

### Translation Process

The AI's translation process is performed based on the following principles and rules:

- **Target:** Only "User-Defined Identifiers" included in the structural definitions within the prompt.
- **Timing:**
  - **Input Interpretation:** Inferring/converting content described in the native language to the English hub language.
  - **Initial Name Determination:** Can infer the optimal English name by referencing descriptions and context.
  - **Response Generation:** Translating from the English hub language to the specified output language. Descriptions are not referenced when translating finalized definitions (for reversibility).
- **Ensuring Consistency (Session Memory):**
  - The AI **remembers the correspondence between User-Defined Identifiers and their English hub names within the session**. *(Refer to `core.md` for the definition of a session)*.
  - If the same User-Defined Identifier (or an expression the AI deems synonymous) appears within the same session, it **must use the remembered English hub name** to prevent translation fluctuations. This takes highest priority.
- **Translation Rules:**
  - Translation is performed based on **naming conventions** and **translation patterns** defined for each language pair. Refer to the respective language rule files (`{language_code}_rules.md`) in the `translation_rules` directory for details.
  - **Cross-lingual Concept Mapping:** For terms representing the same concept in different languages, the AI strives to map them to a common English hub name based on semantic similarity, referencing class definitions, descriptions, and translation rules for each language.
  - **Handling Expression Correspondences (N-to-N, 1-to-N, N-to-1):**
    - **N-to-N (Recommended):** If expressions have different nuances between the hub language and the target language (e.g., `isCompleted` vs. `hasFinished` in the hub language), define corresponding distinct standard translations (`xx_StandardTranslation1` and `xx_StandardTranslation2`) in the target language `xx` whenever possible. This helps maintain the information content across languages.
    - **1-to-N (Caution):** If a single word `TermA` in the hub language can be interpreted in multiple ways (`xx_TranslationB`, `xx_TranslationC`) in the target language `xx` depending on context, translating differently can risk not reverting to `TermA` upon reverse translation. In this case, either define a single most representative standard translation `xx_TranslationB`, or recommend using more specific expressions in the hub language like `TermA_Context1`, `TermA_Context2`.
    - **N-to-1 (Acceptable):** Conversely, if synonyms `TermX` and `TermY` in the hub language are difficult or unnatural to distinguish in the target language `xx`, they may be **aggregated into a single standard translation** `xx_StandardTranslationZ` in the target language.
  - **Standardization from Target Language to Hub Language:** When converting from a target language `xx` to the English hub, if expressions `xx_Expression1` and `xx_Expression2` in the target language refer to the same concept, strive to generate **a single standard English hub name**, such as `HubTermAlpha`. This maintains consistency in expression within the English hub language.
- **Core Translation List:**
  - **Generally Unnecessary.** Basic words are also left to translation based on rules and the AI's language capabilities.
  - **Exceptions:** For a very small vocabulary where notation variations must absolutely be avoided, such as literals (`True`, `False`, `Null` are fixed to English notation), fixed translations are defined exceptionally.
- **Role of AI Inference:**
  - For unknown vocabulary or complex expressions not covered by rules or (exceptional) core lists, the AI **infers** the optimal translation based on context and language knowledge.
  - The AI also adjusts the naturalness of the translation result (e.g., word order, conjugation).
- **Natural Language Parsing Suitability:** Translation rules consider ensuring that the generated target language names become words/phrases easily identifiable by the AI as part of natural language instructions within that language's grammatical structure (e.g., avoiding unnatural particle inclusion).

### Limiting Translation Scope

The AI's translation process is limited to the structural definition parts of the OOPD format (class names, method names, etc.). The **content body (stories, reports, etc.)** that the user asks the AI to generate is **not subject to translation**.

### Regarding Reversibility

OOPD emphasizes that the meaning of definitions should not change between different languages (**semantic reversibility**), especially in the `Definition Format`.

- Since the `Definition Format` lists the English hub name alongside the native name, identity at the hub language level is always guaranteed.
- However, due to the translation rules mentioned above (especially N-to-1 and standardization from target language to hub), note that translating from one language to another and back to the original language **may not guarantee perfect matching at the lexical level (word level)**.
- The goal is purely **"semantic reversibility,"** where the intent and structure of the definition remain unchanged.

### Format and Translation

- **User Format:** Described only in the native language. AI internally infers and manages English hub names.
- **Definition Format:** Lists standardized native language names alongside finalized English hub names. Shareable between languages. This format enables definition conversion between different languages.

### Contribution

Contributions for supporting new languages (creating translation rules) or improving existing rules are welcome. The language files under the `translation_rules` directory are key to the accuracy and quality of translation.

```

```Markdown: sources/translation_rules/README.md

## OOPD Translation Rules Directory

### Overview

This directory (`translation_rules/`) stores files defining **language-specific translation rules** for Object-Oriented Prompt Design (OOPD). These rules are used by the AI to **bidirectionally translate** user-defined "User-Defined Identifiers" (such as class names, method names, property names, etc.) between the hub language, **English (`en`)**, and each supported other language.

These rules are core to OOPD's multilingual support feature and are essential for ensuring consistency between prompts written in different languages and natural expression in each language.

Refer to `localization_overview.md` in the root directory for the overall translation strategy and hub language model.

### Directory Structure and File Naming Convention

- Translation rules for each language are managed as separate Markdown files.
- File names follow the format **`{language_code}_rules.md`**.
  - `{language_code}` uses the 2-letter lowercase language code from **ISO 639-1** (e.g., `ja`, `fr`, `de`). Using regional codes (e.g., `zh_cn`, `pt_br`) connected by an underscore is also considered if necessary.
- Examples:
  - `ja_rules.md`: Japanese translation rules
  - `fr_rules.md`: French translation rules
  - `zh_cn_rules.md`: Rules for Chinese (Simplified)

### Content of Each Language Rule File

Each `{language_code}_rules.md` file must include the following information (refer to existing rule files or templates for details):

1. **Language Code:** Clearly state the language code (`language_code`) the file targets.
2. **English → Target Language Translation Rules:**
   - **Name Conversion Rules** for translating English hub names into the target language (for each element type). This includes naming conventions in the target language (suffixes, etc.).
   - **Translation Patterns** for the target language corresponding to specific English expressions or structures.
   - **Handling of Specific Words/Expressions** to note when translating into the target language.
3. **Target Language → English Translation Rules:**
   - **Name Conversion Rules** for converting target language expressions into English hub names (compliant with standard English naming conventions).
   - **Translation Patterns** for English hub names corresponding to target language expressions or structures.
   - **Handling of Specific Words/Expressions** to note when translating from the target language.
4. **Language-Specific Notes:**
   - Grammar, character encoding, idiomatic expressions, and other considerations specific to the language.

Please structure the rules as much as possible to be easily interpretable by the AI.

### AI Usage

Typically, AI systems do not read these individual language rule files directly. Instead, they utilize a **single combined rule file** (e.g., `ai_combined_translation_rules.md`) generated by automated processes like GitHub Actions. The AI refers to this combined file and applies the appropriate rule set based on the prompt language being processed or the requested output language.

### Contribution

Contributions to expand OOPD's multilingual support by adding translation rules for new languages or improving existing rules are welcome.

- **Adding Rules for a New Language:**
  1. Confirm the ISO 639-1 code for the target language and create a `{language_code}_rules.md` file.
  2. Referencing existing rule files (e.g., `ja_rules.md`), describe the rules according to the "Content of Each Language Rule File" section above. Also, refer to the English specification (`english_specification.md`) and the localization overview (`localization_overview.md`).
  3. Deep knowledge of the target language (preferably native level) is required. Please give sufficient consideration to naming conventions and natural expressions.
  4. Propose via pull requests, etc.
- **Improving Existing Rules:**
  - Modify the target language file (`{language_code}_rules.md`) and propose improvements.

We appreciate your cooperation in developing accurate and natural translation rules.

```

```Markdown: sources/translation_rules/ja_rules.md

### OOPD 日本語 翻訳ルール (Japanese Translation Rules)

**言語コード:** `ja`

#### 英語から日本語への翻訳ルール (Hub (`en`) to Japanese (`ja`))

このセクションでは、英語ハブ名を日本語の翻訳用語に変換する際のルールを定義します。

##### 名称変換ルール (Name Conversion Rules)

以下の規則に従って、英語ハブ名を標準的な日本語名に変換します。

- **原則:**
  - 日本語名は、特定の要素タイプ（クラス、インターフェース、列挙型、イベント）を示す接尾辞を付与します。
  - 助詞「の」は、原則として名詞句の連結には使用しません (例: 「ユーザーの名前」ではなく「ユーザー名」)。
  - メソッド名は、原則として体言止めまたは動詞の名詞形とし、「〜する」は避けます。

- **クラス名 (Class Names):** (`PascalCase`)
  - **標準形式:** `{翻訳された名詞句}クラス` という形式の日本語名に変換します。
  - **定義フォーマット例:** `Customer::顧客クラス`, `OrderHistory::注文履歴クラス`
  - **例 (概念):**
    - `Customer` は `顧客クラス` になります。
    - `OrderHistory` は `注文履歴クラス` になります。
    - `FileManager` は `ファイル管理クラス` になります。

- **インターフェース名 (Interface Names):** (`PascalCase`)
  - **標準形式:** `{翻訳された名詞句/動詞連体形/形容詞}インターフェース` という形式の日本語名に変換します。
  - **定義フォーマット例:** `UserService::ユーザーサービスインターフェース`, `Runnable::実行可能インターフェース`
  - **例 (概念):**
    - `UserService` は `ユーザーサービスインターフェース` になります。
    - `Runnable` は `実行可能インターフェース` になります。
    - `Closable` は `クローズ可能インターフェース` になります。

- **列挙型定義名 (Enum Names):** (`PascalCase`)
  - **標準形式:** `{翻訳された名詞句}列挙型` という形式の日本語名に変換します。 (フラグかどうかの区別は名称では行いません)。
  - **定義フォーマット例:** `TaskStatus::タスク状態列挙型`, `FileAccess::ファイルアクセス列挙型`
  - **例 (概念):**
    - `TaskStatus` は `タスク状態列挙型` になります。
    - `FileAccess` は `ファイルアクセス列挙型` になります。
    - `Color` は `色列挙型` になります。

- **メソッド名 (Method Names):** (`camelCase`)
  - **標準形式:** 原則として `{翻訳された動詞の名詞形/体言止め}` という形式の日本語名に変換します。「〜する」は避けます。
  - **定義フォーマット例:** `getName::名前取得`, `setAge::年齢設定`
  - **パターン例 (概念):**
    - `get{Noun}` パターンは `{名詞}取得` になります (例: `getName` は `名前取得`)。
    - `set{Noun}` パターンは `{名詞}設定` になります (例: `setAge` は `年齢設定`)。
    - `is{State/Condition}` パターンは `{状態/条件}判定` になります (例: `isValid` は `有効判定`, `isConnected` は `接続判定`)。
    - `has{Noun}` パターンは `{名詞}有無確認` になります (例: `hasPermission` は `権限有無確認`, `hasChildNodes` は `子ノード有無確認`)。
    - `can{Action}` パターンは `{行動}可否確認` になります (例: `canExecute` は `実行可否確認`, `canDelete` は `削除可否確認`)。
    - 単純動詞 (`verb`) は `{動詞の体言止め/名詞形}` になります (例: `login` は `ログイン`, `send` は `送信`, `update` は `更新`)。
    - `verb{Noun}` パターンは `{名詞}{動詞の体言止め/名詞形}` になります (例: `updateUser` は `ユーザー更新`, `parseFile` は `ファイル解析`)。

- **イベント名 (Event Names):** (`PascalCase`)
  - **標準形式:** `{翻訳された名詞句/状態変化}イベント` という形式の日本語名に変換します。
  - **定義フォーマット例:** `OrderCompleted::注文完了イベント`, `StatusChanged::状態変更イベント`
  - **例 (概念):**
    - `OrderCompleted` は `注文完了イベント` になります。
    - `StatusChanged` は `状態変更イベント` になります。
    - `InitializationFailed` は `初期化失敗イベント` になります。

- **プロパティ名 (Property Names):** (`camelCase`)
  - **標準形式:** `{翻訳された名詞}` という形式の日本語名に変換します。
  - **定義フォーマット例:** `isEnabled::有効フラグ`, `userName::ユーザー名`
  - **パターン例 (概念):**
    - `is{State}` パターンは `{状態}フラグ` になります (例: `isEnabled` は `有効フラグ`, `isLocked` は `ロックフラグ`)。
    - `has{Noun}` パターンは `{名詞}有無` になります (例: `hasAttachment` は `添付ファイル有無`, `hasError` は `エラー有無`)。
    - `can{Action}` パターンは `{行動}可否` になります (例: `canEdit` は `編集可否`, `canCancel` は `キャンセル可否`)。
    - 通常の名詞 (`noun`) は `{名詞}` になります (例: `userName` は `ユーザー名`, `filePath` は `ファイルパス`, `backgroundColor` は `背景色`)。

- **列挙型の値 (Enum Members):** (`SNAKE_CASE`)
  - **標準形式:** `{翻訳された名詞/状態}` という形式の日本語名に変換します。
  - **定義フォーマット例:** `NOT_STARTED::未着手`, `READ_ONLY::読み取り専用`
  - **例 (概念):**
    - `NOT_STARTED` は `未着手` になります。
    - `IN_PROGRESS` は `進行中` になります。
    - `READ_ONLY` は `読み取り専用` になります。
    - `HIGH_PRIORITY` は `高優先度` になります。
    - `UTF_8` は `UTF-8` (固有名詞はそのまま) になります。

- **構造体クラス定義名 (Struct Class Names):** (`PascalCase`)
  - **標準形式:** `{翻訳された名詞句}クラス` という形式の日本語名に変換します。基本的にクラス名と同じです。
  - **定義フォーマット例:** `Appearance::外見クラス`
  - **例 (概念):** `Appearance` は `外見クラス` になります。

##### 翻訳パターン (Translation Patterns)

(必要に応じて、英語の特定の構文や接辞に対応する日本語の表現パターンをここに記述します。)

- 現時点では特筆すべき共通パターンは名称変換ルールでカバーされているため、省略。

##### 特殊な単語・表現の扱い (Specific Words/Expressions)

(特定の英単語について、文脈によらず固定したい標準訳や注意点があれば記述します)

- `deprecated` は 「非推奨」と翻訳します。
- `experimental` は 「実験的」と翻訳します。
- (必要に応じて追加)

#### 日本語から英語への翻訳ルール (Japanese (`ja`) to Hub (`en`))

このセクションでは、日本語の翻訳用語を英語ハブ名に変換する際のルールを定義します。原則として、`english_specification.md` で定義された英語命名規則に従います。

##### 名称変換ルール (Name Conversion Rules)

- **原則:**
  - 入力された日本語名から、要素タイプ（クラス、メソッド等）に応じた英語命名規則 (`PascalCase`, `camelCase`, `SNAKE_CASE`) に従って英語名を生成します。
  - 日本語名に含まれる助詞「の」は、英語名生成時には基本的に無視します (例: 「ユーザーの名前」は `userName` と解釈)。
  - 日本語名に含まれる標準的な接尾辞（「クラス」「インターフェース」「列挙型」「イベント」）は、英語名生成時には通常含めません（英語側の規則に従う）。

- **クラス名:** (`「{名詞句}クラス」`)
  - **形式:** `PascalCase`
  - **例:**
    - `顧客クラス` は `Customer` になります。
    - `注文履歴クラス` は `OrderHistory` になります。

- **インターフェース名:** (`「{名詞句/動詞連体形/形容詞}インターフェース」`)
  - **形式:** `PascalCase`
  - **例:**
    - `ユーザーサービスインターフェース` は `UserService` になります。
    - `実行可能インターフェース` は `Runnable` になります。

- **列挙型名:** (`「{名詞句}列挙型」`)
  - **形式:** `PascalCase`
  - **例:**
    - `タスク状態列挙型` は `TaskStatus` になります。

- **メソッド名:** (`{動詞の名詞形/体言止め}` 等)
  - **形式:** `camelCase`
  - **パターン例:**
    - `{名詞}取得` は `get{Noun}` になります (例: `名前取得` は `getName`)。
    - `{名詞}設定` は `set{Noun}` になります (例: `年齢設定` は `setAge`)。
    - `{状態/条件}判定` は `is{State/Condition}` になります (例: `有効判定` は `isValid`)。
    - `{名詞}有無確認` は `has{Noun}` になります (例: `権限有無確認` は `hasPermission`)。
    - `{行動}可否確認` は `can{Action}` になります (例: `実行可否確認` は `canExecute`)。
    - `{動詞の体言止め/名詞形}` は `verb` になります (例: `ログイン` は `login`)。
    - `{名詞}{動詞の体言止め/名詞形}` は `verbNoun` になります (例: `ユーザー更新` は `updateUser`)。

- **イベント名:** (`「{名詞句/状態変化}イベント」`)
  - **形式:** `PascalCase`
  - **例:**
    - `注文完了イベント` は `OrderCompleted` になります。

- **プロパティ名:** (`{名詞}` 等)
  - **形式:** `camelCase`
  - **パターン例:**
    - `{状態}フラグ` は `is{State}` になります (例: `有効フラグ` は `isEnabled`)。
    - `{名詞}有無` は `has{Noun}` になります (例: `添付ファイル有無` は `hasAttachment`)。
    - `{行動}可否` は `can{Action}` になります (例: `編集可否` は `canEdit`)。
    - `{名詞}` は `noun` になります (例: `ユーザー名` は `userName`, `背景色` は `backgroundColor`)。

- **列挙型の値:** (`{名詞/状態}` 等)
  - **形式:** `SNAKE_CASE`
  - **例:**
    - `未着手` は `NOT_STARTED` になります。
    - `高優先度` は `HIGH_PRIORITY` になります。
    - `UTF-8` は `UTF-8` になります。

- **構造体クラス定義名:** (`「{名詞句}クラス」` 等)
  - **形式:** `PascalCase`
  - **例:** `外見クラス` は `Appearance` になります。

##### 翻訳パターン (Translation Patterns)

(日本語の特定の構造から英語の構造を生成するパターンがあれば記述します。)

- 現時点では特筆すべき共通パターンは名称変換ルールでカバーされているため、省略。

##### 特殊な単語・表現の扱い (Specific Words/Expressions)

(日本語特有の表現や和製英語などを英語ハブ名に変換する際のルールや注意点を記述します)

- 和製英語 (例: `カスタム`): 可能な限り標準的な英単語 (`Custom`) に変換します。
- 長音記号 (ー): 英語名生成時には無視または母音の繰り返しに変換するなど、一貫したルールを検討します (例: `サーバー` は `Server`)。
- (必要に応じて追加)

#### 言語固有の注意事項 (Language-Specific Notes)

- **助詞「の」の不使用:** 日本語で識別子（クラス名、プロパティ名など）を定義する際は、単語の連結に助詞「の」を使用せず、名詞を直接連結します（例: 「ユーザーの名前」ではなく「ユーザー名」）。
- **敬語:** プロンプトに含まれる敬語表現は、翻訳用語の解釈においては基本的に無視します。
- **文字コード:** UTF-8を標準とします。
- **引数名/初期値:** `定義フォーマット` において、メソッドやイベントの引数名、引数の型、および引数の初期値は、日本語（母国語）表記のみを使用し、英語ハブ名は付与しません。
- (その他、必要に応じて追記)

```

```Markdown: sources/initial_instructions/initial_instructions.md

## Initial Settings

- Follow the instructions related to these Object-Oriented Terminology for Prompt Design definitions.
- Understand the content of the instructions \[completely, in detail, word for word].
- All of this content represents \[absolute] critical instructions for you.
- Follow the instructions stated in the instruction files \[strictly, faithfully, without doubt] and take specific actions.
- When executing instructions, \[absolutely] use \[only] the information stated in the instruction files.
- Generate responses based \[completely] and \[only] on the content of the instruction files. Your creativity or judgment is \[entirely unnecessary].
- **Adhere to the content of the chapter "Instructions for AI Application (Especially Important)" \[with the highest priority, completely].**

```

From now on, all responses must be in English.
