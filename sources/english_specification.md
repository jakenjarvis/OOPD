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
