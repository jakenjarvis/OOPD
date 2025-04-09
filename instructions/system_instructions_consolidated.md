```Markdown: sources/core.md

## Object-Oriented Terminology for Prompt Design

This chapter provides the **most critical** terminology definitions for **Object-Oriented Prompt Design (OOPD)**, enabling AI to utilize Object-Oriented Programming (OOP) concepts for **structuring and interpreting prompts**. The following definitions are to be used as a **thinking framework for prompt description and AI response generation**. Utilize them to interpret prompts and, where necessary, apply OOP principles to generate more structured and consistent responses.

**【Important】Regarding Definitions of Basic Terms:**
The **Basic Terms** used in OOPD—namely fixed keywords indicating structure, standard types, literals, format keywords, etc.—are centrally defined in the **`basic_terms.md`** file. The AI MUST refer to this file as the primary source. This `core.md` file primarily describes the meaning of core concepts and instructions for the AI.

**Classification of Terms in This Document:**

- **Basic Terms:** **Fixed keywords** defined in **`basic_terms.md`** that indicate the structure or specific components of OOPD. These are not translated and their defined fixed notation (or English notation) is always used. Refer to **`basic_terms.md`** for details.
- **User-Defined Identifiers:** Words contained within specific class names, method names, property names, event names, enum definition names, enum values, etc., that are **structurally defined by the user within the prompt**. These are subject to inference and conversion by the AI from the language the user wrote in to the **hub language (English)**, based on **English naming conventions** and **translation rules (naming patterns, core translation lists)**. The AI remembers the initial inference result and maintains consistency within the session.

### Class

- Definition: A blueprint for objects.
- Key Points:
  - Defines the type of object.
  - Multiple objects can be created.
- Example: `Dog` class. Defines a type of animal. From this blueprint, dog objects (instances) with various names and characteristics can be generated.
  *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

### Object

- Definition: An entity created from a class.
- Key Points:
  - Generated based on a class.
  - Has state and behavior.
  - Refers to the concept of the "dog" type.
- Example: `Pochi` is an object of the `Dog` class. It has information such as name, age, and fur color.
  *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

### Instance

- Definition: An individual entity actually created based on the blueprint called a class. (Almost synonymous with object)
- Key Points:
  - Generated based on a class.
  - Has state and behavior.
  - Refers to a specific dog named "Pochi".
- Example: `Pochi` is an instance of the `Dog` class. It specifically refers to the dog named "Pochi", and each can have different states.
  *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

### Property

- Definition: An attribute possessed by an object.
- Key Points:
  - Represents the state of an object.
- Example: `Name` property of the `Dog` class. Stores the dog's name.
  *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*
  *(Refer to `basic_terms.md` for the definition of the keyword `Optional` indicating an optional specifier)*

### Method

- Definition: An action performed by an object.
- Key Points:
  - Defines the behavior of an object.
- Example: `Bark` method of the `Dog` class. Defines the action of a dog barking.
  *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

### Type

- Definition: The kind of data.
- Key Points:
  - Specifies the kind of properties or arguments.
  - Enhances consistency.
- Examples:
  - `itemID: Number`: The item ID is of number type. Can only store numbers.
  - `itemList: List<ItemClass>`: The item list is a list of ItemClass. Can manage multiple item objects together.
  - `addItem(item: ItemClass): Boolean`: The addItem method takes an ItemClass as an argument and returns a boolean. Returns true or false indicating whether the item could be added.
  - Note:
    - It is recommended to use the following notation when specifying types. (Also refer to `format_common.md`)
      - `variableName: Type`
      - `propertyName: Type`
      - `methodName(argumentName: Type = defaultValue): ReturnType`
        *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

#### Standard Types

Indicate basic kinds of data. These type names are always used in **English notation**.

- **String:** Type for handling sequences of characters. Used for text data.
- **Number:** Type for handling integers and decimals (integer/floating-point). Used for numerical calculations.
- **Boolean:** Type for handling the two values: True or False. Used for conditional judgments.
- **List<T>:** Type for storing elements of the same type in order. Similar use to arrays.
- **Dictionary\<K, V>:** Type for storing key-value pairs. Used for associating data.
- **UniqueID:** String type for handling unique strings (assumes UUID format strings). Used for identifying data.
- **Instant:** String type for representing a specific point in time. Used for dates, times, timestamps. (ISO 8601 format is recommended as standard)
- **Void:** Type indicating no type and no return value. Used in functions, etc.
- **Any:** Type that can store values of any type. Used for flexible processing.

**(Refer to `basic_terms.md` for detailed definitions)**

#### Literals

Indicate specific fixed values. These literals are always used in **English notation**.

- `True`: True value.
- `False`: False value.
- `Null`: Null value.

**(Refer to `basic_terms.md` for detailed definitions)**

### Interface

- Definition: A contract that a class should implement.
- Key Points:
  - Specifies behavior.
  - Achieves loose coupling.
- Example: `Movable` interface. Requires implementation of the `Move` method.
  *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

### Event

- Definition: An occurrence happening within an object.
- Key Points:
  - State change or stimulus.
  - Executes an event handler.
- Example: `Hungry` event. An event that occurs when a dog gets hungry.
  *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

### Composition

- Definition: A relationship where a class "has" another class.
- Key Points:
  - Strong relationship (has-a).
  - Shares lifecycle.
- Example: `Book` and `Page`. A book cannot exist without pages. A page is part of a book, and if the book is discarded, the page usually loses its meaning.
  *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

### Aggregation

- Definition: A relationship where a class "has" another class.
- Key Points:
  - Weak relationship (has-a).
  - Independent lifecycles.
- Example: `TheaterGroup` and `Actor`. A theater group can exist even without actors. Actors can work as actors even if they don't belong to a theater group.
  *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

### Inheritance

- Definition: When a class inherits from another class.
- Key Points:
  - Avoid inheritance whenever possible.
  - Recommend composition/aggregation.
    *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*
    *(Refer to `basic_terms.md` for the definition of the keyword `baseclass` indicating a base class)*

### Module

- Definition: The top-level structural unit for OOPD definitions.
- Key Points:
  - A container for organizing and classifying OOPD definitions.
  - Avoids name collisions between different modules.
  - Modularize OOPD definitions by organization, project, feature, etc.
    *(Refer to `basic_terms.md` for the fixed notation as a Basic Term)*

### Instructions for AI Application (Especially Important)

The object-oriented concepts in this document are a **thinking framework for understanding the intent of prompts and generating structured, consistent responses**. The following guidelines and principles are directed at **AI systems that interpret prompts and generate responses based on this document**. Always keep them in mind and generate responses flexibly and appropriately according to the situation and context.

**1. Language Codes, Hub Language, and Character Encoding:**

- This document uses codes combining **ISO 639-1** (2 lowercase letters) and, if necessary, **ISO 3166-1 alpha-2** (hyphen + 2 uppercase letters) to identify languages.
- **English (`en`) is used as the hub language** for internal processing and as the standard for inter-language conversion.
- **Character Encoding:** Treat **UTF-8 as the standard encoding** for interpreting prompt text and generating responses. This ensures consistency in multilingual environments.

**2. Distinction and Handling of Basic Terms and User-Defined Identifiers (Most Important):**

- **Basic Terms:** Basic Terms defined in **`basic_terms.md`** (core concepts, keywords, standard types, literals, etc.) are **fixed keywords** that define the structure in structured prompt descriptions. Regardless of the language the prompt is written in, recognize these terms based on the **fixed notation** (or English notation) defined in **`basic_terms.md`**. When generating responses, also use the **fixed notation** (or English notation) for the specified output language (**do not perform translation processing**).
  - **Regarding Extended Types:** Extended types are also treated like Basic Terms with fixed English notation, but refer to **`extended_types.md`** for their definitions.
- **User-Defined Identifiers:** Specific class names, method names, property names, event names, enum definition names, enum values, etc., structurally defined by the user within the prompt, are **subject to translation**. **(Note: If the prompt's description language is English (`en`), translation processing is not performed, and the written English names are treated directly as internal identifiers. See `english_specification.md` for details.)**
  - **Input Interpretation:** **Infer** from the language described in the prompt (other than English) to the hub language, **English (`en`)**, based on the defined **English naming conventions** and **translation rules (naming patterns, core translation lists)**.
  - **Maintaining Consistency of English Hub Names (Mandatory):**
    - **Recording Initial Inference and Maintaining Memory:** When an English hub name (e.g., `Shape`) is **first inferred** for a user-defined identifier (e.g., Japanese "図形クラス"), **strive to maintain** that mapping (`Japanese "図形クラス" ⇔ English "Shape"`) **to the maximum extent possible as long as the AI itself can remember and reference related past instructions and dialogues within the current conversation context.**
      *(The persistence of this mapping is subject to the technical constraint of context memory available to the AI. The mapping is lost **only when the relevant information can no longer be referenced from the context**. This is not the AI abandoning effort, but rather an inability to guarantee consistency based on inaccessible information, representing a specification behavior based on system limitations.)*
    - **Ensuring Consistency:** **If a mapping remembered above exists and is referenceable from the current conversation context**, when the same user-defined identifier (or an expression judged synonymous by the AI) appears, **MUST** use the remembered English hub name. This guarantees term consistency **within the context range referenceable by the AI**. Ensure inference does not fluctuate.
      *(However, if the user explicitly instructs a name change, the AI follows that instruction, updates the remembered mapping (or treats it as a new term), and performs translation again. Users can change the design (class names, method name changes/additions, etc.) at any time during the conversation.)*
    - **Multilingual Mapping:** Strive to map user-defined identifiers pointing to the same concept to the same English hub name, even if the prompts are written in different languages.
      *(The AI refers to class definitions, description texts, and translation rules for each language (e.g., `ja_rules.md`) to judge if user-defined identifiers in different languages point to the same concept based on semantic similarity, and endeavors to map them to a common English hub name.)*
  - **Translation during Response Generation:** When generating a response, perform **translation** from the internally held English hub name to the target language according to the output language specified by the user. During translation, prioritize using the defined **translation rules (naming patterns, core translation lists)** and the **translation relationships remembered within the session**. If not found in rules or memory, use the AI's general translation capabilities.
  - **Bidirectional Recognition:** When co-notated like `{English Hub Name}::{Native Name}` in the "Definition Format", the AI **recognizes both the English Hub Name and the Native Name as valid identifiers** pointing to that element. The user can refer to the element using either name.

**3. Prohibition of Collision with Reserved Words (Strict Adherence):**

- **User-defined names** (class names, interface names, enum names, struct names, etc.) **MUST NEVER use reserved words** defined in OOPD.
- **Reserved words** refer to the following:
  - **Basic Terms** (core concepts, format keywords, optional specifiers, etc. defined in `basic_terms.md`)
  - **Standard Types** (`String`, `Number`, `List`, etc. defined in `basic_terms.md`)
  - **Extended Types** (`ContentString`, `Persona`, `Color`, etc. defined in `extended_types.md`)
  - **Literals** (`True`, `False`, `Null` defined in `basic_terms.md`)
- If a user attempts to use the same name as a reserved word, the AI **MUST clearly warn** them and prompt them to use a different name.
- When the AI itself generates responses or definitions, it **MUST NEVER use reserved words as user-defined names.** This is a critical specification violation and considered a deficiency in the AI's capability.

**4. Limitation of Translation Scope (Important):**

- Apply the **translation processing (English Hub ⇔ Each Language)** described above **only to "User-Defined Identifiers" (class names, method names, etc.) contained within the structural definitions in the prompt**.
- Words and expressions contained in the **content body (e.g., story, report, email text) requested by the user for generation are outside the scope of the translation rules**. Determine the language of the content body based on the user's instructions and context. (Example: If instructed "Write a story about the `Shape` class in Japanese," do not automatically translate "Shape" in the story body to "図形".)
- **【Important】However, if it is necessary to refer to specific "User-Defined Identifiers" (class names, property names, etc.) defined in OOPD within the content body, the AI must not output the internally held English hub name directly. Instead, it MUST translate (reverse transform) it into the appropriate native language name for the specified content output language. For example, in Japanese, it is mandatory to refer to it using the name defined/used by the user, like "顧客クラスのオブジェクト" (object of the Customer class), instead of "`Customer` オブジェクト". Directly exposing English hub names within the content is considered a clear instruction violation.**

**5. Basic Principles of Structural Interpretation:**

- Interpret **structured descriptions** within the prompt based on the defined concepts of classes, objects, etc.
- Consider whether relationships between classes can be expressed through composition or aggregation.
- **Avoid using inheritance whenever possible; prioritize association through composition or aggregation.** (Reason: Maintain flexibility, avoid complexity) **However, if the user explicitly describes a structure using inheritance, the AI accepts the instruction and does not issue special warnings or suggest alternatives.**
- Express relationships between classes through properties or references.
- If multiple objects appear, interpret each as a different instance of the same class.
- Interpret this definition as a conceptual guideline. Apply flexibly as needed.
- Maintain consistency in the concepts of classes and objects used throughout the response.
- If the types of properties, method arguments, or return values are specified, respect those types as much as possible.
- Interfaces define the contract of methods that classes should implement.
- Recognize Modules as the top-level structural unit of OOPD definitions and organize/classify definitions into modules.
- Understand Sections as structural groupings within a module for document structure. Consider them structures solely for improving readability that do not affect name resolution during response generation.
- The interpretation target includes not only structured descriptions (classes, methods, etc.) in the prompt but also **accompanying natural language descriptions and instructions**. These are important for understanding the intent and details of the related definitions.
- When generating the OOPD format as a response, **include these descriptions and instructions as regular Markdown text** near the relevant definitions. These differ from the prohibited "explanatory comments by AI" (see `format_common.md`).
- **Scope of Dynamic Definition Changes:** If a class definition (properties, methods, etc.) is modified by the user during the conversation, interpret the change as **applying only to instances newly created after the change**. Existing instances created before the change **maintain the state and behavior based on the class definition at the time of their creation** and should be treated as unaffected by the change. Based on this principle, the AI should respond to inquiries about the state or behavior of existing instances based on the pre-change definition and not retroactively apply the post-change definition.
- **Priority and Scope of Natural Language Instructions:** Prompts may contain both overall instructions and individual instructions tied to OOPD structures (modules, classes, methods, etc.). Apply the following **Specificity Rule** when interpreting these instructions:
  - **Scope:** Each element defined by the Markdown hierarchy (heading levels, lists) has its own scope of instruction application.
  - **Inheritance and Override:** Instructions from a higher scope (e.g., entire prompt, module level) are applied (inherited) by default to lower scopes. However, if a **more specific individual instruction** regarding the same matter is described within a lower scope, that individual instruction **overrides** the higher-level instruction and takes precedence within that lower scope.
  - **Limited Application:** The effect of an overridden individual instruction is limited to its scope (and further down) and does not affect other elements at the same level or instructions in higher scopes.
  - **Example:** Even if the entire prompt instructs "Responses should be concise," if the description for a specific method instructs "Explain the behavior of this method in detail," a detailed response takes precedence only for that method's explanation.
- **Placement Constraint for Definition Elements:** Major definition elements such as Class definitions (`#### ClassName`), Interface definitions (`#### InterfaceName`), Structure definition groups (`#### {Fixed name for structure definitions}`), and Enum definition groups (`#### {Fixed name for enum definitions}`) **MUST be described at a level below the Module definition (`##`) (i.e., `###` or lower).** They cannot be placed at the top level or the same level as the Module. The AI must strictly adhere to and interpret this hierarchical structure.
- Treat Structure definitions primarily as lightweight containers for simple data holding, distinct from classes. The AI should basically infer/complement its components (properties, etc.) based on the struct's name and accompanying description. Use classes when complex structures or behaviors are needed.

**6. Handling Programming Elements (Thorough Prohibition of Code Generation):**

- Even if programming elements (classes, methods, etc.) are included in **structured prompt descriptions** or the prompt body, treat them as **metaphors for conveying structure and thinking frameworks**, and **NEVER directly link them to specific code generation or implementation.**
- As long as this Object-Oriented Terminology for Prompt Design is used, **no code generation will be performed by default.**
- **Only** if the user specifies a particular programming language within the prompt AND **explicitly** requests code generation, perform code generation in that language on a limited basis. Otherwise, refrain from code generation and stick to conceptual explanations or examples.
- **Code generation is an act outside the scope of this definition and considered an AI judgment error.**

**7. Self-Check (Strict Adherence):**

**【Most Important - Automatic Execution Obligation】When the AI generates a response containing the OOPD format (e.g., definitions enclosed in Markdown code blocks "(`~~~Markdown`) ... (`~~~`)"), it MUST 【automatically】 perform validation based on this self-checklist immediately before outputting the response. This is a mandatory process that MUST ALWAYS be executed whenever the AI outputs the OOPD format, regardless of whether there is an explicit "self-check" instruction from the user. (A most critical process that must never be ignored.)**

- `[ ]` Does the output contain programming code? (If not explicitly requested. This is a **critical violation**)
- `[ ]` Is the technical explanation too detailed, assuming programming knowledge? (OOPD is a thinking framework)
- `[ ]` Are **Basic Terms** correctly used with the fixed notation defined in **`basic_terms.md`**? (Variations in notation for type names, literals, keywords, etc., are **not permissible**)
- `[ ]` Are **User-Defined Identifiers** linked to consistent English hub names within the context and appropriately translated (based on rules or memory) to the specified output language? If using "Definition Format", does it follow the specified format (`{English Hub Name}::{Native Name}` or `{English Name}`, etc.)? (Lack of consistency is **fatal**)
- `[ ]` Is the **translation scope** limited to User-Defined Identifiers in the prompt's structural definitions, not affecting the user-generated content body?
- `[ ]` **【Reserved Word Collision Check】** In the generated definition, are any **OOPD reserved words (Basic Terms, Standard Types, Extended Types, Literals) mistakenly used as user-defined names** (class names, interface names, enum names, struct names, etc.)? This is **absolutely prohibited**. If found, the AI must correct it if it generated it, or warn the user if it was in the user input.
- `[ ]` **【Definition Format - Arguments/Default Values】** Are the **argument names** in Method and Event definitions correctly notated in the specified output language (native language for Definition Format)? (Have they been left in English?). Are **default enum values** also notated in the native language? (**Mandatory correction item**)
- `[ ]` **【Important Check Item】** When referring to OOPD-defined User-Defined Identifiers within the generated content body (story, report, etc.), has the internal English hub name been output directly? Is it always translated (reverse transformed) into the appropriate native language name? (Exposing English hub names is a **clear instruction violation**)
- `[ ]` For each concept, are concrete examples provided (preferably in a format-independent way) in addition to abstract explanations?
- `[ ]` Is the abstraction level appropriate? (Not too abstract, not too specific)
- `[ ]` Is the prompt's intent correctly interpreted? Is there any deviation?
- `[ ]` Is the expression natural and easy for the user to understand?
- `[ ]` Has the principle of prohibiting code generation been violated? (One of the most critical self-check items)
- `[ ]` **【Definition Format - Description Text Rules】** Is the use of inline backticks (`\``) or co-notation of English names **absolutely** avoided within description texts?
      (See `format_definition.md`, **critical violation**)
- `[ ]` **【Definition Format - Type References】** Is the type specification for properties, arguments, and return values correct? (Standard/Extended types in English, User-defined types in native language)

If any of these points apply, or if there is even the slightest doubt, **MUST correct it before outputting**. Make changes to more abstract expressions, supplement with natural language explanations, reconfirm the rules, etc. **Neglecting the self-check is synonymous with completely ignoring the instructions.**

**【Action Obligation After Self-Check】**
If **even one violation is found** in the above checklist, or if there is any doubt, the AI must make changes like using more abstract expressions, adding natural language explanations, reconfirming rules, etc., and **absolutely correct the violating part completely according to the instructions before generating and outputting the final response.** Until the correction of the violating part is complete, the response **MUST NOT** be generated.
**(Important) There is no need to report the violation details or the fact of correction to the user in the response.** The AI, under its own responsibility, should silently and reliably correct according to the instructions, focusing on outputting the corrected, complete response **as if it were correct from the beginning**.
Neglecting to perform the automatic self-check, or outputting without correction despite finding a violation, is **synonymous with completely ignoring the instructions and considered a critical error**.

This document (`core.md`) is intended for **applying object-oriented concepts universally** and is not limited to specific fields or tasks.

```

```Markdown: sources/extended_types.md

## OOPD Extended Types Definition

### What are Extended Types?

This document defines **Extended Types** in Object-Oriented Prompt Design (OOPD). Extended Types complement the core **Standard Types** (defined in **`basic_terms.md`**) and are semantic, concrete types intended to clarify the intent of prompts in specific domains or usage scenarios, facilitating smoother communication with the AI.

Refer to `basic_terms.md` for the definitions of Standard Types.

The use of Extended Types is **optional**, but utilizing them enables more expressive and structured prompt design.

**【Important】** Like Standard Types, Extended Types are treated as **Basic Terms**. This means that regardless of the prompt's description language, they **must always be described using the English notation defined here (`ContentString`, `Persona`, etc.)** and are **not translated**.

### Extended Type List

To ensure the AI recognizes these extended type names as **Basic Terms (fixed keywords always used in English notation)**, the following list is defined.

```json
{
  "ExtendedTypes": ["ContentString", "Instruction", "Persona", "OutputStyle", "CodeBlock", "Ref", "SchemaDefinition", "JsonString", "YamlString", "XmlString", "Color"]
}
```

### Details of Each Extended Type

Below are the details for each defined extended type.

Note for AI: The description of multiple formats in the 'Underlying Representation/Format' for extended types indicates flexibility in the AI's internal interpretation. The AI should understand the content according to the meaning of the extended type and reflect it in processing, whether the user describes it in natural language or in a form suggesting structured data.

#### `ContentString`

- **Meaning:**
  Represents the central text block that the AI processes or generates, such as the main body of an article, report content, email body, or story text. Used to specify text as content, distinct from other metadata (like instructions or personas).
- **Use Cases:**
  - Specifying the target for summarization/translation of articles or documents.
  - Specifying the body part of reports or emails.
  - Specifying the main body part of creative works like stories or poems.
  - When wanting to indicate pure content text, distinct from code (`CodeBlock`) or instructions (`Instruction`).
- **Underlying Representation/Format:**
  - `String`.
  - May also contain structured text, such as Markdown format.
- **Related Basic Terms:**
  - `String` (from `basic_terms.md`)

#### `Instruction`

- **Meaning:**
  Represents specific instructions, commands, or task details described in natural language for the AI to execute. A type for clearly indicating action requests to the AI, distinct from other information (like data or context) within the prompt. Describes content that prompts specific actions, not just explanations.
- **Use Cases:**
  - When wanting to structurally indicate the instruction part for the AI within complex prompts.
  - When defining multiple instruction steps to be executed sequentially.
  - Meta-prompting, such as treating the prompt itself as data for analysis or generation.
- **Underlying Representation/Format:**
  - `String`. Instruction text in natural language.
- **Related Basic Terms:**
  - `String` (from `basic_terms.md`)

#### `Persona`

- **Meaning:**
  Represents the specific role, character image, or expert stance persona setting that the AI is intended to embody. This includes the AI's response style (e.g., 'formal', 'friendly'), tone of voice (e.g., 'polite language', 'assertive tone'), assumed knowledge level (e.g., 'beginner-friendly', 'expert level'), thinking style (e.g., 'logical', 'creative'), or even a specific background (e.g., '18th-century philosopher'). Defining these elements descriptively specifies the AI's behavior.
- **Use Cases:**
  - Making the AI respond as a specific role (e.g., "skilled editor," "friendly assistant," "specific historical figure").
  - Controlling the tone and expertise level of responses.
  - Defining character dialogues or role-playing scenarios.
- **Underlying Representation/Format:**
  - `String` (text describing the persona) or `Dictionary` (structured attributes like name, personality, tone).
- **Related Basic Terms:**
  - `String`, `Dictionary` (from `basic_terms.md`)

#### `OutputStyle`

- **Meaning:**
  Represents composite information for specifying the format, appearance, writing style, tone, etc., of the final output generated by the AI. Describes requirements related to response formatting or style, such as "Use Markdown bullet points," "Output in JSON format," "Use polite language with an empathetic tone," or "Summarize to approximately 500 characters."
- **Use Cases:**
  - Specifying output format (e.g., Markdown, JSON, bullet points).
  - Specifying writing style (e.g., formal, casual, academic).
  - Specifying tone (e.g., polite, empathetic, assertive).
  - Specifying constraints like character limits or summarization levels.
- **Underlying Representation/Format:**
  - `Dictionary` (with attributes like `format: String`, `tone: String`, `length: Number`).
  - Or, a simple `String` (e.g., "JSON format, polite tone").
- **Related Basic Terms:**
  - `Dictionary`, `String`, `Number` (from `basic_terms.md`)

#### `CodeBlock`

- **Meaning:**
  Represents a snippet of code itself written in a specific programming language. Used to specify the target code when requesting the AI to generate, explain, review, or debug code, or to provide code examples as reference. Co-notating the language type (e.g., 'Python', 'JavaScript') is recommended but not required.
- **Use Cases:**
  - Specifying the target for instructions like code generation, explanation, review, debugging, or translation.
  - Embedding sample or reference code within the prompt.
  - Clearly distinguishing between text parts and code parts.
- **Underlying Representation/Format:**
  - `String` (the code itself).
  - Can also be represented as a `Dictionary` with an attribute specifying the language (e.g., `language: String`).
- **Related Basic Terms:**
  - `String`, `Dictionary` (from `basic_terms.md`)

#### `Ref`

- **Meaning:**
  Represents an identifier indicating reference information or location to external resources or other data. Specifically, this includes web page URLs, file system paths, API endpoints, database record IDs, or links to image or video files. Used as the reference target when the AI accesses these resources or refers to them.
- **Use Cases:**
  - Specifying web page URLs.
  - Specifying local or remote file paths.
  - Specifying API endpoints.
  - Specifying links or identifiers to images, audio, or video files.
  - Indicating references to other data, such as database record IDs.
- **Underlying Representation/Format:**
  - `String`. Various formats of strings like URL, file path, URN, data URI.
- **Related Basic Terms:**
  - `String`, `UniqueID` (from `basic_terms.md`)

#### `SchemaDefinition`

- **Meaning:**
  Represents a data structure definition, schema, or data model itself described in text format. Examples include JSON Schema definitions, database table definitions (like CREATE TABLE statements), or class structure definitions. Used when instructing the AI to generate data based on a specific structure or to analyze/explain the data structure itself.
- **Use Cases:**
  - Instructing data generation based on a specific schema.
  - Requesting the AI to define or explain a data structure.
  - Specifying data validation rules.
- **Underlying Representation/Format:**
  - `String` (the schema definition described in text).
  - Often represented by `JsonString` or `YamlString`.
- **Related Basic Terms:**
  - `String` (from `basic_terms.md`), `JsonString`, `YamlString` (defined in this file)

#### `JsonString`

- **Meaning:**
  Represents a string conforming to the JSON (JavaScript Object Notation) format. Indicates that it holds a valid JSON data structure (starting with an object {} or array \[]) as a string value. Used when wanting to directly handle structured data like API response data or configuration information in JSON format.
- **Use Cases:**
  - Instructing parsing, generation, or transformation of JSON data.
  - Explicitly indicating that structured data should be input/output in JSON format.
  - Body part of API requests/responses, etc.
- **Underlying Representation/Format:**
  - `String` (a string conforming to JSON format).
- **Related Basic Terms:**
  - `String` (from `basic_terms.md`)

#### `YamlString`

- **Meaning:**
  Represents a string conforming to the YAML (YAML Ain't Markup Language) format. Indicates that it holds a valid YAML data structure as a string value. Used when wanting to directly handle configuration file content or human-readable structured data in YAML format.
- **Use Cases:**
  - Instructing parsing, generation, or transformation of YAML data.
  - Explicitly indicating that configuration files or structured data should be handled in YAML format.
  - OOPD instance data representation, etc.
- **Underlying Representation/Format:**
  - `String` (a string conforming to YAML format).
- **Related Basic Terms:**
  - `String` (from `basic_terms.md`)

#### `XmlString`

- **Meaning:**
  Represents a string conforming to the XML (Extensible Markup Language) format or HTML (HyperText Markup Language) format. Indicates that it holds a valid XML/HTML markup structure as a string value. Used when wanting to directly handle XML data snippets, configuration files, or HTML content.
- **Use Cases:**
  - Instructing parsing, generation, or transformation of XML/HTML data.
  - Explicitly indicating the handling of configuration files, data exchange (like SOAP), or markup documents.
- **Underlying Representation/Format:**
  - `String` (a string conforming to XML/HTML format).
- **Related Basic Terms:**
  - `String` (from `basic_terms.md`)

#### `Color`

- **Meaning:**
  Specifies a color value as a string. Assumes description in formats commonly recognized in CSS etc. (e.g., color name 'red', HEX value '#FF0000', RGB value 'rgb(255, 0, 0)', HSL value 'hsl(0, 100%, 50%)'). Used for UI color specification or color instructions during image generation, etc.
- **Use Cases:**
  - UI design, data visualization, image generation instructions.
  - Color settings in simulation environments (sky color, object color, etc.).
  - Instructions for text decoration (text color, background color).
- **Underlying Representation/Format:**
  - `String` (Recommended). Assumes commonly used formats like HEX (`#RRGGBB`, `#RGB`), RGB (`rgb(r,g,b)`), HSL (`hsl(h,s,l)`), color names (`red`, `blue`), etc., as used in CSS.
- **Related Basic Terms:**
  - `String` (from `basic_terms.md`)

```

```Markdown: sources/basic_terms.md

# OOPD Basic Terms Definition

This document defines the **Basic Terms** in Object-Oriented Prompt Design (OOPD). Basic Terms are **fixed keywords** used to indicate the structure or specific components of OOPD. Regardless of the prompt's description language, the fixed notation (or English notation) defined here is used, and **translation processing is not performed**.

The AI must recognize these Basic Terms and use them in responses with the specified fixed notation (or English notation) for the target language. **【Important】Variations from the defined notation are not permissible.**

Basic Terms are classified into the following categories.

## 1. Core Concepts

Terms indicating the fundamental ideas of OOPD.

```json
{
  "en": "Class", "ja": "クラス", "zh-CN": "类", "zh-TW": "類別", "es": "Clase", "fr": "Classe", "de": "Klasse", "ko": "클래스", "pt": "Classe", "ru": "Класс", "ar": "فئة", "hi": "क्लास"
}
```

```json
{
  "en": "Object", "ja": "オブジェクト", "zh-CN": "对象", "zh-TW": "物件", "es": "Objeto", "fr": "Objet", "de": "Objekt", "ko": "객체", "pt": "Objeto", "ru": "Объект", "ar": "كائن", "hi": "ऑब्जेक्ट"
}
```

```json
{
  "en": "Instance", "ja": "インスタンス", "zh-CN": "实例", "zh-TW": "實體", "es": "Instancia", "fr": "Instance", "de": "Instanz", "ko": "인스턴스", "pt": "Instância", "ru": "Экземпляр", "ar": "مثيل", "hi": "इंस्टेंस"
}
```

```json
{
  "en": "Property", "ja": "プロパティ", "zh-CN": "属性", "zh-TW": "屬性", "es": "Propiedad", "fr": "Propriété", "de": "Eigenschaft", "ko": "속性", "pt": "Propriedade", "ru": "Свойство", "ar": "خاصية", "hi": "प्रॉपर्टी"
}
```

```json
{
  "en": "Method", "ja": "メソッド", "zh-CN": "方法", "zh-TW": "方法", "es": "Método", "fr": "Méthode", "de": "Methode", "ko": "메소드", "pt": "Método", "ru": "Метод", "ar": "طريقة", "hi": "मेथड"
}
```

```json
{
  "en": "Type", "ja": "型", "zh-CN": "类型", "zh-TW": "型別", "es": "Tipo", "fr": "Type", "de": "Typ", "ko": "타입", "pt": "Tipo", "ru": "Тип", "ar": "نوع", "hi": "टाइप"
}
```

```json
{
  "en": "Interface", "ja": "インターフェース", "zh-CN": "接口", "zh-TW": "介面", "es": "Interfaz", "fr": "Interface", "de": "Schnittstelle", "ko": "인터페이스", "pt": "Interface", "ru": "Интерфейс", "ar": "واجهة", "hi": "इंटरफ़ेस"
}
```

```json
{
  "en": "Event", "ja": "イベント", "zh-CN": "事件", "zh-TW": "事件", "es": "Evento", "fr": "Événement", "de": "Ereignis", "ko": "이벤트", "pt": "Evento", "ru": "Событие", "ar": "حدث", "hi": "इवेंट"
}
```

```json
{
  "en": "Composition", "ja": "コンポジション", "zh-CN": "组合", "zh-TW": "組合", "es": "Composición", "fr": "Composition", "de": "Komposition", "ko": "컴포지션", "pt": "Composição", "ru": "Композиция", "ar": "تكوين", "hi": "कंपोजीशन"
}
```

```json
{
  "en": "Aggregation", "ja": "集約", "zh-CN": "聚合", "zh-TW": "聚合", "es": "Agregación", "fr": "Agrégation", "de": "Aggregation", "ko": "애그리게이션", "pt": "Agregação", "ru": "Агрегация", "ar": "تجميع", "hi": "एग्रीगेशन"
}
```

```json
{
  "en": "Inheritance", "ja": "継承", "zh-CN": "继承", "zh-TW": "繼承", "es": "Herencia", "fr": "Héritage", "de": "Vererbung", "ko": "상속", "pt": "Herança", "ru": "Наследование", "ar": "وراثة", "hi": "इनहेरिटेंस"
}
```

```json
{
  "en": "Module", "ja": "モジュール", "zh-CN": "模块", "zh-TW": "模組", "es": "Módulo", "fr": "Module", "de": "Modul", "ko": "모듈", "pt": "Módulo", "ru": "Модуль", "ar": "وحدة", "hi": "मॉड्यूल"
}
```

## 2. Format Keywords

Keywords used to indicate the structure of the OOPD format. **MUST use the notation defined in Basic Terms below.**

### 2.1 Element Definition Keywords

Keywords in bold notation indicating element lists within classes or interfaces (see `format_common.md`).
In the format specification, for example, to indicate the start of a property list, use the Basic Term **`Property`** (`ja`: `プロパティ`) (e.g., `**Property:**`). Similarly, use **`Method`** (`ja`: `メソッド`) for method lists, and **`Event`** (`ja`: `イベント`) for event lists.

### 2.2 Definition Group Headings

Fixed `####` level heading names for grouping specific types of definitions (see `format_common.md`, `format_definition.md`).

```json
{
  "en": "Structure Definitions", "ja": "構造体定義", "zh-CN": "结构体定义", "zh-TW": "結構體定義", "es": "Definiciones de Estructuras", "fr": "Définitions de Structures", "de": "Strukturdefinitionen", "ko": "구조체 정의", "pt": "Definições de Estrutura", "ru": "Определения структур", "ar": "تعريفات الهياكل", "hi": "संरचना परिभाषाएँ"
}
```

```json
{
  "en": "Enum Definitions", "ja": "列挙型定義", "zh-CN": "枚举定义", "zh-TW": "列舉定義", "es": "Definiciones de Enumeraciones", "fr": "Définitions d'Énumérations", "de": "Enum-Definitionen", "ko": "열거형 정의", "pt": "Definições de Enumeração", "ru": "Определения перечислений", "ar": "تعريفات التعداد", "hi": "एनम परिभाषाएँ"
}
```

### 2.3 Base Class / Interface Keywords

Keywords in bold notation within class definitions to indicate base classes or implemented interfaces (see `format_definition.md`).
To indicate a base class, use the Basic Term **`baseclass`** (`ja`: `基底クラス`) (e.g., `**baseclass:**`). To indicate implemented interfaces, use the Basic Term **`Interface`** (`ja`: `インターフェース`) (e.g., `**Interface:**`).

```json
{
  "en": "baseclass", "ja": "基底クラス", "zh-CN": "基类", "zh-TW": "基礎類別", "es": "clasebase", "fr": "classebase", "de": "Basisklasse", "ko": "기본클래스", "pt": "classebase", "ru": "базовыйкласс", "ar": "फئةأساسية", "hi": "आधारवर्ग"
}
```

*(Interface uses the definition of the core concept `Interface` above)*

## 3. Types and Literals

Terms representing data types or fixed values. These are always used in **English notation**.

### 3.1 Standard Types

Basic data types.

```json
{
  "StandardTypes": [
    "String", "Number", "Boolean", "List", "Dictionary", "UniqueID", "Instant", "Void", "Any"
  ]
}
```

*(Note: The `<>` in `List<T>` or `Dictionary<K,V>` is notation indicating type parameters; the Basic Terms themselves are `List`, `Dictionary`.)*

### 3.2 Literals

Specific fixed values.

```json
{
  "Literals": [
    "True", "False", "Null"
  ]
}
```

### 3.3 Extended Types

Semantic types for specific domains or uses. Refer to `extended_types.md` for detailed definitions. These are also always used in English notation.

*(Note: The list of extended types itself is managed in `extended_types.md`, so the list is not included here. The AI should refer to `extended_types.md` to recognize extended type names as Basic Terms (fixed English).)*

## 4. Other Keywords

```json
{
  "en": "Optional", "ja": "オプション", "zh-CN": "可选", "zh-TW": "可選的", "es": "Opcional", "fr": "Optionnel", "de": "Optional", "ko": "선택적", "pt": "Opcional", "ru": "необязательный", "ar": "اختياري", "hi": "वैकल्पिक"
}
```

```

```Markdown: sources/localization_overview.md

## OOPD Localization Overview

### Overview

This document explains the basic concepts and strategy for multilingual support (localization) in Object-Oriented Prompt Design (OOPD). OOPD aims to enable users worldwide to design prompts in their native language, interact effectively with AI, and share the definitions they create across language barriers.

### Goals

- **Description in Native Language:** Users can, in principle, describe OOPD format (especially "User Format") in their own native language.
- **Sharing Definitions:** OOPD definitions (Definition Format) created in different languages can be accurately understood and reused by speakers of other languages and by AI.
- **Interpretation by AI:** AI can accurately interpret the structure and intent of prompts written in the user's native language.
- **Consistent Translation:** AI maintains consistency in the translation of terms and concepts when processing information internally and generating responses.

### Hub Language Model and Technical Foundation

OOPD employs the following technical foundation to ensure consistency in translation between multiple languages and internal processing:

- **Hub Language:** **English (`en`) is adopted as the hub language**.
  1. **Input:** The user inputs the prompt in their native language. **(Note: If the input language is English (`en`), step 2, internal conversion, is skipped.)**
  2. **Internal Conversion:** (If the input language is not English) The AI interprets the "User-Defined Identifiers" within the prompt and internally converts/manages them into English hub language representations.
  3. **Processing:** Internal thinking, inference, and response generation by the AI are performed based on this English hub representation.
  4. **Output:** The AI translates the generated response from the English hub representation into the output language specified by the user (or the input language) and presents it.
- **Character Encoding:** **UTF-8** is used as the standard encoding for interpreting and generating prompts, ensuring proper handling of multilingual characters.

### Term Classification and Handling

Terms used in OOPD are classified into two types from a translation perspective.

- **Basic Terms:**
  - **Definition:** **Fixed keywords** indicating the structure or specific components of OOPD. Includes core concepts (`Class`, `Method`, etc.), format keywords (`Property`, `baseclass`, etc.), group headings (`Structure Definitions`, etc.), standard types (`String`, `Number`, etc.), and literals (`True`, `False`, etc.).
  - **Definition Location:** The complete list of Basic Terms and their multilingual notations (or fixed English notation) is centrally defined in the **`basic_terms.md`** file. (Refer to `extended_types.md` only for extended types).
  - **Handling:** These are **not translated**. The fixed notation for each language defined in `basic_terms.md` (or always the English notation) is used as is.
- **User-Defined Identifiers:** User-defined class names, interface names, method names, property names, event names, enum definition names, enum values, etc. These are **subject to translation processing** by the AI.

### Translation Processing

Translation processing by the AI is performed based on the following principles and rules:

- **Target:** Only "User-Defined Identifiers" included in the structural definitions within the prompt.
- **Timing:**
  - **During Input Interpretation:** Infer and convert content described in the native language to the English hub language.
  - **During Initial Name Determination:** Can infer the optimal English name by referencing descriptions and context.
  - **During Response Generation:** Translate from the English hub language to the specified output language. Does not reference descriptions when translating finalized definitions (for reversibility).
- **Ensuring Consistency (In-Context Memory):**
  - The AI **strives to maintain the mapping between User-Defined Identifiers and their English hub names to the maximum extent possible, as long as it can remember and reference related past instructions and dialogues within the current conversation context.**
    *(The persistence of this memory is subject to the technical constraint of context memory available to the AI. The mapping is lost **only when the relevant information can no longer be referenced from the context**. This is not the AI abandoning effort, but rather an inability to guarantee consistency based on inaccessible information, representing a specification behavior based on system limitations.)*
  - **If a mapping remembered above exists and is referenceable from the current conversation context**, when the same User-Defined Identifier (or an expression judged synonymous by the AI) appears, the AI **MUST** use the remembered English hub name to prevent translation fluctuations. Utilization of this remembered mapping takes highest priority.
- **Translation Rules:**
  - Translation is performed based on **naming conventions** and **translation patterns** defined for each language pair. Refer to the respective language rule files (`{language_code}_rules.md`) in the `translation_rules` directory for details.
  - **Cross-lingual Concept Mapping:** For terms representing the same concept in different languages, the AI strives to map them to a common English hub name based on semantic similarity, referencing class definitions, descriptions, and translation rules for each language.
  - **Handling Representation Mappings (N-to-N, 1-to-N, N-to-1):**
    - **N-to-N (Recommended):** If the hub language and target language have different nuances in expression (e.g., the hub language has multiple expressions with different nuances like `isCompleted` and `hasFinished`), define corresponding different standard translations `xx_StandardTranslation1` and `xx_StandardTranslation2` in the target language `xx` whenever possible. This maintains the information content between languages as much as possible.
    - **1-to-N (Caution):** If one word `TermA` in the hub language can be interpreted into multiple meanings like `xx_TranslationB` and `xx_TranslationC` in the target language `xx` depending on context, carelessly translating differently can prevent reverse translation back to `TermA`. In this case, it's recommended to either establish one representative standard translation `xx_TranslationB`, or use more specific expressions in the hub language like `TermA_Context1`, `TermA_Context2`.
    - **N-to-1 (Permissible):** Conversely, if distinguishing synonyms `TermX` and `TermY` in the hub language is difficult or unnatural in the target language `xx`, it is permissible to **consolidate them into one standard translation** `xx_StandardTranslationZ` in the target language.
  - **Standardization from Target Language to Hub Language:** When converting from a target language `xx` to the English hub, if expressions `xx_Expression1` and `xx_Expression2` in the target language refer to the same concept, strive to generate **one standard English hub name**, such as `HubTermAlpha`, when converting to the hub language. This maintains consistency in expression on the English hub language side.
- **Core Translation List (Limited Use):**
  - Maintaining and managing large-scale translation lists is impractical, so OOPD **avoids relying on fixed translation lists as the primary axis** for translation processing.
  - **However, as an exception,** for literals (`True`, `False`, `Null` are fixed to English notation) and **a very select few vocabularies** deemed necessary for strict mapping between languages, they might be defined and utilized as a core translation list in the future. (No extensive list exists currently.)
- **Role of AI Inference (Intentional Design):**
  - As mentioned above, the use of core translation lists is **limited**. Therefore, for unknown vocabulary or complex expressions not covered by the translation rules (`xx_rules.md`) for each language or their exceptional lists, **OOPD intentionally relies on the AI's own context understanding and general language capabilities (inference)**.
  - The AI should attempt translation in the following order of priority:
    1. **Mapping relationships remembered within the session** (see `core.md`).
    2. Defined **translation rules** (`xx_rules.md`).
    3. Defined **core translation list** (if it exists).
    4. **AI's own inference** if none of the above apply.
  - The AI should understand that inference may have limitations or fluctuations due to the model, but recognize that this approach is a design decision to balance realistic multilingual support with flexibility.
  - Adjustments for the naturalness of translation results (e.g., word order, conjugation) are also left to the AI's language capabilities.
- **Natural Language Parsing Suitability:** Translation rules consider making the generated target language names words/phrases that are easily identifiable by the AI as part of natural language instruction sentences within that language's grammatical structure (e.g., avoiding unnatural particle inclusion).

### Limitation of Translation Scope

AI translation processing is limited to the structural definition parts of the OOPD format (class names, method names, etc.). The **content body (story, report, etc.)** requested by the user for generation is **not subject to translation**.

### Regarding Reversibility

OOPD emphasizes that the meaning of definitions should not change between different languages (**semantic reversibility**), especially in the "Definition Format".

- In the "Definition Format", since English hub names are co-notated, identity at the hub language level is always guaranteed.
- However, note that due to the translation rules mentioned above (especially N-to-1 and standardization from target language to hub language), when translating from one language to another and back to the original, **perfect lexical (word-level) identity may not always be guaranteed**.
- **However, the important point is that OOPD always displays and utilizes consistent native language names within each user's working environment (language setting). For instance, if one user defines "顧客クラス" in Japanese, and another user receives it in an English environment and uses it as "Customer," each user will consistently encounter the same term within their respective language environments. Therefore, lexical differences in the translation process (e.g., consolidation into an English hub name, or the possibility of not reverting to the exact same word upon reverse translation to the original language) do not typically cause direct confusion in individual user experiences.**
- The goal is ultimately **"semantic reversibility,"** where the intent and structure of the definition do not change, and this is ensured by the consistency of display within each language environment.

### Format and Translation

- **User Format:** Described only in the native language. AI infers and manages English hub names internally.
- **Definition Format:** Co-notates standardized native language names and finalized English hub names. Shareable across languages. **Through this Definition Format, when a definition created in one language is used in another language environment, the AI generates and displays the standard native language name (or a name based on translation rules) for the receiving language based on the English hub name. This enables speakers of different languages to understand the definition in their respective native languages and use it consistently.** Conversion of definitions between different languages becomes possible via this format.

### Contribution

Contributions for supporting new languages (creating translation rules) or improving existing rules are welcome. The language files under the `translation_rules` directory are key to the accuracy and quality of translation.

```

```Markdown: sources/english_specification.md

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

```

```Markdown: sources/translation_rules/README.md

## OOPD Translation Rules Directory

### Overview

This directory (`translation_rules/`) contains files that define **language-specific translation rules** for Object-Oriented Prompt Design (OOPD). These rules are used by the AI to **bidirectionally translate** user-defined "User-Defined Identifiers" (class names, method names, property names, etc.) between the hub language, **English (`en`)**, and other supported languages.

These rules are core to OOPD's multilingual support capabilities and are essential for ensuring consistency between prompts written in different languages and natural expression in each language.

For the overall translation strategy and hub language model, refer to `localization_overview.md` in the root directory.

### Directory Structure and File Naming Convention

- Translation rules for each language are managed as separate Markdown files.
- File names follow the format **`{language_code}_rules.md`**.
  - `{language_code}` uses the 2-letter lowercase language code from **ISO 639-1** (e.g., `ja`, `fr`, `de`). If necessary, consider concatenating a region code (e.g., `zh_cn`, `pt_br`) with an underscore.
- Examples:
  - `ja_rules.md`: Japanese translation rules
  - `fr_rules.md`: French translation rules
  - `zh_cn_rules.md`: Rules for Chinese (Simplified)

### Content of Each Language Rule File

Each `{language_code}_rules.md` file should include the following information (refer to existing rule files or templates for details):

1. **Language Code:** Clearly state the language code (`language_code`) the file targets.
2. **English → Target Language Translation Rules:**
   - **Name Conversion Rules** for translating English hub names to the target language (for each element type). This includes naming conventions (suffixes, etc.) in the target language.
   - **Translation Patterns** for specific English expressions/structures corresponding to target language patterns.
   - **Handling of Specific Words/Expressions** to note when translating to the target language.
3. **Target Language → English Translation Rules:**
   - **Name Conversion Rules** for converting target language expressions to English hub names (conforming to standard English naming conventions).
   - **Translation Patterns** for target language expressions/structures corresponding to English hub name patterns.
   - **Handling of Specific Words/Expressions** to note when translating from the target language.
4. **Language-Specific Notes:**
   - Grammar, character codes, idiomatic expressions, and other considerations specific to that language.

Rules should be described in a structured manner, as much as possible, to be easily interpretable by the AI.

### Usage by AI

Typically, AI systems do not read these individual language rule files directly. Instead, they utilize a **single combined rule file** (e.g., `ai_combined_translation_rules.md`) generated by an automated process like GitHub Actions. The AI refers to this combined file and applies the appropriate rule set based on the prompt's processing language or the requested output language.

### Contributing

To expand OOPD's multilingual support, contributions for adding translation rules for new languages or improving existing rules are welcome.

- **Adding rules for a new language:**
  1. Check the ISO 639-1 code for the target language and create a `{language_code}_rules.md` file.
  2. Referencing existing rule files (e.g., `ja_rules.md`), describe the rules according to the "Content of Each Language Rule File" section above. Also refer to the English specification (`english_specification.md`) and the localization overview (`localization_overview.md`).
  3. Deep knowledge of the target language (preferably native level) is required. Please give sufficient consideration to naming conventions and natural expressions.
  4. Propose via pull request, etc.
- **Improving existing rules:**
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
  - 助詞「の」は、原則として名詞句の連結には使用してはいけません (例: 「ユーザーの名前」ではなく「ユーザー名」)。
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

- **構造体定義名 (Struct Names):** (`PascalCase`)
  - **標準形式:** `{翻訳された名詞句}構造体` という形式の日本語名に変換します。基本的にクラス名と同じです。
  - **定義フォーマット例:** `Appearance::外見構造体`
  - **例 (概念):** `Appearance` は `外見構造体` になります。

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

- **構造体定義名:** (`「{名詞句}構造体」` 等)
  - **形式:** `PascalCase`
  - **例:** `外見構造体` は `Appearance` になります。

##### 翻訳パターン (Translation Patterns)

(日本語の特定の構造から英語の構造を生成するパターンがあれば記述します。)

- 現時点では特筆すべき共通パターンは名称変換ルールでカバーされているため、省略。

##### 特殊な単語・表現の扱い (Specific Words/Expressions)

(日本語特有の表現や和製英語などを英語ハブ名に変換する際のルールや注意点を記述します)

- 和製英語 (例: `カスタム`): 可能な限り標準的な英単語 (`Custom`) に変換します。
- 長音記号 (ー): 英語名生成時には無視または母音の繰り返しに変換するなど、一貫したルールを検討します (例: `サーバー` は `Server`)。
- (必要に応じて追加)

#### 言語固有の注意事項 (Language-Specific Notes)

- **助詞「の」の使用は原則禁止**
  - **理由:** 日本語の識別子（クラス名、プロパティ名等）に助詞「の」が含まれると、 **その識別子を使った自然言語での指示や説明（例: 「AのBを取得して」）が非常に不自然になり、AIや人間による指示の正確な解釈を著しく困難にする** ため、原則として使用を **禁止** します。 **例外は認めません。**
  - **代替表現:** 識別子の単語連結には「の」を使わず、 **名詞の直接連結** （例: `ユーザー名`）や、より自然な **日本語の複合語・熟語** （例: `注文履歴`, `線種`）を使用してください。
  - **適用:** この禁止ルールは、クラス、インターフェース、列挙型、メソッド、イベント、プロパティ、構造体、引数など、 **全てのユーザー定義識別子** に **厳格に適用** されます。
  - **AIへの指示:** AIは、この「 **自然言語指示の困難化** 」という理由を理解し、日本語名を生成・提案する際は、 **絶対に** 「の」を含まず、上記代替表現を用いた自然な名称を選択してください。ユーザーが「の」を用いた場合、ルール違反として明確に指摘し、理由を説明した上で、修正を自動適用してください（フォーマットモードにかかわらず）。

- **敬語:** プロンプトに含まれる敬語表現は、翻訳用語の解釈においては基本的に無視します。
- (その他、必要に応じて追記)

```

```Markdown: sources/interaction_mode_selection.md

## Interaction Mode Selection and Initial Procedure (for Non-English Languages)

### Purpose

This document defines the **initial procedure** for when the AI starts an interaction based on Object-Oriented Prompt Design (OOPD) with the user in a **language other than English**, and the AI's **basic interaction modes** corresponding to the working format selected by the user. These procedures and modes serve as the premise for interpreting and applying subsequent OOPD specifications (especially those related to formats).

**Note:** If the user's language is **English (`en`)**, according to the OOPD specification (see `english_specification.md`), the AI operates in a **strict mode compliant with the Definition Format** at all times, without distinguishing formats. Therefore, the **format confirmation procedure described in this document does not apply** to interactions in English.

### Initial Format Confirmation (Non-English Languages)

If the AI determines that the user has initiated class design, definition, or related operations using OOPD in a **language other than English**, **first confirm the working format** using the following procedure:

1. **Confirmation:** Clearly ask the user, "Will you be working with OOPD using the **User Format** or the **Definition Format**?"
2. **Explanation:** Simultaneously with the question, briefly explain the main features of each format as follows:
   - **User Format:**
     - Primarily described in your native language, allowing for more flexible description.
     - Naming conventions are relatively lenient (AI suggests standard names but doesn't enforce them).
     - English hub names are managed internally by the AI.
     - Suitable for personal use, drafting ideas, and rapid prototyping.
   - **Definition Format:**
     - Requires co-notation of English hub names and adherence to standard naming conventions.
     - Structured, suitable for sharing and reusing definitions.
     - **Especially if you don't insist on specific names yourself, or if you want to efficiently create definitions following standard naming conventions, working in this format, where the AI automatically applies standard names (\*), is recommended.**
       \*(*AI will notify you upon automatic application)*
3. **User Selection:** Accept the user's choice ("User Format" or "Definition Format").

### AI Behavior Modes Based on Format Selection (Non-English Languages)

After the user selects a format, the AI should switch to the **corresponding behavior mode** and interpret/execute subsequent OOPD-related instructions as follows:

- **When User Format Mode is Selected:**
  - The AI performs flexible interpretation based on the User Format specification (see `format_user.md`).
  - If the name specified by the user deviates from standard naming conventions, the AI **only suggests** the standard name and does not confirm usage or automatically apply it. It respects the name used by the user.
  - Follow other rules specific to the User Format.

- **When Definition Format Mode is Selected:**
  - The AI performs strict interpretation and validation based on the Definition Format specification (see `format_definition.md`).
  - If the name specified by the user violates standard naming conventions, the AI calculates the standard name, **notifies the user, and then automatically applies it**.
  - Strictly apply other rules specific to the Definition Format, such as requiring co-notation of English hub names and fully qualified names for cross-module references.

### Changing Modes (Non-English Languages)

The user may wish to change the format during the conversation. The AI should switch modes according to the user's instruction, considering the following points:

- **Changing from User Format to Definition Format:**
  - If the user instructs something like "Convert to Definition Format," the AI reformats the current definition content based on the strict rules of the Definition Format (co-notation of English hub names, application of standard naming conventions, etc.).
  - At this time, the AI performs inference/finalization of English hub names as necessary, and executes validation and automatic application (with notification) of naming conventions.

- **Changing from Definition Format to User Format:**
  - If the user instructs something like "I want to edit in User Format," the AI switches to the following mode:
    - **Format Change:** In displays and responses, omit format elements specific to the Definition Format (like co-notation of English hub names) and match the User Format description style.
    - **Internal Management:** Ensure English hub names are held and managed internally by the AI.
    - **Relaxation of Naming Conventions:** Lift the enforcement of standard naming conventions that were applied in the Definition Format. While using the standard native language names finalized in the Definition Format as a base, the AI allows the user to change those names or use names deviating from standard rules. For subsequent naming convention violations, shift to the mode of only making suggestions (the behavior when User Format is selected).

```

```Markdown: sources/formats/format_common.md

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

```

```Markdown: sources/formats/format_definition.md

### OOPD Format: Definition Format Specification

#### What is the Definition Format?

The Definition Format is a **strict and formal description format for sharing definitions created based on OOPD with others or reusing them across different sessions or environments**. It serves as the finalized version of a definition, aiming to ensure **reversibility** between languages and **consistency** in interpretation.

#### About This Document

This document (`format_definition.md`) explains the strict rules specific to the Definition Format. For common rules, refer to `format_common.md`. The Definition Format must follow the rules below, regardless of the prompt's description language.

#### Mandatory Rules and Formatting

- **Co-notation of English Hub Names (for Non-English Languages):**
  - **(Note: This rule applies when describing in languages other than English. When describing in English, use only the English name; co-notation of the hub name is unnecessary. See `english_specification.md`.)**
  - For "User-Defined Identifiers" subject to AI translation, such as class names, interface names, enum names, etc., the **finalized English hub name must always be co-notated**. See the individual description methods below for details.
  - English hub names follow the **English Naming Conventions** defined in `english_specification.md`.
  - The native language notation for User-Defined Identifiers follows the **standard naming conventions** defined in the translation rules for the target language (within `translation_rules/`).

- **Strict Application of Naming Conventions:**
  - As mentioned above, the **standard naming conventions defined for each language must be strictly applied** to both the native language name and the English hub name. (When describing in English, only the English Naming Conventions defined in `english_specification.md` apply.)
  - Module names must follow the English naming conventions defined in `english_specification.md`, and ensuring global uniqueness is strongly recommended.

- **Recognition of English Hub Name and Native Name:**
  - For elements co-notated in the format `{English Hub Name}::{Native Name}`, the AI **recognizes both the English Hub Name and the Native Name as valid identifiers** pointing to that element.

- **Cross-Reference:**
  - **Within the Same Module:** When referencing class names, etc., **must describe using only the native language name** (e.g., `propertyName: CustomerClass`). Do not describe the English hub name. The AI identifies the definition within the module from context.
  - **Across Different Modules:** If the referenced class, etc., belongs to another module, it **must be specified using the fully qualified name (`module.name.ClassName`)**. The same applies to type specifications. (Example: `creator (com.example.common.User)`)

- **Recommendation for Description Texts:**
  - **It is strongly recommended to write description texts** for each module, section, class, interface, method, property, etc., to clarify their purpose and meaning. This aids AI interpretation and promotes human understanding. Describe description texts in the prompt description language.

- **Module Definition (`##`):**
  - All definitions must be described within a module.
  - Format: `## {EnglishModuleName}`
  - Global uniqueness for module names is recommended (see `english_specification.md`).
  - The module's native name or detailed description text can be described as regular text below the `##` line (optional).

- **Headings (Class `####`, Interface `####`, Section `###`/`####`/..., Structure Definition `####`, Enum Definition `####`):**
  - **Class/Interface (Individual Definition):**
    - Format (Native): `{HeadingLevel} {NativeName} ({EnglishHubName}): {TitleSummary}`
    - Format (English): `{HeadingLevel} {EnglishName}: {TitleSummary}`
    - **【Important】The order of names is `{NativeName} ({EnglishHubName})` or `{EnglishName}`. Be careful not to reverse it.**

    - **【1. Title Summary (after `:` on the heading line)】**
      - **Role:** A title-like summary, as part of the heading, indicating the **core essence of the class/interface in one phrase**.
      - **Content:** Most succinctly expresses **"what"** the element is. Does not include specific feature lists or detailed context.
      - **Mandatory:** **Required**.
      - **Length:** Must be **extremely concise**. Generally described in **one line and as a short sentence**.
      - **Note for AI Generation:** The AI should generate the most concise and accurate expression capturing the essence of this element. Do not include redundant explanations or content that should be in the detailed description below. Also, **as it is a heading, a period should not be placed at the end of the line.** This needs judgment according to each language.
      - **Good Examples:**
        - `E-commerce site customer data model`
        - `Asynchronous task execution contract`
        - `Environment configuration value provider`
        - `3D object geometric transformation`
      - **Bad Examples:**
        - `Class for managing customer profiles and order history of an e-commerce site` (← A bit long, suitable for detailed description)
        - `This is a customer class` (← Meaningless)
        - Omitting it (← Required)

    - **【2. Detailed Description Text (below the heading line)】**
      - **Role:** The place to **explain in detail the purpose, functionality, usage methods, constraints, background, related information, etc.** of the class/interface, as **body text** independent of the heading.
      - **Content:**
        - Specific functions and scope of responsibility
        - Assumed usage scenarios
        - Design decisions and background
        - Important constraints and notes (e.g., thread safety, performance considerations)
        - References to related other classes or interfaces
        - References to external documents
        - Special instructions to the AI (e.g., "Ensure methods of this class guarantee idempotency")
      - **Mandatory:** **Optional**, but **strongly recommended** to deepen understanding of the class/interface. Should be described especially for complex or important elements.
      - **Format:** Can be freely described over multiple lines as regular Markdown text. Lists, emphasis, code blocks (` ``` `), etc., can also be used.
      - **Note for AI Generation:** The AI should describe the information necessary for understanding the element in a structured and easy-to-understand manner. It needs to provide more detailed information rather than simply repeating the content described in the title summary.

            ```markdown
            記述例 (日本語):
            #### 顧客クラス (Customer): ECサイトの顧客データモデル。

            このクラスは、ECサイトにおける顧客の基本情報（氏名、連絡先）、配送先住所リスト、および過去の注文履歴（直近100件）を一元的に管理します。
            データの整合性を保ち、関連サービス（推奨エンジン、サポートシステム）へ最新の情報を提供することが主な責務です。
            個人情報保護の観点から、メールアドレス等の機密情報へのアクセスは厳格に制御されます。
            インスタンス生成時には、必須項目（氏名、メールアドレス）のバリデーションを実行してください。
            ```

            *(Translator's Note: Japanese Markdown block retained as per instruction.)*

            ```markdown
            Description Example (English):
            #### Customer: E-commerce site customer data model

            This class centrally manages customer base information (name, contact), shipping address list, and past order history (latest 100) in the e-commerce site.
            Its primary responsibility is to maintain data integrity and provide up-to-date information to related services (e.g., recommendation engine, support system).
            Access to sensitive information like email addresses is strictly controlled due to privacy concerns.
            Validate required fields (name, email) upon instance creation.
            ```

    *(`Class`, `Interface` Basic Term definitions in `basic_terms.md`)*

  - **Section:**
    - Defined using Markdown headings (`###`, `####`, `#####`, etc.).
    - Format: `{HeadingLevel} {NativeName} ({EnglishHubName})` or `{HeadingLevel} {NativeName} ({EnglishHubName}): {DescriptionText}`
    - **Description text is optional**.
    - **If English is the native language:** Only `{EnglishName}` is used, parentheses for the English hub name are unnecessary. Rules for description text are the same as above.
    - Following the rules in `format_common.md`, multiple levels (nesting) are possible.
    - **【Important】** Class definitions (`#### {IndividualClassName}`), Interface definitions (`#### {IndividualInterfaceName}`), `#### {FixedNameForStructureDefinitions}` group, `#### {FixedNameForEnumDefinitions}` group, etc., can be placed not only directly under the module but also within sections of any level.
    - **【Constraint】However, these definition elements (classes, interfaces, group headings) MUST be described at a level below the Module definition (`##`) (i.e., `###` or lower).** They cannot be placed at the top level or the same level as the Module. (This is to maintain structural consistency when combining multiple definition files.)

  - **`#### {Fixed name for structure definitions}` / `#### {Fixed name for enum definitions}` (Group Headings):**
    - As instructed for reference in `format_common.md`, use the **fixed heading name** for each language defined in **`basic_terms.md`** (e.g., `#### 構造体定義` in Japanese, `#### Structure Definitions` in English).
    - These are group headings for organizing structure definitions and enum definitions, respectively, and can be used optionally.
    - Individual struct or enum definitions must be described under these group headings in list format (`-`).
    - It is not necessary to co-notate the English hub name in parentheses `()` for group headings.
    - If necessary, a description for the entire group can be written below the group heading.
        *(Basic Term definitions in `basic_terms.md`)*

- **Element Names (Property Name, Method Name, Event Name, Enum Definition Name, Enum Value, Struct Definition Name):**
  - Native language name is "primary", English hub name is "secondary".
  - Use the English hub name as a **prefix**, connected to the native language name with double colons `::`.
  - Basic Format: `{EnglishHubName}::{NativeName}`
  - **(For non-English languages)** As above.
  - **If English is the native language:** The prefix (`{EnglishHubName}::`) is unnecessary. Describe only the English name following the rules in `english_specification.md`.

- **Definition of List Format Elements (Property, Method, Event, Enum, Struct):**
  - Start the line with a Markdown list hyphen `-`.

  - **List Start Keyword:** When starting each list (property list, etc.), describe the corresponding **Basic Term** in bold notation, followed by a colon `:`. Refer to **`basic_terms.md`** for the Basic Terms to use.
    - Example (Japanese): `**プロパティ:**`, `**メソッド:**`, `**イベント:**`
    - Example (English): `**Property:**`, `**Method:**`, `**Event:**`

  - **Scope of Backticks (`\``):**
    - (Compliant with `format_common.md`)
    - **Property, Method, Event:** Enclose **only** the main part of the definition (from the space after the hyphen up to the type/return type specification). Do not enclose the description.
    - **Enum, Struct (Individual Definition):** Enclose **only** the element name part (`{EnglishHubName}::{NativeName}` or `{EnglishName}`). Do not enclose the description or value list.

  - **【Common Rule】Description of Explanations and Instructions:**
    - For each element definition (property, method, etc.), you can write an explanation describing its purpose, usage, constraints, instructions, etc.
    - The description text is written **after** the colon `:` at the end of the definition line, or **on the following line(s)**.
    - It can be described over **multiple lines**.
    - Description text is written as **regular Markdown text** and can include Markdown elements like lists (`-`, `*`, `1.`), emphasis (`**bold**`, `*italic*`), etc.
    - You can also omit the brief explanation after the colon `:` on the definition line and start the detailed explanation from the next line.
    - If the description text is short, it is recommended to write it on a single line if possible.
    - **Note:** Whether the description text is required/optional depends on the element type (required for struct, optional for enum). See the definition rules for each element for details.
    - **【Regarding Notation within Description Texts (Strict Adherence - Absolute Prohibition)】**
      - **1. Absolute Non-use of Backticks (`\``):** To ensure the readability of description texts and the accuracy of AI translation/interpretation, the use of **inline backticks within description texts is absolutely prohibited for any reason whatsoever.** Even when referring to other definition elements (property names, method names, type names, enum values, etc.) or technical terms, **must describe them as regular text** without enclosing them in backticks.
      - **2. Absolute Prohibition of English Co-notation:** Description texts should, in principle, be described **only** in the prompt's description language. To avoid critically impairing the accuracy and consistency of AI translation processing, **co-notating English names** within description texts using formats like `{EnglishHubName}::{NativeName}` or parentheses (`(englishName)`) is **absolutely prohibited.** The AI has the capability to determine necessary information from context, making such co-notation unnecessary and harmful.

            ```markdown
            記述例（プロパティの場合。他も同様）:
            **プロパティ:**

            *(最も推奨: 短い記載で済む場合)*
            - `propertyName1::プロパティ名1: Type`: これは一行で完結する説明です。

            *(推奨: 簡易説明に加え、詳細な説明が必要な場合)*
            - `propertyName2::プロパティ名2: Type`: ここに簡易説明を記述します。
              これは簡易説明に加え、複数行にわたる詳細な説明や指示の例です。
              - 詳細な仕様をリストで記述できます。
              - **重要:** この値は必ず正の数にしてください。

            *(詳細な説明や手順が多く必要な場合)*
            - `propertyName3::プロパティ名3: Type`:
              これは複数行にわたる説明や指示の例です。
              1. 詳細な仕様をリストで記述できます。
              2. 詳細な仕様をリストで記述できます。
              3. 詳細な仕様をリストで記述できます。
              4. 詳細な仕様をリストで記述できます。
              5. 詳細な仕様をリストで記述できます。
              6. 詳細な仕様をリストで記述できます。
              7. 詳細な仕様をリストで記述できます。
              8. 詳細な仕様をリストで記述できます。
              - **重要:** この値は必ず正の数にしてください。
            ```

            *(Translator's Note: Japanese example retained for context)*

            ```markdown
            記述例（列挙型の場合）:
            #### 列挙型定義

            *(最も推奨: 短い記載で済む場合)*
            - `ProcessingStatus::処理状態列挙型 = PENDING::待機中, RUNNING::実行中, COMPLETED::完了, FAILED::失敗`: 非同期処理の全体的な状態を示します。
            - `ColorFlag::色フラグ列挙型 = RED::赤, GREEN::緑, BLUE::青`: 基本的な色要素を表すビットフラグです。組み合わせて色を表現します (例: 紫 = 赤 + 青)。

            *(推奨: 簡易説明に加え、詳細な説明が必要な場合)*
            - `ErrorCode::エラーコード列挙型 = NONE::エラーなし, TIMEOUT::タイムアウト, INVALID_INPUT::不正な入力, SERVER_ERROR::サーバーエラー, UNKNOWN::不明なエラー`:
              処理が失敗状態になった場合の具体的な原因を示します。
              - タイムアウト: 規定時間内に処理が完了しなかった場合に設定されます。ネットワーク状況を確認してください。
              - 不正な入力: 入力データ形式が正しくないか、必須項目が欠落している場合に発生します。入力仕様書を参照してください。
              - サーバーエラー: サーバー内部で予期せぬ問題が発生しました。管理者に連絡してください。ログIDを併せて伝えると調査がスムーズです。

            *(説明がなくとも一般的に理解可能な場合)*
            - `Direction::方向列挙型 = NORTH::北, SOUTH::南, EAST::東, WEST::西`
            - `Size::サイズ列挙型 = SMALL::小, MEDIUM::中, LARGE::大`
            - `DayOfWeek::曜日列挙型 = MONDAY::月曜日, TUESDAY::火曜日, WEDNESDAY::水曜日, THURSDAY::木曜日, FRIDAY::金曜日, SATURDAY::土曜日, SUNDAY::日曜日`
            ```

            *(Translator's Note: Japanese example retained for context)*

- **Property Definition:**
  - Format (Native): - \`{EnglishHubName}::{NativeName}: {TypeName}\[, {OptionalSpecifier}]\`: {Description}
  - Format (English): - \`{EnglishName}: {TypeName}\[, {OptionalSpecifier}]\`: {Description}
  - **Type Name:**
    - **Standard/Extended Types:** Must use English notation (`String`, `Number`, `List<String>`, `Color`, etc.) (**Definitions in `basic_terms.md` and `extended_types.md`**).
    - **User-Defined Types (Class, Interface, Enum, Struct):** **【Important】Must reference using only the native language name** (e.g., `顧客クラス`, `色フラグ列挙型`). Do not describe the English hub name.
  - **Optional Item:**
    - In property definitions, optional items can be indicated by appending `, {OptionalSpecifier}` after the type name (Refer to **`basic_terms.md`** for the definition of the Basic Term **`Optional`** (`ja`: `オプション`)).
      - Example (Japanese): - \`プロパティ名: String, オプション\`
      - Example (English): - \`propertyName: String, Optional\`
  - **Description:** Follows **【Common Rule】Description of Explanations and Instructions** above.

- **Method Definition:**
  - Format (Native): - \`{EnglishHubName}::{NativeName}({ArgumentList}): {ReturnTypeName}\`: {Description}
  - Format (English): - \`{EnglishName}({ArgumentList}): {ReturnTypeName}\`: {Description}
  - **Return Type Name:** Same rules as property type names (Standard types in English, User-defined types in native language). `Void` can be omitted, but **description is recommended**.
  - **Argument List:** Comma-separated `{argumentName}: {TypeName}` or `{argumentName}: {TypeName} = {defaultValue}`.
  - **Argument Name:** Use only native language notation; do not attach English hub name. (English notation if English)
  - **Argument Type Name:** Same rules as property type names (Standard types in English, User-defined types in native language).
  - **Default Value (`= {defaultValue}`):**
    - In method definitions, default values can be expressed by appending `= {defaultValue}` after the argument's type name.
    - **Notation for Default Value:**
      - Literals (`True`, `False`, `Null`, numbers, strings) are described as is (**Definitions in `basic_terms.md`**).
      - **Enum Values:** **【Important】Must describe using the native language name** (e.g., `= 赤`, `= 未着手`). Do not describe the English hub name. (English notation if English)
      - Example (Japanese): - \`メソッド名(フラグ: Boolean = True, ステータス: タスク状態 = 未着手): Void\`
      - Example (English): - \`methodName(flag: Boolean = True, status: TaskStatus = NOT_STARTED): Void\` (*Note: Enum value also English if English*)
  - **【Important】Even if there are no arguments, must describe empty parentheses `()`.** (e.g., `methodName()`)
  - **Description:** Follows **【Common Rule】Description of Explanations and Instructions** above.

- **Event Definition:**
  - Format (Native): - \`{EnglishHubName}::{NativeName}({ArgumentList})\`: {Description}
  - Format (English): - \`{EnglishName}({ArgumentList})\`: {Description}
  - **Return Value:** Usually `Void`, but **omitting the description is recommended**.
  - **Argument List:** Follows the same rules as method definition. Argument name, type name, default value are in native language notation (English notation if English).
  - **Argument Name:** Follows the same rules as method definition. Argument name, type name, default value are in native language notation (English notation if English).
  - **【Important】Even if there are no arguments, must describe empty parentheses `()`.** (e.g., `eventName()`)
  - **Description:** Follows **【Common Rule】Description of Explanations and Instructions** above.

- **Enum Definition (Individual):**
  - Must be described under the `#### {Fixed name for enum definitions}` group heading (or within a section under it) in **list format (`-`)**.
  - Format (Native): - \`{EnglishHubName}::{NativeName} = {ValueList}\` \[: {Description}]
  - Format (English): - \`{EnglishName} = {ValueList}\` \[: {Description}]
  - **Separator:** Use `=` (equals sign) between the enum name and the value list.
  - **Value List:** Enumerate values in the format `{EnglishHubName}::{NativeName}` (or English only), separated by commas. Recommending space after comma (e.g., `RED::赤, GREEN::緑`).
  - Backticks: Backticks (\`) start after the space following the hyphen and enclose **up to the end of the value list**. Do not enclose the description text.
  - **Description:** Description can be written after the colon `:` (**optional**). Follows **【Common Rule】Description of Explanations and Instructions** above.

- **Struct Definition (Individual):**
  - Must be described under the `#### {Fixed name for structure definitions}` group heading (or within a section under it) in **list format (`-`)**.
  - Format (Native): - \`{EnglishHubName}::{NativeName}\`: {Description}
  - Format (English): - \`{EnglishName}\`: {Description}
  - **Description:** Description is written after the colon `:` (**required**). Follows **【Common Rule】Description of Explanations and Instructions** above.

    **Guideline for Using Structs**
  - **Simple Data Container Recommended:** Structs are recommended for simple data holding purposes where the AI can infer the content from the name and description, like `Coordinate` struct.
  - **Explicit Definition Discouraged:** Explicitly defining elements using `**Property:**`, etc., like classes, is **strongly discouraged**.
  - **Recommended Specification:** Describe necessary properties in **natural language within the struct's description text** (e.g., "The coordinate struct holds X and Y coordinates"). The AI prioritizes this instruction.

        ```markdown
        記述例（構造体の場合）:
        #### 構造体定義

        *(最も推奨: 短い記載で済む場合)*
        - `RgbColor::Rgb色構造体`: RGB形式の色情報 (赤、緑、青の各値、通常 0-255) を保持します。アルファ値は含みません。
        - `VersionInfo::バージョン情報構造体`: ソフトウェアやコンポーネントのバージョン番号（メジャー、マイナー、パッチ）を格納します。

        *(推奨: 簡易説明に加え、詳細な説明が必要な場合)*
        - `RenderingOptions::描画オプション構造体`: レンダリング時の詳細設定をまとめた構造体です。
          このオプション設定は、リアルタイムレンダリングパイプライン全体に影響します。
          特にアンチエイリアスレベルとテクスチャ品質はパフォーマンスに大きく関わるため、ターゲット環境に応じて慎重に設定してください。
          デフォルト設定については、別ドキュメント「デフォルト描画設定」を参照してください。

        *(プロパティを自然言語で記載する場合)*
        - `Point::座標構造体`: 2次元空間における点の位置を表します。X座標とY座標の2つの数値を持ちます。座標系の原点は左上とします。
        - `Address::住所構造体`: 住所情報を構成する要素を保持します。郵便番号、都道府県、市区町村番地を持ち、オプションで建物名部屋番号を持つことができます。

        *(強く非推奨: プロパティを明確に記載する場合。クラスの使用を検討してください)*
        - `Size::寸法構造体`: オブジェクトの幅と高さを表します。 *(注意: 非推奨の記述方法です。クラスの使用を検討してください)*
          単位はピクセルを基本とします。

          **プロパティ:**
          - `width::幅: Number`: オブジェクトの横幅。
          - `height::高さ: Number`: オブジェクトの縦幅。
        ```

        *(Translator's Note: Japanese example retained for context)*

  - **Using Classes:** If detailed definition of properties or methods is needed, **use a Class** instead of a struct.

- **Implementation of Base Class and Interfaces:**
  - Within the class definition, use the corresponding **Basic Term** in bold notation to indicate the implemented base class or interfaces. Refer to **`basic_terms.md`** for the Basic Terms to use.
  - **Inheritance:**
    - Format (Japanese Example): `**基底クラス:** {BaseClassNameInNative}` (Keyword is Basic Term for `baseclass`)
    - Format (English Example): `**baseclass:** {BaseClassName}` (Keyword is Basic Term for `baseclass`)
    - **【Important】Must reference using only the native language name.**
  - **Interface Implementation:**
    - Format (Japanese Example): `**インターフェース:** {InterfaceName1InNative}, {InterfaceName2InNative}, ...` (Keyword is Basic Term for `Interface`)
    - Format (English Example): `**Interface:** {InterfaceName1}, {InterfaceName2}, ...` (Keyword is Basic Term for `Interface`)
    - **【Important】Must reference using only the native language name.** Use comma separation for multiple specifications.

- **Type References:**
  - When specifying types in properties, arguments, or return values, even when referencing user-defined classes or enums, describe **only the native language name**; do not attach the English hub name.

- **Description Example:**

    ```markdown
    記述例（日本語での定義全体の例）:
    ## com.example.shapes

    このモジュールは、基本的な図形とその操作に関連する定義を含みます。

    ### 定義グループ

    #### 列挙型定義

    - `ShapeType::図形種類列挙型 = CIRCLE::円, RECTANGLE::長方形, TRIANGLE::三角形`: 図形の基本的な種類を示します。
    - `ColorType::色列挙型 = RED::赤, BLUE::青, GREEN::緑, BLACK::黒, WHITE::白`: 図形の色を表します。

    #### 構造体定義

    - `Coordinate::座標構造体`: 2次元空間における点の位置を表します。X座標とY座標の2つの数値を持ちます。

    ### インターフェース定義

    #### 描画可能インターフェース (Drawable): 図形が描画可能であることを示すコントラクト

    このインターフェースを実装するクラスは、自身を描画する機能を持つ必要があります。

    **メソッド:**

    - `draw::描画実行(): Void`: 図形を描画します。具体的な描画処理は実装クラスに依存します。

    ### 基底クラス定義

    #### 基本図形クラス (BaseShape): 全ての図形の基底となるクラス

    図形に共通する基本的なプロパティを提供します。

    **プロパティ:**

    - `id::識別子: UniqueID`: 図形を一意に識別するためのIDです。
    - `creationTime::作成日時: Instant`: この図形オブジェクトが作成された日時（ISO8601形式）です。
    - `shapeType::図形種別: 図形種類列挙型`: 図形の種類を示します。

    ### 図形クラス定義

    #### 円クラス (Circle): 円形を表す図形クラス

    **基底クラス:** 基本図形クラス
    **インターフェース:** 描画可能インターフェース

    このクラスは円を表現し、中心座標と半径を持ちます。基本的な図形操作メソッドを提供します。

    **プロパティ:**

    - `center::中心座標: 座標構造体`: 円の中心点の座標です。
    - `radius::半径: Number`: 円の半径です。負の値は許可されません。
    - `color::色: 色列挙型`: 円を塗りつぶす色です。
    - `isDrawn::描画済みフラグ: Boolean`: 円が既に描画されたかどうかを示すフラグです。
    - `lineStyle::線種: String, オプション`: 円の輪郭線のスタイル（例: 実線、破線）を指定します。指定がない場合はデフォルトの線種が使用されます。
    - `attributes::属性辞書: Dictionary<String, Any>`: 円に関する追加のカスタム属性を格納します。キーは文字列、値は任意型です。
    - `relatedShapes::関連図形リスト: List<UniqueID>`: この円に関連する他の図形の識別子リストです。

    **メソッド:**

    - `calculateArea::面積計算(): Number`: 円の面積を計算して返します。
    - `move::移動(移動先座標: 座標構造体): Void`: 円の中心座標を指定された新しい座標に移動します。
    - `resize::リサイズ(倍率: Number = 1.0): Boolean`: 円の半径を指定された倍率で変更します。成功した場合は真を返します。デフォルト倍率は1.0（変更なし）です。
    - `setColor::色設定(新しい色: 色列挙型 = 赤): Void`: 円の色を指定された新しい色に設定します。デフォルトは赤です。
    - `draw::描画実行(): Void`: 円を描画します。描画可能インターフェースの実装です。描画後、描画済みフラグを真にします。

    **イベント:**

    - `click::クリックイベント()`: 円がクリックされたときに発生します。
    - `sizeChanged::サイズ変更イベント(新半径: Number)`: 円のサイズ（半径）が変更されたときに発生します。新しい半径を引数として渡します。
    - `colorChanged::色変更イベント(旧色: 色列挙型, 新色: 色列挙型)`: 円の色が変更されたときに発生します。変更前の色と変更後の色を引数として渡します。
    ```

    *(Translator's Note: Japanese Markdown block retained as per instruction.)*

    ```markdown
    Description Example (Overall example of definition in English):
    ## com.example.shapes

    This module contains definitions related to basic shapes and their operations.

    ### Definition Groups

    #### Enum Definitions

    - `ShapeType = CIRCLE, RECTANGLE, TRIANGLE`: Indicates the basic types of shapes.
    - `ColorType = RED, BLUE, GREEN, BLACK, WHITE`: Represents the color of a shape.

    #### Structure Definitions

    - `Coordinate`: Represents the position of a point in 2D space. It holds two numeric values: X coordinate and Y coordinate.

    ### Interface Definitions

    #### Drawable: Contract indicating that a shape can be drawn

    Classes implementing this interface must have the capability to draw themselves.

    **Method:**

    - `draw(): Void`: Draws the shape. The specific drawing process depends on the implementing class.

    ### Base Class Definitions

    #### BaseShape: Base class for all shapes

    Provides fundamental properties common to all shapes.

    **Property:**

    - `id: UniqueID`: A unique identifier for the shape.
    - `creationTime: Instant`: The date and time (ISO8601 format) when this shape object was created.
    - `shapeType: ShapeType`: Indicates the type of the shape.

    ### Shape Class Definitions

    #### Circle: Shape class representing a circle

    **baseclass:** BaseShape
    **Interface:** Drawable

    This class represents a circle and holds its center coordinates and radius. It provides basic shape manipulation methods.

    **Property:**

    - `center: Coordinate`: The coordinates of the center point of the circle.
    - `radius: Number`: The radius of the circle. Negative values are not allowed.
    - `color: ColorType`: The color used to fill the circle.
    - `isDrawn: Boolean`: A flag indicating whether the circle has already been drawn.
    - `lineStyle: String, Optional`: Specifies the style of the circle's outline (e.g., solid, dashed). If not specified, a default line style is used.
    - `attributes: Dictionary<String, Any>`: Stores additional custom attributes related to the circle. Keys are strings, values are of any type.
    - `relatedShapes: List<UniqueID>`: A list of identifiers for other shapes related to this circle.

    **Method:**

    - `calculateArea(): Number`: Calculates and returns the area of the circle.
    - `move(destination: Coordinate): Void`: Moves the center of the circle to the specified new coordinates.
    - `resize(scaleFactor: Number = 1.0): Boolean`: Changes the radius of the circle by the specified scale factor. Returns true on success. The default scale factor is 1.0 (no change).
    - `setColor(newColor: ColorType = RED): Void`: Sets the color of the circle to the specified new color. The default is red.
    - `draw(): Void`: Draws the circle. Implementation of the Drawable interface. Sets the isDrawn flag to true after drawing.

    **Event:**

    - `Click()`: Occurs when the circle is clicked.
    - `SizeChanged(newRadius: Number)`: Occurs when the size (radius) of the circle is changed. Passes the new radius as an argument.
    - `ColorChanged(oldColor: ColorType, newColor: ColorType)`: Occurs when the color of the circle is changed. Passes the old color and the new color as arguments.
    ```

#### Output Rules

- If the AI is instructed to output in "Definition Format", it **must enclose the entire OOPD format (Markdown format) output using code blocks "(`~~~Markdown`) ... (`~~~`)"**. (However, code blocks within the OOPD format use "(` ``` `)")
- When outputting instance data, use **YAML format code blocks "(` ```yaml `) ... (` ``` `)"** as the standard. Other formats like JSON may be used if specifically instructed by the user.

#### Definition Format Finalization Process

- Typically, the "Definition Format" is generated by the AI based on content created by the user in "User Format".
- During generation, the AI automatically checks for compliance with the mandatory rules above (English name co-notation, naming conventions, module affiliation, etc.).
- If issues are found during the check (e.g., naming convention violation, unclear English name, undefined module), the AI points out the issues to the user and prompts for correction. The AI may also suggest corrections.
- The "Definition Format" is finalized when the user resolves the issues through dialogue with the AI and confirms/approves the content.

```

```Markdown: sources/formats/format_user.md

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

```
