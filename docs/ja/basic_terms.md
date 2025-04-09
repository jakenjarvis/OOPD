# OOPD 基本用語定義 (Basic Terms Definition)

このドキュメントは、Object-Oriented Prompt Design (OOPD) における **基本用語 (Basic Terms)** を定義します。基本用語は、OOPDの構造や特定の構成要素を示すための **固定キーワード** であり、プロンプトの記述言語に関わらず、ここで定義された固定表記（または英語表記）が使用され、**翻訳処理は行われません**。

AIは、これらの基本用語を認識し、指定された言語の固定表記（または英語表記）で応答に使用する必要があります。 **【重要】定義された表記以外の揺れは許容されません。**

基本用語は以下のカテゴリに分類されます。

## 1. コア概念 (Core Concepts)

OOPDの基本的な考え方を示す用語です。

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
  "en": "Property", "ja": "プロパティ", "zh-CN": "属性", "zh-TW": "屬性", "es": "Propiedad", "fr": "Propriété", "de": "Eigenschaft", "ko": "속성", "pt": "Propriedade", "ru": "Свойство", "ar": "خاصية", "hi": "प्रॉपर्टी"
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

## 2. フォーマット関連キーワード (Format Keywords)

OOPD形式の構造を示すためのキーワードです。**必ず以下の基本用語で定義された表記を使用してください。**

### 2.1 要素定義キーワード (Element Definition Keywords)

クラスやインターフェース内の要素リストを示すボールド表記のキーワード (`format_common.md` 参照)。
フォーマット仕様書内で、例えばプロパティリストの開始を示す場合は、基本用語 **`Property`** (`ja`: `プロパティ`) を使用します（例: `**プロパティ:**`）。同様にメソッドリストは **`Method`** (`ja`: `メソッド`)、イベントリストは **`Event`** (`ja`: `イベント`) を使用します。

### 2.2 定義グループ見出し (Definition Group Headings)

特定の種類の定義をまとめるための `####` レベルの固定見出し名 (`format_common.md`, `format_definition.md` 参照)。

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

### 2.3 基底クラス/インターフェース指定キーワード (Base Class / Interface Keywords)

クラス定義内で基底クラスや実装インターフェースを示すためのボールド表記のキーワード (`format_definition.md` 参照)。
基底クラスを示す場合は、基本用語 **`baseclass`** (`ja`: `基底クラス`) を使用します（例: `**基底クラス:**`）。実装インターフェースを示す場合は、基本用語 **`Interface`** (`ja`: `インターフェース`) を使用します（例: `**インターフェース:**`）。

```json
{
  "en": "baseclass", "ja": "基底クラス", "zh-CN": "基类", "zh-TW": "基礎類別", "es": "clasebase", "fr": "classebase", "de": "Basisklasse", "ko": "기본클래스", "pt": "classebase", "ru": "базовыйкласс", "ar": "فئةأساسية", "hi": "आधारवर्ग"
}
```

*(Interface は上記のコア概念 `Interface` の定義を使用)*

## 3. 型とリテラル (Types and Literals)

データの種類や固定値を表す用語です。これらは常に **英語表記** で使用されます。

### 3.1 標準型 (Standard Types)

基本的なデータの種類。

```json
{
  "StandardTypes": [
    "String", "Number", "Boolean", "List", "Dictionary", "UniqueID", "Instant", "Void", "Any"
  ]
}
```

*(Note: `List<T>` や `Dictionary<K,V>` の `<>` は型パラメータを示す記法であり、基本用語自体は `List`, `Dictionary` です。)*

### 3.2 リテラル (Literals)

特定の固定値。

```json
{
  "Literals": [
    "True", "False", "Null"
  ]
}
```

### 3.3 拡張型 (Extended Types)

特定のドメインや用途のための意味的な型。詳細な定義は `extended_types.md` を参照してください。これらも常に英語表記で使用されます。

*(Note: 拡張型のリスト自体は `extended_types.md` で管理されるため、ここにはリストを記載しません。AIは `extended_types.md` を参照して拡張型名を基本用語（英語固定）として認識してください。)*

## 4. その他キーワード (Other Keywords)

```json
{
  "en": "Optional", "ja": "オプション", "zh-CN": "可选", "zh-TW": "可選的", "es": "Opcional", "fr": "Optionnel", "de": "Optional", "ko": "선택적", "pt": "Opcional", "ru": "необязательный", "ar": "اختياري", "hi": "वैकल्पिक"
}
```
