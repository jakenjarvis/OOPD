# Object-Oriented Prompt Design (OOPD)

**Note:** [This](https://github.com/jakenjarvis/OOPD) is the original repository for the Object-Oriented Prompt Design (OOPD) concept. Please refer to this repository for the latest updates and ensure proper attribution if reusing.

## Overview

Object-Oriented Prompt Design (OOPD) introduces a novel, structured approach to interacting with Large Language Models (LLMs). By applying familiar principles from Object-Oriented Programming (OOP) to prompt engineering, OOPD empowers users to **design AI instructions and interactions programmatically**. This framework aims to make prompt design significantly more **structured, reusable, maintainable, controllable, precise, and intuitive**, especially for complex or collaborative tasks. Think of it as bringing software engineering best practices to the art of prompt creation.

This repository provides the foundational concepts, terminology, and a recommended structured format (the `OOPD Format`) for implementing OOPD.

## Core Concepts

OOPD enables more sophisticated, reliable, and maintainable communication with AI models through these key ideas:

- **OOP as a Thinking and Design Model:** Leverage well-understood OOP concepts (Classes, Objects, Properties, Methods, etc.) not just as a mental model, but as a **practical design paradigm** for prompts. This allows for systematic structuring of prompt logic, encapsulation of instructions, and definition of interactions, enhancing reusability and maintainability in ways similar to software development. You can essentially "program" the structure of your AI's task and knowledge. **(Core concepts are explained in `sources/core.md`)**
- **Hub Language & Robust Multilingual Support:** Utilize **English (`en`)** as the internal **hub language** for core definitions and ensuring consistency across languages. This allows users to write prompts primarily in their native language (`User Format`) while enabling robust interpretation, translation, and definition sharing (`Definition Format`) via clearly defined rules. See [`sources/localization_overview.md`](sources/localization_overview.md) and the [`sources/translation_rules/`](sources/translation_rules/) directory for details.
- **Precise AI Interpretation Guidance:** Provide explicit instructions to the AI on how to interpret OOP concepts and structures within the prompt context. This includes managing language translation for user-defined terms (while keeping basic terms and types fixed), maintaining consistency, and strictly adhering to constraints like the **prohibition of direct code generation** by default. Key AI instructions are defined in [`sources/core.md`](sources/core.md).
- **Recommended OOPD Format (User & Definition):** This repository proposes a specific **Markdown-based format** (specified in the [`sources/formats/`](sources/formats/) directory) as a clear and effective way to implement OOPD.
  - It features two variations: a flexible **`User Format`** optimized for ease of use in a user's native language, and a stricter **`Definition Format`** which includes English hub names for unambiguous sharing and reusability.
  - The format is designed for human readability, flexibility, and minimizing unintended AI code generation.
  - While this Markdown format is recommended, the core OOPD principles can potentially be applied using other structured representations if the AI can reliably interpret the intended structure and semantics.
- **Centralized Basic Terminology:** Key structural keywords, standard types, literals, and other fixed terms (**Basic Terms**) are centrally defined in **[`sources/basic_terms.md`](sources/basic_terms.md)** to ensure consistency across the entire specification. Optional extended types are defined in **[`sources/extended_types.md`](sources/extended_types.md)**.

## Documentation Structure

This repository contains the complete specification for OOPD. These documents define the standard and provide **instructions for AI systems** on how to interpret and apply it. Key documents include:

- **[`sources/core.md`](sources/core.md):** Explains foundational OOP concepts (as a thinking model), core AI instructions (interpretation rules, translation logic, constraints like code generation prohibition). **Essential reading for understanding the core mechanics and AI behavior.**
- **[`sources/basic_terms.md`](sources/basic_terms.md):** Defines all core **Basic Terms** used in OOPD, including keywords for core concepts, format elements, standard types, and literals. Provides the definitive list of fixed, non-translatable terms and their multi-language representations where applicable.
- **[`sources/english_specification.md`](sources/english_specification.md):** Specifies rules and naming conventions specifically for writing OOPD prompts in English (the hub language).
- **[`sources/localization_overview.md`](sources/localization_overview.md):** Explains the overall strategy for multilingual support, the hub language model, and how translation works within OOPD.
- **[`sources/extended_types.md`](sources/extended_types.md):** Defines optional extended data types (e.g., `Persona`, `Ref`, `CodeBlock`, `Color`) for more specific use cases, enhancing semantic clarity.
- **`sources/formats/` Directory:** Contains the specifications for the recommended Markdown-based OOPD format.
  - **[`sources/formats/format_common.md`](sources/formats/format_common.md):** Basic principles and syntax common to both format variations. References `basic_terms.md` for keywords.
  - **[`sources/formats/format_user.md`](sources/formats/format_user.md):** Specification for the **`User Format`**, designed for ease of use in the user's native language, allowing for more flexible naming.
  - **[`sources/formats/format_definition.md`](sources/formats/format_definition.md):** Specification for the **`Definition Format`**, a stricter format including English hub names alongside standardized native language names, intended for sharing, reusability, and ensuring definition consistency across languages.
- **`sources/translation_rules/` Directory:** Contains language-specific translation rules for AI interpretation.
  - **[`sources/translation_rules/README.md`](sources/translation_rules/README.md):** Explains the structure and purpose of this directory.
  - **[`sources/translation_rules/{language_code}_rules.md`](sources/translation_rules/):** Files defining naming conventions and translation patterns between the English hub and specific target languages (e.g., `ja_rules.md` for Japanese).

(Note: Translated versions of core documents may be provided in separate `/docs/{lang}/` directories in the future, referencing the primary definitions in `sources/`.)

## Dive Deeper

To fully understand OOPD, we recommend exploring the following key documents:

- Start with the core concepts and AI instructions in **[`sources/core.md`](sources/core.md)**.
- Understand the fundamental keywords and types in **[`sources/basic_terms.md`](sources/basic_terms.md)**.
- Learn about the recommended Markdown syntax in the **[`sources/formats/`](sources/formats/)** directory, particularly [`sources/formats/format_common.md`](sources/formats/format_common.md).
- Understand the multilingual strategy in **[`sources/localization_overview.md`](sources/localization_overview.md)**.

## Contributing

Contributions, issues, and feedback are highly welcome! Please feel free to open an issue to discuss potential improvements, report problems, or suggest new language support (especially translation rules).

## License

This project is licensed under the **CC BY 4.0 License**. See the [LICENSE](LICENSE) file for details. Please ensure proper attribution when reusing or adapting this work.
