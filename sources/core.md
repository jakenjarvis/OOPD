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
