## OOPD Format (Object-Oriented Prompt Design Format): Common Specification

### What is the OOPD Format?

The OOPD Format (Object-Oriented Prompt Design Format) is a prompt description format that functions as a common language for effective communication between users and AI. This format leverages concepts from Object-Oriented Programming (OOP) and is designed to be easily understandable for users while enabling the AI to comprehend the prompt's intent more deeply. This allows for the generation of consistent, structured responses.

It not only defines how to describe OOP elements like classes and objects in a Markdown-based, natural language manner but also encompasses prompt instructions in regular Markdown format. It is a flexible format capable of describing both instructions to the AI and structured information. **Crucially, content described in this OOPD format is not merely data definitions or descriptive text; the entire content is interpreted as specific instructions to the AI and constitutes an instruction manual that must be strictly executed. The AI must always be aware of this.**

### About This Document

This document (`format_common.md`) defines the **common basic principles and description rules** for both variations of the OOPD format: "User Format" and "Definition Format". For language-specific rules or differences between formats, refer to their respective specifications (`format_user.md`, `format_definition.md`, translation rules for each language).

### Basic Principles

- **Markdown-based:** Based on Markdown format for readability and ease of description.
- **Leveraging OOP Concepts:** Utilizes OOP concepts like classes, interfaces, properties, and methods as metaphors to structure prompt content. Refer to `core.md` for detailed concept definitions.
- **Mixing Structure and Natural Language:** Allows seamless description of both structured definition parts and natural language explanations or instructions.
- **Character Encoding:** Prompt description and AI interpretation treat **UTF-8** as the standard encoding. This ensures consistency in multilingual environments.

### Prohibition of Collision with Reserved Words (Common to All Languages - Strict Adherence)

Names defined by the user in the OOPD format (module names, class names, interface names, enum names, struct names, method names, property names, event names, argument names, etc.) **MUST NEVER collide with reserved words used by the OOPD system itself.** This is the **most critical rule** to ensure accurate interpretation of prompts by the AI and the consistency of the specification.

**Reserved words** refer to the following, **regardless of the prompt's description language**:

- **All Basic Terms defined in `basic_terms.md`:** This includes not only **English keywords (`Class`, `Property`, etc.) but also the fixed notation keywords defined for all languages (e.g., Japanese `クラス`, `プロパティ`, French `Classe`, `Propriété`, etc.)**.
- **All Standard Types defined in `basic_terms.md`:** e.g., `String`, `Number`, `Boolean`, `List`, `Dictionary`, `Void`, `Any`, etc. (These are always in English notation).
- **All Extended Types defined in `extended_types.md`:** e.g., `ContentString`, `Persona`, `CodeBlock`, `Color`, `Ref`, etc. (These are always in English notation).
- **All Literals defined in `basic_terms.md`:** e.g., `True`, `False`, `Null`. (These are always in English notation).

**【Most Important】This rule strictly applies even if the prompt's description language differs from the language of the reserved word.** That means, regardless of the language you are writing the prompt in, using any reserved word defined in `basic_terms.md` or `extended_types.md` (including those for **all languages**) as a user-defined name is **absolutely prohibited**.

- Example 1: While writing a prompt in **English**, using the Japanese reserved word "`クラス`" or the French reserved word "`Classe`" **as a user-defined name** (e.g., for a class or method) is **not allowed**.
- Example 2: While writing a prompt in **Japanese**, using the English reserved word "`Property`" or the German reserved word "`Eigenschaft`" **as a user-defined name** (e.g., for a property or event) is **not allowed**.

**Instructions for AI:**

- When interpreting prompts, the AI **must always verify** that user-defined names do not collide with any of the reserved words listed above (including Basic Terms for all languages), **regardless of the description language**.
- If a user attempts to use the same name as a reserved word, the AI **must clearly point it out as an error** and **require** the user to use a different name. It is desirable to indicate which language's reserved word it conflicts with (e.g., "'プロパティ' cannot be used as a method name because it is a Japanese reserved word").
- When the AI itself generates responses or definitions, it **MUST NEVER use reserved words as user-defined names.**

Violation of this rule can corrupt the prompt's intent and cause unpredictable behavior, and is therefore **absolutely unacceptable.**

### Markdown Notation and Structure

- **Heading Levels:** Use Markdown headings (`#`, `##`, `###`, `####`, etc.) to represent the hierarchical structure of definitions.
  - `##`: Used for **Module** definitions. The top-level container for OOPD definitions. Global uniqueness for module names is recommended (see `english_specification.md`). **(Refer to `basic_terms.md` for the Basic Term definition of `Module`)**
  - **Section:** Defined using Markdown headings (`###`, `####`, `#####`, etc.). An optional structural grouping (chaptering) within a module for document organization. Nesting (multiple levels) is possible. **Sections do not affect name resolution or references, but they do affect the scope of instruction application for the AI (see `core.md`).** Heading text is free-form (usually in the prompt description language).
  - `####`: Used for defining **individual Classes** or **individual Interfaces**. Headings at this level typically contain the name of the class or interface being defined (e.g., `#### MyClassName`). **(Refer to `basic_terms.md` for the Basic Term definitions of `Class`, `Interface`)**
  - `####`: Also used as a **fixed heading name for grouping Structure definitions**. This heading name MUST use the fixed name defined as a **Basic Term** in **`basic_terms.md`** (`Structure Definitions` / `構造体定義`, etc.). Individual struct definitions are described under this heading in list format (`-`).
  - `####`: Also used as a **fixed heading name for grouping Enum definitions**. This heading name MUST use the fixed name defined as a **Basic Term** in **`basic_terms.md`** (`Enum Definitions` / `列挙型定義`, etc.). Individual enum definitions are described under this heading in list format (`-`).
  - Heading numbers (e.g., `1.`, `1.1`) may or may not be included. The AI recognizes structure by heading level and text, not numbers.

- **Element Definition Keywords:** Element groups within classes or interfaces, such as properties, methods, and events, are indicated by the **Basic Terms defined in `basic_terms.md`** (`Property`, `Method`, `Event`, etc.) in **bold notation**. A colon (`:`) follows the keyword.
  - Example (Japanese): `**プロパティ:**`, `**メソッド:**`, `**イベント:**`
  - Example (English): `**Property:**`, `**Method:**`, `**Event:**`
    *(Note: While plural forms might be conventional in English etc., the singular Basic Term is used as the keyword)*

- **Lists:** Use bulleted lists (`-`) to define properties, methods, events, enum definitions, struct definitions, etc.
  - List items MUST start with exactly one half-width hyphen (`-`), followed by one half-width space.
  - Note: Never use other Markdown list markers (e.g., `*`, `+`). These are considered OOPD format violations.

- **Code Blocks (` ``` `):** When embedding code examples or data examples (YAML, JSON, etc.) within the document, enclose them with triple backticks (` ``` `). This is to distinguish them from the code block (`~~~`) that the AI uses to enclose the entire "Definition Format".

  ````
  ```markdown
  Example:
  ```yaml
  instanceData:
    name: Example
    value: 123
  ```
  ```
  ````

- **Table Notation:**
  - Tables are useful for comparisons, but list format is better suited for complex structural information for AI interpretation and consistent processing.
  - Therefore, **using tables for structural representation in AI-generated OOPD format is discouraged**; prioritize list formats, etc.
  - **However, if a user uses a table within a prompt, the AI should respect and interpret that structure. Retaining it without forced conversion during response generation is recommended.**

### Notation for Types and Literals (Common to All Languages - Unified English Notation)

When specifying types for properties, arguments, return values, etc., or describing specific literal values within the OOPD format, **use the following standard English notations, regardless of the prompt's description language**. These notations are treated as **Basic Terms** and are not translated (**Refer to `basic_terms.md` for definitions**).

- **Standard Types:**
  - `String`, `Number`, `Boolean`, `List`, `Dictionary`, `UniqueID`, `Instant`, `Void`, `Any`

- **Extended Types:**
  - `ContentString`, `Instruction`, `Persona`, `OutputStyle`, `CodeBlock`, `Ref`, `SchemaDefinition`, `JsonString`, `YamlString`, `XmlString`, `Color`, etc.
  - (Refer to `extended_types.md` for details on extended types)

- **Literals:**
  - `True`, `False`, `Null`
  - (Numeric literals, string literals can also be used normally)

- **Type Specification Notation (within list items):**
  - Property: `{propertyName}: {TypeName}`
  - Method argument: `{argumentName}: {TypeName}` or `{argumentName}: {TypeName} = {defaultValue}`
  - Method return value: `): {ReturnTypeName}`
  - Type parameters for lists or dictionaries: Use `< >` (e.g., `List<String>`, `Dictionary<String, Number>`).

### Text Handling and Comment Rules (Strict Adherence)

The OOPD format consists of structured definitions and accompanying natural language text (explanations or instructions). Adhere strictly to the following rules regarding text handling:

- **Text within Definitions (Descriptions/Instructions - Allowed):**
  - **Description texts** for classes, methods, properties, etc., and **instruction texts for the AI** concerning specific elements that were part of the original prompt, are important information holding meaning as part of the OOPD format definition. These should be **described as regular Markdown text** near the relevant definition (e.g., under the heading, after the definition). The AI interprets these and uses them for response generation. These **do not fall under prohibited comments.**
  - **【Most Important Check Item - Strict Obligation】To keep description texts clearly as natural language and facilitate AI translation and interpretation, the use of inline backticks (`\``) and co-notation of English names within description texts is absolutely prohibited for any reason whatsoever.**
    - This is a most critical rule where violations have been repeatedly confirmed in the past, and the AI must recognize this rule violation as its own critical flaw and absolutely avoid it.
    - Even when explaining specific keywords (literals) like True, False, or Null within the Definition Format's description text, do not use inline backticks to highlight them as code snippets or special terms. (see `format_definition.md`)
    - When referring to other definition elements or specific terms, describing them as regular text is recommended.
    - (e.g., `True`, `False`, `Null`, `{nativeName}`, `(englishName)`, `{englishName}::{nativeName}`)
  - Description texts should, in principle, be unified in the prompt's description language. Avoid unnecessary mixing of languages unless there is a clear intent, such as quoting.
  - (Refer to `format_definition.md` for strict rules in the Definition Format.)

- **Explanatory Comments by AI (Prohibited):**
  - Annotative text or symbols added by the AI **within** the OOPD format Markdown code block (`~~~`) **to explain modifications or points of caution to the user** (regardless of format, e.g., `# Change`, `// Note`, `<!-- Correction -->`, etc.) are **absolutely prohibited**.
  - These AI explanations are not part of the OOPD format (the instruction manual for the AI) itself and only serve as noise that can mislead the AI's interpretation of instructions.
  - If the AI needs to provide explanations to the user, it must always describe them **outside** the OOPD format code block (`~~~`) (before or after the code block).

- **User Memo Comments (HTML format - AI Ignores/Maintains):**
  - Users can use HTML-style comments (`<!-- comment content -->`) for personal notes, etc.
  - The AI must **completely ignore** blocks enclosed in `<!-- ... -->`, not interpret them, and **maintain them as is without modification** (prohibited to delete/change).
  - The AI **MUST NEVER use this HTML format** when generating its own responses or explanations.
