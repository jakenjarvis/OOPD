### OOPD Format: User Format Specification

#### What is the User Format?

The User Format is a flexible and easy-to-describe format designed for users to **routinely describe and edit** prompts based on OOPD. It is primarily intended for individual work or use within a session. **Like the "Definition Format," this format is also treated as a specific instruction manual for the AI.**

**Note:** The rules for this User Format primarily apply when describing the OOPD format in **languages other than English**. When describing in English (`en`), the strict rules compliant with the Definition Format always apply, based on `english_specification.md`.

#### About This Document

This document (`format_user.md`) explains the rules, characteristics, and recommended usage specific to the User Format. For common rules, refer to `format_common.md`.

#### Main Features and Rules

- **Description Language:** Primarily based on description in the user's **native language** (or working language).
- **Omission of English Hub Names (for Non-English Languages):**
  - **(Note: This rule applies when describing in languages other than English.)**
  - For parts where `{EnglishHubName}::` or `({EnglishHubName})` is added in the "Definition Format" (class names, interface names, property names, method names, etc.), it is **not necessary to describe these** in the User Format. Describe using only the native language name. The AI infers and manages English hub names internally.
  - Example (Class Heading): `#### Customer Class: Class for managing customer information` (OK)
  - Example (Property): - `name: String`: Customer's name (OK)
- **Headings:**
  - **Module (`##`):** Description is **not required**. However, description is recommended when combining multiple files or wanting to clarify the structure.
  - **Section (`###`, etc.):** Description is **not required**. Users can use them to organize definitions as needed.
  - **Class (`####`) / Interface (`####`):** Describe the native language name and description text. Co-notation of the English hub name is unnecessary. **If necessary, it is also possible to describe detailed explanations or instructions below the heading.** (Refer to description rules in `format_definition.md`)

        ```markdown
        Example:
        #### Customer Class: Manages customer information

        This class is important and handles customer data.
        Includes personal info, purchase history, contact details, etc.

        Do not output email addresses directly.
        ```

  - **Structure Definition / Enum Definition Group Headings (`####`):**
    - **Can be used optionally**. Use them when grouping structure definitions or enum definitions.
    - Using the fixed name defined in **`basic_terms.md`** (e.g., `#### Structure Definitions`) is **recommended** for the heading name, but not required. Users may use headings they find easy to understand (the AI will attempt to judge from context).
  - **【Important】Placement Constraint:** If a Module definition (`##`) is described, major definition elements like Class definitions, Interface definitions, and Structure/Enum definition group headings **must be placed at a level below that module definition (`###` or lower)**. They cannot be placed at the top level or the same level as the module.
  - Even if modules or sections are not explicitly stated, the AI internally manages definitions based on context or default settings.
- **List Format Elements (Property, Method, Event, Enum, Struct):**
  - Start the line with a hyphen `-`.
  - **List Start Keyword:** Similar to Definition Format, **describing** the corresponding **Basic Term** (see **`basic_terms.md`**, e.g., `Property`, `Method`, `Event`) in bold notation followed by a colon `:` when starting each list is **recommended** (e.g., `**Property:**`). This improves AI interpretation accuracy. However, even if not described or if deviated, the AI attempts to infer the list's content (property, method, etc.) from context and applies it automatically.
  - **Use of Backticks (`\``) (Required):** When describing properties, methods, events, enum definitions, or struct definitions in list format, **must use backticks**.
    - This is for accurate interpretation of the definition part by the AI. Refer to the rules in "Definition Format" (`format_definition.md`) for specific enclosure methods **(pay special attention to the backtick scope for structs and enums)**.
  - Property, method, etc., definitions are described with native language names, types, arguments, return values, etc. (English hub name unnecessary). **Similar to "Definition Format," explanations or instructions can be freely described after the definition or on subsequent lines.** (See `format_definition.md`)

        ```markdown
        Example (Properties and Methods):
        **Property:**
        - `name: String`: Stores the customer's full name.
        - `emailAddress: String`: Email address used for contact.

        **Method:**
        - `calculatePrice(quantity: Number, unitPrice: Number): Number`:
          Calculates the price including tax.
          - Uses an internal fixed value for the consumption tax rate.
          - Returns 0 if quantity is 0 or less.
          - Please round down the calculation result to the nearest integer.
        ```

        ```markdown
        Example (Enum):
        #### Enum Definitions
        - `Task Status = Not Started, In Progress, Completed`: Status of the task.
        - `Color Flag = Red, Green, Blue`: Color flags.
        *(↑ In User Format, no need to attach English hub names to enum names or values)*
        *(↑ Using `=` as separator is recommended, but AI attempts interpretation even with `:`)*
        *(↑ Recommending enclosing up to `= ValueList` with backticks)*
        ```

        ```markdown
        Example (Keywords omitted, AI infers):
        - `name: String`: Stores the customer's full name.
        - `emailAddress: String`: Email address used for contact.
        - `calculatePrice(quantity: Number, unitPrice: Number): Number`: Calculates price including tax...
        - `Task Status = Not Started, In Progress, Completed`
        ```

- **Naming Conventions (Non-English Languages):**
  - **Lenient:** In User Format, it is not necessary to strictly follow the standard naming conventions for the target language (e.g., see `ja_rules.md`), as long as the AI can interpret from context. Naming deviations are acceptable if the AI can recognize them. (**Note:** When describing in English (`en`), the strict naming conventions of `english_specification.md` always apply.)
  - **Recommendation of Standard Rules:** However, following standard naming conventions improves AI interpretation accuracy and smooths the transition to "Definition Format".
  - **Suggestions from AI:** As defined in `interaction_mode_selection.md`, if a name deviating from standard naming conventions is used in User Format, the AI **only suggests** the standard name and does not confirm or automatically apply it.

- **Cross-Reference:**
  - Describe the class name, etc., you want to reference directly using the native language name. The AI judges from context, but may ask for confirmation if ambiguity arises. When referencing elements from different modules, specification in the `ModuleName.ClassName` format, similar to "Definition Format," is recommended.
- **Interaction with AI:**
  - **No Name Specified:** If the user does not specify a name, the AI automatically generates a standard name from context (user confirmation unnecessary).
  - **Confirmation for Non-compliant Rules:** If the name specified by the user does not comply with standard naming conventions, the AI may suggest a standard name and ask for confirmation. (This confirmation behavior can be changed according to user instructions or settings. For example, behaviors like always applying the standard name without confirmation, or always accepting the user's naming without confirmation, are also possible).

#### User Format Usage Scenarios

- Creating prompts for personal use, organizing ideas, drafting.
- **Clarifying and refining** definitions through dialogue with the AI within a session.
- Temporary prompt instructions.

Definitions created in User Format can be converted and output into "Definition Format" by instructing the AI as needed.
