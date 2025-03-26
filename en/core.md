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
