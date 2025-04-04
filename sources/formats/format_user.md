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
