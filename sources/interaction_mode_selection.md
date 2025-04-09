## Interaction Mode Selection and Initial Procedure (for Non-English Languages)

### Purpose

This document defines the **initial procedure** for when the AI starts an interaction based on Object-Oriented Prompt Design (OOPD) with the user in a **language other than English**, and the AI's **basic interaction modes** corresponding to the working format selected by the user. These procedures and modes serve as the premise for interpreting and applying subsequent OOPD specifications (especially those related to formats).

**Note:** If the user's language is **English (`en`)**, according to the OOPD specification (see `english_specification.md`), the AI operates in a **strict mode compliant with the Definition Format** at all times, without distinguishing formats. Therefore, the **format confirmation procedure described in this document does not apply** to interactions in English.

### Initial Format Confirmation (Non-English Languages)

If the AI determines that the user has initiated class design, definition, or related operations using OOPD in a **language other than English**, **first confirm the working format** using the following procedure:

1. **Confirmation:** Clearly ask the user, "Will you be working with OOPD using the **User Format** or the **Definition Format**?"
2. **Explanation:** Simultaneously with the question, briefly explain the main features of each format as follows:
   - **User Format:**
     - Primarily described in your native language, allowing for more flexible description.
     - Naming conventions are relatively lenient (AI suggests standard names but doesn't enforce them).
     - English hub names are managed internally by the AI.
     - Suitable for personal use, drafting ideas, and rapid prototyping.
   - **Definition Format:**
     - Requires co-notation of English hub names and adherence to standard naming conventions.
     - Structured, suitable for sharing and reusing definitions.
     - **Especially if you don't insist on specific names yourself, or if you want to efficiently create definitions following standard naming conventions, working in this format, where the AI automatically applies standard names (\*), is recommended.**
       \*(*AI will notify you upon automatic application)*
3. **User Selection:** Accept the user's choice ("User Format" or "Definition Format").

### AI Behavior Modes Based on Format Selection (Non-English Languages)

After the user selects a format, the AI should switch to the **corresponding behavior mode** and interpret/execute subsequent OOPD-related instructions as follows:

- **When User Format Mode is Selected:**
  - The AI performs flexible interpretation based on the User Format specification (see `format_user.md`).
  - If the name specified by the user deviates from standard naming conventions, the AI **only suggests** the standard name and does not confirm usage or automatically apply it. It respects the name used by the user.
  - Follow other rules specific to the User Format.

- **When Definition Format Mode is Selected:**
  - The AI performs strict interpretation and validation based on the Definition Format specification (see `format_definition.md`).
  - If the name specified by the user violates standard naming conventions, the AI calculates the standard name, **notifies the user, and then automatically applies it**.
  - Strictly apply other rules specific to the Definition Format, such as requiring co-notation of English hub names and fully qualified names for cross-module references.

### Changing Modes (Non-English Languages)

The user may wish to change the format during the conversation. The AI should switch modes according to the user's instruction, considering the following points:

- **Changing from User Format to Definition Format:**
  - If the user instructs something like "Convert to Definition Format," the AI reformats the current definition content based on the strict rules of the Definition Format (co-notation of English hub names, application of standard naming conventions, etc.).
  - At this time, the AI performs inference/finalization of English hub names as necessary, and executes validation and automatic application (with notification) of naming conventions.

- **Changing from Definition Format to User Format:**
  - If the user instructs something like "I want to edit in User Format," the AI switches to the following mode:
    - **Format Change:** In displays and responses, omit format elements specific to the Definition Format (like co-notation of English hub names) and match the User Format description style.
    - **Internal Management:** Ensure English hub names are held and managed internally by the AI.
    - **Relaxation of Naming Conventions:** Lift the enforcement of standard naming conventions that were applied in the Definition Format. While using the standard native language names finalized in the Definition Format as a base, the AI allows the user to change those names or use names deviating from standard rules. For subsequent naming convention violations, shift to the mode of only making suggestions (the behavior when User Format is selected).
