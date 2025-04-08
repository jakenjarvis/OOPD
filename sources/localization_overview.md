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
