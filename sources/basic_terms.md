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
