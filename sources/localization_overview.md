## OOPD Localization Overview

### Overview

This document explains the basic concepts and strategy for multilingual support (localization) in Object-Oriented Prompt Design (OOPD). OOPD aims to enable users worldwide to design prompts in their native language, interact effectively with AI, and share the definitions they create across language barriers.

### Goals

- **Native Language Description:** Users can, in principle, describe OOPD format (especially `User Format`) in their own native language.
- **Definition Sharing:** OOPD definitions (`Definition Format`) created in different languages can be accurately understood and reused by speakers of other languages and AI.
- **AI Interpretation:** AI can accurately interpret the structure and intent of prompts written in the user's native language.
- **Consistent Translation:** AI maintains consistency in the translation of terms and concepts during internal information processing and response generation.

### Hub Language Model

OOPD adopts **English (`en`) as the hub language** to ensure consistency in translation between multiple languages and internal processing.

1. **Input:** User inputs a prompt in their native language.
2. **Internal Conversion:** AI interprets the "User-Defined Identifiers" within the prompt and internally converts/manages them into the English hub language representation.
3. **Processing:** AI's internal thinking, reasoning, and response generation are performed based on this English hub representation.
4. **Output:** AI translates the generated response from the English hub representation into the output language specified by the user (or the input language) and presents it.

### Terminology Classification and Handling

Terms used in OOPD are classified into two types from a translation perspective (see `core.md`).

- **Basic Terms:** Core concepts defining the structure of OOPD, such as `Class`, `Method`, `Property`. These are **fixed keywords** and are **not translated**. The fixed notation defined for each language is used as is. Standard Types, Extended Types, and Literals are treated similarly and always use their English notation.
- **User-Defined Identifiers:** Class names, interface names, method names, property names, event names, enum definition names, enum values, etc., defined by the user. These are **subject to the translation process** by the AI.

### Translation Process

The AI's translation process is performed based on the following principles and rules:

- **Target:** Only "User-Defined Identifiers" included in the structural definitions within the prompt.
- **Timing:**
  - **Input Interpretation:** Inferring/converting content described in the native language to the English hub language.
  - **Initial Name Determination:** Can infer the optimal English name by referencing descriptions and context.
  - **Response Generation:** Translating from the English hub language to the specified output language. Descriptions are not referenced when translating finalized definitions (for reversibility).
- **Ensuring Consistency (Session Memory):**
  - The AI **remembers the correspondence between User-Defined Identifiers and their English hub names within the session**. *(Refer to `core.md` for the definition of a session)*.
  - If the same User-Defined Identifier (or an expression the AI deems synonymous) appears within the same session, it **must use the remembered English hub name** to prevent translation fluctuations. This takes highest priority.
- **Translation Rules:**
  - Translation is performed based on **naming conventions** and **translation patterns** defined for each language pair. Refer to the respective language rule files (`{language_code}_rules.md`) in the `translation_rules` directory for details.
  - **Cross-lingual Concept Mapping:** For terms representing the same concept in different languages, the AI strives to map them to a common English hub name based on semantic similarity, referencing class definitions, descriptions, and translation rules for each language.
  - **Handling Expression Correspondences (N-to-N, 1-to-N, N-to-1):**
    - **N-to-N (Recommended):** If expressions have different nuances between the hub language and the target language (e.g., `isCompleted` vs. `hasFinished` in the hub language), define corresponding distinct standard translations (`xx_StandardTranslation1` and `xx_StandardTranslation2`) in the target language `xx` whenever possible. This helps maintain the information content across languages.
    - **1-to-N (Caution):** If a single word `TermA` in the hub language can be interpreted in multiple ways (`xx_TranslationB`, `xx_TranslationC`) in the target language `xx` depending on context, translating differently can risk not reverting to `TermA` upon reverse translation. In this case, either define a single most representative standard translation `xx_TranslationB`, or recommend using more specific expressions in the hub language like `TermA_Context1`, `TermA_Context2`.
    - **N-to-1 (Acceptable):** Conversely, if synonyms `TermX` and `TermY` in the hub language are difficult or unnatural to distinguish in the target language `xx`, they may be **aggregated into a single standard translation** `xx_StandardTranslationZ` in the target language.
  - **Standardization from Target Language to Hub Language:** When converting from a target language `xx` to the English hub, if expressions `xx_Expression1` and `xx_Expression2` in the target language refer to the same concept, strive to generate **a single standard English hub name**, such as `HubTermAlpha`. This maintains consistency in expression within the English hub language.
- **Core Translation List:**
  - **Generally Unnecessary.** Basic words are also left to translation based on rules and the AI's language capabilities.
  - **Exceptions:** For a very small vocabulary where notation variations must absolutely be avoided, such as literals (`True`, `False`, `Null` are fixed to English notation), fixed translations are defined exceptionally.
- **Role of AI Inference:**
  - For unknown vocabulary or complex expressions not covered by rules or (exceptional) core lists, the AI **infers** the optimal translation based on context and language knowledge.
  - The AI also adjusts the naturalness of the translation result (e.g., word order, conjugation).
- **Natural Language Parsing Suitability:** Translation rules consider ensuring that the generated target language names become words/phrases easily identifiable by the AI as part of natural language instructions within that language's grammatical structure (e.g., avoiding unnatural particle inclusion).

### Limiting Translation Scope

The AI's translation process is limited to the structural definition parts of the OOPD format (class names, method names, etc.). The **content body (stories, reports, etc.)** that the user asks the AI to generate is **not subject to translation**.

### Regarding Reversibility

OOPD emphasizes that the meaning of definitions should not change between different languages (**semantic reversibility**), especially in the `Definition Format`.

- Since the `Definition Format` lists the English hub name alongside the native name, identity at the hub language level is always guaranteed.
- However, due to the translation rules mentioned above (especially N-to-1 and standardization from target language to hub), note that translating from one language to another and back to the original language **may not guarantee perfect matching at the lexical level (word level)**.
- The goal is purely **"semantic reversibility,"** where the intent and structure of the definition remain unchanged.

### Format and Translation

- **User Format:** Described only in the native language. AI internally infers and manages English hub names.
- **Definition Format:** Lists standardized native language names alongside finalized English hub names. Shareable between languages. This format enables definition conversion between different languages.

### Contribution

Contributions for supporting new languages (creating translation rules) or improving existing rules are welcome. The language files under the `translation_rules` directory are key to the accuracy and quality of translation.
