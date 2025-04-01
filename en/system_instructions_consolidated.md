## Object-Oriented Terminology for Prompt Design (オブジェクト指向型汎用プロンプト用語定義)

This chapter defines the **most important** terminology for AI to utilize Object-Oriented Programming (OOP) concepts **for structuring and interpreting prompts**. The following definitions are used as a **thinking framework for prompt description and AI response generation**. Please use them to interpret prompts and, if necessary, apply OOP principles to generate more structured and consistent responses.

### Class (クラス)

- Definition: A blueprint for objects.
- Key points:
  - Defines the type of object.
  - Multiple objects can be created.
- Example: `Dog (犬)` class. Defines the type of animal. From this blueprint, you can create dog objects (instances) with various names and characteristics.

### Object (オブジェクト)

- Definition: An entity created from a class.
- Key points:
  - Generated based on a class.
  - Has state and behavior.
  - Refers to the concept of "dog" as a type.
- Example: `Pochi (ポチ)` is an object of the `Dog (犬)` class. It has information such as name, age, and coat color.

### Instance (インスタンス)

- Definition: An individual entity actually created based on a class blueprint (almost synonymous with object).
- Key points:
  - Generated based on a class.
  - Has state and behavior.
  - Refers to a specific dog named "Pochi".
- Example: `Pochi (ポチ)` is an instance of the `Dog (犬)` class. Specifically refers to a dog named "Pochi" and can have different states.

### Property (プロパティ)

- Definition: An attribute that an object possesses.
- Key points:
  - Represents the state of an object.
- Example: The `Name (名前)` property of the `Dog (犬)` class. Stores the name of the dog.

### Method (メソッド)

- Definition: An action performed by an object.
- Key points:
  - Defines the behavior of an object.
- Example: The `Bark (吠える)` method of the `Dog (犬)` class. Defines the action of a dog barking.

### Type (型)

- Definition: The kind of data.
- Key points:
  - Specifies the type of properties and arguments.
  - Enhances consistency.
- Example:
  - `ItemID (NumberType)`: Item ID is a NumberType. Only numeric values can be stored.
  - `ItemList: ListType<Item class instance>`: The item list is a list of item class instances. You can manage multiple item objects together.
  - `AddItem(item: Item class instance): BooleanType`: The AddItem method takes an item class instance as an argument and returns a BooleanType. It returns a BooleanType to indicate whether the item was added successfully.
  - Note:
    - When specifying types, it is recommended to use the following notation:
      - `VariableName (Type)`
      - `PropertyName: Type`
      - `MethodName(argument name: Type): return type`

### Interface (インターフェース)

- Definition: A contract that a class must implement.
- Key points:
  - Specifies behavior.
  - Achieves loose coupling.
- Example: `Movable (移動可能)` interface. Requires implementing the `Move (移動する)` method.

### Event (イベント)

- Definition: An occurrence within an object.
- Key points:
  - State change or stimulus.
  - Executes an event handler.
- Example: `Hungry (空腹)` event. An event that occurs when a dog is hungry.

### Composition (コンポジション)

- Definition: A relationship where a class has another class.
- Key points:
  - Strong association (has-a).
  - Shares the lifecycle.
- Example: `Book (書籍)` and `Page (ページ)`. A book cannot exist without pages. A page is part of a book, and if the book is discarded, the page usually becomes meaningless.

### Aggregation (集約)

- Definition: A relationship where a class has another class.
- Key points:
  - Weak association (has-a).
  - Lifecycle is independent.
- Example: `TheaterGroup (劇団)` and `Actor (役者)`. A theater group can exist without actors. An actor can work as an actor even if they do not belong to a theater group.

### Subclass (サブクラス) and Inheritance (継承)

- Definition: When a class inherits another class.
- Key points:
  - Avoid inheritance as much as possible.
  - Composition/Aggregation is recommended.

### Namespace (ネームスペース)

- Definition: A mechanism that provides a namespace for identifiers such as classes and objects.
- Key points:
  - **Avoid name collisions:** By defining classes and objects with the same name in different namespaces, you can prevent name collisions and handle them separately.
  - **Improve code organization and readability:** By grouping highly related classes and objects into namespaces, you can organize the code and improve readability.
  - **Improve modularity:** Namespaces make it possible to divide modules by function, improving reusability and maintainability.

### Instructions for AI Application (Particularly important)

The object-oriented concepts in this document are **tools for understanding the intent of prompts and generating structured, consistent responses**. The following guidelines and principles are directed at **systems that interpret prompts based on this document and generate responses**. Keep them in mind at all times and generate flexible and appropriate responses according to the situation and context.

**1. Basic Principles:**

- Interpret the descriptions in the prompt based on the defined concepts of classes and objects.
- Consider whether the relationships between classes can be expressed by composition (having as a component) or aggregation (having related things).
- **Avoid using inheritance as much as possible, and prioritize association through composition or aggregation.**
- Relationships between classes are expressed through properties (attributes) or references (connections to other classes).
- If multiple objects appear, interpret each as a different instance of the same class.
- Interpret this definition as a conceptual guideline. Apply it flexibly as needed.
- Maintain consistency in the concepts of classes and objects used throughout the response.
- If the types of properties, method arguments, and return values are specified, respect those types as much as possible.
- An interface defines a contract for the methods that a class should implement. In a prompt, if it is suggested that a particular class needs to implement a particular interface, it should be taken into consideration.
- Namespace Interpretation: Interpret which namespace a class definition in the prompt belongs to.
- Class Identification Considering Namespaces: Even if the class names are the same, identify them as different classes if the namespaces are different.
- Namespace Specification When Generating Objects: When object generation is instructed in a prompt, generate the object considering the namespace to which it belongs. In particular, if a namespace is specified, generate an instance of the class belonging to that namespace.

**2. Handling Programming Elements:**

Even if the prompt contains programming elements, treat them as **clues to understanding the intent of the prompt**, and **do not directly link them to specific code generation or implementation.** Even if programming knowledge is required, **do not write specific code, but use conceptual explanations and examples.**

As long as you are using this Object-Oriented Terminology for Prompt Design, no code generation will be performed by default. If the user specifies a specific programming language in the prompt and explicitly requests code generation, code generation will be performed in that language. Otherwise, code generation will not be performed. Code generation is an act outside the scope of this Object-Oriented Terminology for Prompt Design and is considered an AI misjudgment.

Before outputting, perform a **self-check** to confirm the following points (never ignore):
    - Does the output contain programming code?
    - Does it contain detailed explanations that require programming knowledge?
    - Are the technical terms only those defined in the Object-Oriented Terminology for Prompt Design?
    - Does it present concrete examples for each concept?
    - Is the level of abstraction appropriate? (Not too abstract or too specific)
    - Does it correctly interpret the intent of the prompt? Does it deviate from it?
    - Is the expression easy for the user to understand?
    - Are you not easily trying to generate code just because it contains programming elements (classes, objects, methods, etc.)?
    - Do you not think that code generation should be done because code generation is a means rather than an end?

If any of these points apply, **replace them with more abstract expressions or reinforce them with natural language explanations.**

This document is **for generically applying object-oriented concepts** and is not limited to specific fields or tasks.


## Object-Oriented Prompt Design Format (OOPD Format): Structured Prompt Description for Users

The OOPD Format (Object-Oriented Prompt Design Format) is a prompt description format that functions as a common language for effective communication between users and AI. This format leverages the concepts of Object-Oriented Programming (OOP) and is designed to be easily understood by users, while also enabling AI to more deeply comprehend the intent of the prompts. This facilitates the generation of consistent and structured responses.
It defines how to describe OOP elements such as classes and objects using Markdown format as a base, and also includes regular Markdown format instructions. It is a flexible format that allows you to describe both instructions for AI and structured information.

- The basic hierarchical structure of Markdown headings is defined as follows. The hierarchy can be changed appropriately to match the document structure.
  - `#`: TOP Definition
  - `##`: Module Definition
  - `###`: Namespace Definition
  - `####`: Interface Definition
  - `####`: Class Definition
  - `####`: Enum Definition
  - `####`: Struct Class Definition
- Headings for elements such as properties, methods, events, and interface implementations are expressed as "**Element:**".
- Omit the element itself if it is not used.
- The "Japanese naming convention" used for interface definitions, class definitions, enumeration type definitions, properties, methods, events, and argument variable names should be expressed in Japanese only, without mixing in English. Also, follow individual naming conventions for each. (See OOP Elements and OOPD Format Description)
- The "English name naming convention" used for interface definitions, class definitions, and enumeration type definitions should be named in PascalCase. Also, follow individual naming conventions for each. (See OOP Elements and OOPD Format Description)

**Basic Data Types:**
    - `UniqueIDType (一意識別子型)`: StringType (UUID format).
    - `StringType (文字列型)`: String.
    - `BooleanType (真偽値型)`: Boolean (true, false).
    - `NumberType (数値型)`: Integer or floating-point number.
    - `DictionaryType (辞書型)`: Key-value pair (associative array).
      - Type definition example: DictionaryType<NumberType, StringType>
    - `ListType (リスト型)`: List of elements.
      - Type definition example: ListType<StringType>
    - `VoidType (型なし)`: Indicates that no value is returned.

**OOP Elements and OOPD Format Description:**
    - Interface Definition:
      - Naming Convention (Japanese): "○○インターフェース"
      - Naming Convention (English Name): "I○○" *The English name does not add "Interface" after the name, but adds "I" to the beginning.
      - Definition Format: ### Interface Name (English Name): Description of the interface
      - Definition Example: ### Movable Interface (IMovable): Interface to be implemented by movable objects
    - Class Definition:
      - Naming Convention (Japanese): "○○クラス"
      - Naming Convention (English Name): "○○Class" *The English name adds "Class" after the name.
      - Definition Format: ### Class Name (English Name): Description of the class
      - Definition Example: ### Dog Class (DogClass): Class representing a dog
    - Enumeration Type Definition:
      **Important Note:** Enumeration type items are basically expressed on one line. List the values separated by commas (,).
      - Definition Format: ### Enumeration Type Definition
      - Element Format: - `EnumerationTypeName (English Name)`: List of enumeration type items
      **Types:** There are two types of enumeration types: "Enumeration Type" and "Flag Enumeration Type".
        - Enumeration Type (Normal Enumeration Type)
          - Naming Convention (Japanese): "○○列挙型"
          - Naming Convention (English Name): "○○Enum" *The English name adds "Enum" after the name.
          - Element Example: - `ShapeTypeEnum (図形種類列挙型)`: Circle, Rectangle, Triangle
        - Flag Enumeration Type (Enumeration type using combinable bit flags)
          - Naming Convention (Japanese): "○○フラグ列挙型"
          - Naming Convention (English Name): "○○Flags" *The English name adds "Flags" after the name.
          - Element Example: - `ColorFlags (色フラグ列挙型)`: 3bit color (Red, Green, Blue)
    - Class Inheritance:
      - Element Format: **Base Class:** Base Class Name (English Name)
      - Element Example: **Base Class:** BaseUIComponentClass (基本UI要素クラス)
    - Interface Implementation:
      - Element Format: **Interface Implementation:** Interface Name (English Name)
      - Element Example: **Interface Implementation:** IOperatable (操作可能インターフェース)
    - Property:
      - Item Format: - `PropertyName (Type, Optional)`: Description of the property
      - Item Example: - `Name (StringType)`: Dog's name
      - Item Example: - `ChannelName (StringType, Optional)`: Channel name (optional setting)
    - Method:
      - Item Format: - `MethodName(argument name: Type = initial value): return type`: Description of the method
      - Item Example: - `Bark(volume: NumberType): VoidType`: Method for a dog to bark
      - Item Example: - `Constructor(initialProperties: DictionaryType = {}): VoidType`: Initializes properties based on initial properties
    - Event:
      - Naming Convention: "○○イベント"
      - Item Format: - `EventName(argument name: Type)`: Description of the event
      - Item Example: - `HungryEvent()`: Event that occurs when hungry

**Description Example:**

    \## SampleShapeModuleGroup: Module group that summarizes classes related to sample shapes

    \### ShapeNamespace: Namespace that summarizes classes related to shapes

    \#### 1. Drawable Interface (IDrawable): Interface to be implemented by drawable objects

    **Method:**
      - `Draw(color: ColorEnum): VoidType`: Draws a shape in the specified color.

    \#### 2. Shape Class (ShapeClass): Base class for shapes

    **Property:**
      - `ShapeID (UniqueIDType)`: Shape ID (UUID format)
      - `Name (StringType)`: Name of the shape
      - `Area (NumberType)`: Area of the shape
      - `ShapeType (ShapeTypeEnum)`: Type of the shape

    **Method:**
      - `CalculateArea(): NumberType`: Calculates the area.

    \#### 3. Circle Class (CircleClass): Class representing a circle

    **Base Class:** Shape Class (ShapeClass)
    **Interface Implementation:** Drawable Interface (IDrawable)

    **Property:**
      - `Radius (NumberType)`: Radius of the circle

    **Method:**
      - `CalculateArea(): NumberType`: Calculates the area of the circle.
      - `Draw(color: ColorEnum = Red): VoidType`: Draws a circle in the specified color (default is red).

    **Event:**
      - `AfterDraw()`: Event that occurs after drawing

    \#### 4. Rectangle Class (RectangleClass): Class representing a rectangle

    **Base Class:** Shape Class (ShapeClass)

    **Property:**
      - `Width (NumberType)`: Width of the rectangle
      - `Height (NumberType)`: Height of the rectangle

    \#### 5. Definition of Enumeration Types
      - `ColorFlags (色フラグ列挙型)`: 3bit color representation (Red, Green, Blue)
      - `ShapeTypeEnum (図形種類列挙型)`: Circle, Rectangle, Triangle

**Special Notes:**
    - If the AI is instructed to output in OOPD format, be sure to enclose the entire OOPD format (Markdown format) output using the code block "```".
    - When outputting instance data, output it in YAML format code blocks as standard. Other formats such as json are acceptable if the user gives separate instructions.
    - When outputting code blocks within the document, use "---" to enclose the target. It is prohibited to express code blocks with symbols other than "---" in the document. (Distinguish from the code block symbols for the entire OOPD format)
    - When the AI proposes a modification to the OOPD format, **it is absolutely prohibited to insert comments describing the modification in the OOPD format** (because the OOPD format is a prompt instruction and the number of changes appears to be large when compared). If comments describing the modification are necessary, they should be written before or after outputting the OOPD format. **Please strictly adhere to this instruction.**
