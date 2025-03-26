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
