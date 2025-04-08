### OOPD English Specification

#### Introduction

This document defines the **specifications and guidelines** for describing prompts in **English (`en`)** and for the AI to interpret and respond to them within the Object-Oriented Prompt Design (OOPD) framework. As English is the **hub language** of OOPD and serves as the baseline for translation with other languages, its specification is particularly important.

For common basic principles and description rules applicable to other languages, refer to `core.md`, `format_common.md`, and **`basic_terms.md`**.

#### Basic Principles

**Important:** The following principles are **absolute rules** for describing the OOPD format in English (`en`) and for the AI interpreting and responding to it. The flexibility of the "User Format" described in other documents (see `format_user.md`) and the "Interaction Mode Selection" process (see `interaction_mode_selection.md`) **do not apply at all** to interactions in English.

- **Hub Language:** English (`en`) is the hub language of OOPD. All User-Defined Identifiers are internally mapped to English hub names.
- **Single Format (Definition Format Only Applied):** When describing the OOPD format in English, the **conceptual distinction** between "User Format" and "Definition Format" found in other languages **does not exist; descriptions must always comply with the rules defined in `format_definition.md`**. Therefore, the lenient rules described in `format_user.md` (e.g., allowing deviations from naming conventions, proposing standard names only) **do not apply to English**.
  - This means Module definitions (`##`) are mandatory.
  - **【Important】Placement Constraint:** Major definition elements such as Class definitions, Interface definitions, and group headings (`#### Structure Definitions`, `#### Enum Definitions`) **MUST be described at a level below the Module definition (`##`) (i.e., `###` or lower).**
  - Defined elements (classes, methods, etc.) must **strictly adhere** to the **English Naming Conventions** described later. If naming conventions are violated, the AI will point out the violation and **automatically apply the standard English name after notifying** the user. Unless the user corrects the name, the AI will continue to use the standard name internally.
- **Skipping Format Confirmation:** Based on the "Single Format" principle above, the AI **does not execute** the format confirmation procedure defined in `interaction_mode_selection.md` when starting a conversation in English.
- **No Translation Processing:** If the input prompt is in English and the output is also specified as English, translation processing between the hub language does not occur. The AI directly interprets English definitions and responds in English.
- **Omission of Hub Name Prefix:** When describing in English, it is **not necessary** to prefix element names (properties, methods, etc.) with `{English Hub Name}::`. Describe only the English name.
- **No Co-notation of Other Languages:** It is **not necessary** to co-notate names in other languages using parentheses `()` or similar in headings, etc.

#### Prohibition of Collision with Reserved Words (Most Important)

**Important:** Even when describing the OOPD format in English, user-defined names (module names, class names, method names, property names, etc.) **MUST NEVER collide with OOPD reserved words.** This is the **most critical rule common to all languages**, defined in detail in `format_common.md`, and must be strictly observed, especially when describing in English (the hub language).

**Reserved words** primarily include the following ( **For the complete definition of reserved words that are prohibited from collision and the strict rules for their application across all languages, MUST refer to the "Prohibition of Collision with Reserved Words" section in `format_common.md`** ):

- **Basic Terms** (see `basic_terms.md`): Examples include `Class`, `Property`, `Module`, `baseclass`, `Optional`, etc.
- **Standard Types** (see `basic_terms.md`): Examples include `String`, `Number`, `Boolean`, `List`, `Void`, `Any`, etc.
- **Extended Types** (see `extended_types.md`): Examples include `ContentString`, `Persona`, `CodeBlock`, `Color`, `Ref`, etc.
- **Literals** (see `basic_terms.md`): Examples include `True`, `False`, `Null`.

**Note:** As defined in `format_common.md`, this rule includes **fixed keywords of all languages** listed in `basic_terms.md`.

The AI, when encountering user attempts to use these reserved words (all reserved words based on the definition in `format_common.md`) as identifiers, **MUST issue a warning** and prompt the user to use a different name. The AI itself **MUST NEVER generate these reserved words as user-defined names.** This is the **most important rule** to eliminate ambiguity and ensure accurate interpretation of the specification.

#### English Naming Conventions

When describing the OOPD format in English, **strictly apply** the following naming conventions. The AI will also interpret prompts and generate responses/definitions based on these rules.

- **Module Names:**
  - **Format:** Dot (`.`) separated hierarchical structure. **Lowercase** is recommended overall.
  - **Components:** Each hierarchy element name can use **alphanumerics (a-z, 0-9)** and **hyphen (`-`)**, **underscore (`_`)**.
  - **Period:** Used only as a hierarchy separator, not within element names.
  - **Uniqueness:** Reverse domain name (`com.example.project`) or `io.github.username.project` format is strongly recommended to ensure global uniqueness.
  - **Examples:** `com.example.task_management`, `io.github.username.my_utils`
- **Section Names:**
  - **Format:** Free-form text. No special naming rules or character restrictions. Descriptive English text suitable for a document structure heading is recommended.
  - **Examples:** `### Core Functionality`, `### Helper Classes`
- **Class Names:**
  - **Format:** `PascalCase`. Capitalize the first letter of each word and concatenate.
  - **Examples:** `UserProfile`, `TaskItem`, `HttpRequestHandler`
- **Interface Names:**
  - **Format:** `PascalCase`. Same as class names. (Do not use `I` prefix).
  - **Examples:** `UserService`, `Runnable`, `ShapeRenderer`
- **Enum Names:**
  - **Format:** `PascalCase`.
  - **Examples:** `OrderStatus`, `ColorMode`, `FileAccessLevel`
- **Method Names:**
  - **Format:** `camelCase`. The first word is lowercase, subsequent words start with an uppercase letter and are concatenated.
  - **Getters:** `get` prefix recommended (e.g., `getName()`, `getTotalPrice()`).
  - **Setters:** `set` prefix recommended (e.g., `setName(name: String)`, `setPriority(priority: Priority)`).
  - **Boolean returning:** Prefixes like `is`, `has`, `can` recommended (e.g., `isValid()`, `hasChildren()`, `canExecute()`).
  - **Other actions:** Recommended to start with a verb representing the action (e.g., `calculateArea()`, `sendNotification()`, `updateDatabase()`).
- **Property Names:**
  - **Format:** `camelCase`.
  - **Boolean:** Prefixes like `is`, `has`, `can` recommended (e.g., `isEnabled`, `hasErrors`, `canModify`).
  - **Others:** Usually nouns or noun phrases (e.g., `firstName`, `orderCount`, `backgroundColor`).
- **Event Names:**
  - **Format:** `PascalCase`. Often past tense or noun forms indicating event occurrence.
  - **Examples:** `ButtonClick`, `StatusChanged`, `DownloadComplete`, `InitializationFailed`
- **Enum Members:**
  - **Format:** All uppercase `SNAKE_CASE`. Separate words with underscores (`_`).
  - **Examples:** `NOT_STARTED`, `IN_PROGRESS`, `COMPLETED`, `LOW`, `MEDIUM`, `HIGH`, `READ_ONLY`
- **Struct Names:**
  - **Format:** `PascalCase`. Same as class names.
  - **Examples:** `Appearance`, `Coordinate`
- **Constant Names (Reference):**
  - **Format:** All uppercase `SNAKE_CASE`. Same as enum members.
  - **Examples:** `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT`
- **Variable/Parameter Names (Reference):**
  - **Format:** `camelCase`. Same as method or property names.
  - **Examples:** `userName`, `itemIndex`, `targetUrl`

#### Notation for Types and Literals

Standard types defined in `basic_terms.md`, literals, and extended types defined in `extended_types.md` are always used with their **English notation**.

- **Type Examples:** `String`, `Number`, `Boolean`, `List<String>`, `Dictionary<String, Any>`, `UniqueID`, `Instant`, `Void`, `Any`, `ContentString`, `Persona`, `CodeBlock`, `Ref`, `Color`, etc.
- **Literal Examples:** `True`, `False`, `Null`

#### Structure and References

- **Module (`##`):** All definitions are described within a module.
- **Section (`###`, etc.):** Can be used optionally for organizing document structure. Does not affect reference paths.
- **Heading (`####`):**
  - **Individual Class/Interface:** Format `#### ClassName: Description` or `#### InterfaceName: Description` (brief description required).
    - Detailed description can be written below the heading.
  - **Group Heading:** Use `#### Structure Definitions` or `#### Enum Definitions`. These are fixed English names defined in **`basic_terms.md`**.
    - Detailed description can be written below the heading.
- **List Format Elements (`-`):** Define properties, methods, events, enums, structs.
  - **List Start Keyword:** When starting a list, use the corresponding Basic Term defined in **`basic_terms.md`** (`Property`, `Method`, `Event`) in bold notation (e.g., `**Property:**`, `**Method:**`, `**Event:**`).
  - **Property:** - \`propertyName: Type\`: Description (add `, Optional` if optional. See `basic_terms.md` for `Optional`)
  - **Method:** - \`methodName(argName: Type = defaultValue): ReturnType\`: Description (omitting ReturnType is not recommended even if `Void`)
  - **Event:** - \`eventName(argName: Type)\`: Description (omitting ReturnType is recommended if `Void`, `()` required even with no arguments)
  - **Enum:** - \`EnumName = VALUE\_ONE, VALUE\_TWO, ...\` \[: Description] (List format, describe under `#### Enum Definitions`. Separator is `=`, backticks cover up to the value list)
  - **Struct:** - \`StructName\`: Description (List format, describe under `#### Structure Definitions`)
- **Base Class / Interface Implementation:**
  - Within the class definition, use the corresponding Basic Term (see **`basic_terms.md`**) in bold notation.
  - **Inheritance:** `**baseclass:** BaseClassName`
  - **Interface Implementation:** `**Interface:** InterfaceName1, InterfaceName2, ...`
- **Cross-Module Reference:** When referencing definitions in other modules, always use the fully qualified name (`module.name.ClassName`).

#### Instructions for AI

- When interpreting OOPD format prompts written in English, strictly apply the naming conventions and structural rules above.
- If the user describes something violating the naming conventions, point it out and prompt for correction.
- Strictly adhere to the **Prohibition of Collision with Reserved Words** rule, and warn the user if they attempt to use a reserved word. The AI itself must not use reserved words as identifiers.
- When generating responses in English, also follow the naming conventions and format rules above. The `{English Hub Name}::` prefix for element names is unnecessary.
- In situations requiring cross-module references, if the user does not use the fully qualified name, confirm which module's definition is intended, or supplement with the most likely one based on context (however, prioritize confirmation if ambiguity remains).
