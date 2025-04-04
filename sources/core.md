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
