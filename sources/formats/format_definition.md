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
    - **Properties, Methods, Events:** Enclose the main part of the definition (from immediately after the hyphen up to the type/return type specification) **only**.
    - **Enums, Structs:** Enclose only the element name part (the `{English Hub Name}::{Native Name}` or `{English Name}` **only**).
      - Start: After a hyphen (`-`) and a single space. Right before the element definition.
      - End: Right after the element definition, before the colon (`:`), and a space. Do not enclose the colon and description in backticks.
      - The value list of enums are not enclosed in backticks.
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
