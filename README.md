# Object-Oriented Prompt Design (OOPD)

**Note:** This is the original repository for the Object-Oriented Prompt Design (OOPD) concept. Please refer to this repository for the latest updates and ensure proper attribution if reusing.

## Overview

Object-Oriented Prompt Design (OOPD) introduces a novel approach to interacting with Large Language Models (LLMs) by applying principles from Object-Oriented Programming (OOP) to prompt engineering. This framework aims to make prompt design more **structured, reusable, maintainable, and intuitive**, especially for complex tasks.

This repository provides the foundational terminology and a structured format (`OOPD Format`) for implementing OOPD.

## Core Concepts

OOPD enables more sophisticated communication with AI models through these key ideas:

- **OOP as a Thinking Model:** Leverage familiar OOP concepts (Classes, Objects, Properties, Methods, etc.) as a **mental model** for designing prompts. This allows for systematic structuring of prompt logic, enhancing reusability and maintainability, much like in software development.
- **Hub Language & Multilingual Support:** Utilize **English (`en`)** as the internal **hub language** for core definitions and consistency. This allows users to write prompts in their native language while facilitating interpretation and translation via defined rules.
- **AI Interpretation Guidance:** Instruct the AI on how to interpret these OOP concepts and structures within the prompt context, manage language translation for defined terms, and maintain consistency—**without generating programming code** by default.
- **Recommended Format (`OOPD Format`):** This repository proposes a specific **Markdown-based format** (`OOPD Format`, detailed in `format.md`) as a clear and recommended way to implement the OOPD thinking model. It is designed for readability, flexibility, and to minimize the risk of unintended code generation by the AI (see `core.md` for AI interpretation details). While the core principle is effective communication of the structure, this format provides a practical starting point. (If the AI can reliably interpret the design, other structured representations **can also be used** in principle.)

## Documentation Structure

This repository contains detailed definitions and format specifications in multiple languages, organized as follows. These documents define the OOPD standard and also **instruct AI systems on how to interpret and apply it.**

- **`/en` Directory:** Core definitions, format specifications, and system instructions in **English**.
  - [en/core.md](en/core.md): Foundational OOP terminology and **core instructions dictating the AI's thinking framework and interpretation rules.**
  - [en/format.md](en/format.md): Specific `OOPD Format` syntax **that guides AI in parsing structured prompts.**
  - [en/system_instructions.md](en/system_instructions.md): Instructions for AI to load `core.md` and `format.md` via URLs (for capable AIs).
  - [en/system_instructions_consolidated.md](en/system_instructions_consolidated.md): A combined version of `core.md` and `format.md` for AIs that cannot load URLs.

- **`/ja` Directory:** Core definitions, format specifications, and system instructions in **Japanese**.
  - [ja/core.md](ja/core.md): 日本語での用語定義と、**AIの思考フレームワークと解釈ルールを指示するコア指示。**
  - [ja/format.md](ja/format.md): **構造化プロンプトを解析する際にAIをガイドする** 、日本語でのOOPD形式の書き方。
  - [ja/system_instructions.md](ja/system_instructions.md): AIがURL経由で `core.md` と `format.md` を読み込むための指示（対応可能なAI向け）。
  - [ja/system_instructions_consolidated.md](ja/system_instructions_consolidated.md): URLを読み込めないAI向けに、`core.md` と `format.md` を結合したもの。

*(Potentially other language directories in the future)*

## Dive Deeper

Choose your preferred language to explore the detailed specifications:

- [English Documentation](readme-en.md)
- [日本語ドキュメント (Japanese Documentation)](readme-ja.md)

## Contributing

Contributions, issues, and feedback are welcome! Please feel free to open an issue to discuss potential improvements or report problems.

## License

This project is licensed under the **CC BY 4.0 License**. See the [LICENSE](LICENSE) file for details.
