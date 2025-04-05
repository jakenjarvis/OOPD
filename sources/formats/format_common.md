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
  - List elements must start with a single hyphen (`-`) followed by exactly one space.
  - Caution: Do not use other Markdown list symbols (e.g., `*`, `+`). These are considered violations of the OOPD format.

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
