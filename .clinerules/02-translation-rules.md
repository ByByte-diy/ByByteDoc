# Translation Rules

## Primary Task

Translate documentation from English into the target language specified by the user or determined from the localization directory.

Translate only content intended for human readers.

Do not modify source documentation unless explicitly requested.

## Translation Quality

Translations must:

* sound natural to a native speaker
* preserve the exact technical meaning
* use terminology commonly used by the target-language technical community
* remain understandable to beginners
* maintain consistent terminology across files
* preserve the tone and level of formality of the source

Avoid:

* word-for-word translation when it sounds unnatural
* invented terminology
* unnecessary transliteration
* translating established technical names that are normally used in English
* adding explanations that are absent from the source
* removing information
* summarizing the source

## Context Awareness

Never translate an isolated sentence blindly when surrounding context is available.

Before translating:

1. Read the complete translation unit.
2. Inspect surrounding entries when necessary.
3. Determine whether the text is a heading, instruction, warning, UI label, description, or technical explanation.
4. Check existing translations for established terminology.

Use existing project terminology consistently.

If the same English technical term already has an established translation in the project, prefer that translation unless it is clearly incorrect.

## Technical Content

Preserve without translation unless context explicitly requires otherwise:

* source code
* commands
* file names
* directory paths
* package names
* API names
* class names
* function names
* variable names
* configuration keys
* hardware part numbers
* protocol names
* URLs
* email addresses

Inline code must retain its exact contents.

Examples:

`digitalWrite()`
`setup()`
`loop()`
`HC-05`
`DRV8833`
`WS2813`
`/dev/ttyUSB0`

## Formatting

Preserve:

* paragraph structure
* lists
* emphasis
* inline code
* code blocks
* links
* references
* placeholders
* punctuation required by markup syntax

Do not convert markup into plain text.

## Consistency

Before choosing a translation for an important technical term:

1. Search existing translations in the project.
2. Reuse the established translation when appropriate.
3. Keep the same term consistent across related documentation.

Do not alternate between multiple translations of the same technical concept without a semantic reason.

## Ambiguity

If a source phrase is genuinely ambiguous and the surrounding project context does not resolve it:

* do not invent technical meaning
* preserve the safest semantically accurate interpretation
* inform the user when the ambiguity could materially affect the translation

## Scope Control

Translate only the files or entries requested by the user.

Do not perform unrelated refactoring, formatting, cleanup, or source-code changes.

Do not modify generated files unless explicitly requested.
