# Sphinx and Gettext PO Rules

These rules are mandatory for all tasks that modify Sphinx gettext `.po` files.

Detailed translation workflow, quality control, batch processing, and validation procedures are defined by the relevant translation skill.

## PO File Integrity

When modifying `.po` files:

* `msgid` is canonical source content and MUST NEVER be modified.
* Translations MUST be written only to the corresponding `msgstr`.
* Preserve PO comments, metadata, source references, flags, and entry order unless a specific task requires a justified change.
* Preserve valid gettext syntax.
* Do not delete PO entries unless explicitly requested.
* Avoid rewriting or reformatting unrelated entries.

## Existing Translations

Unless the current task explicitly includes review, correction, or retranslation:

* preserve non-empty `msgstr` values
* translate only eligible empty or requested entries

Do not overwrite valid existing translations as a side effect of another task.

## Fuzzy Entries

Entries marked with `#, fuzzy` require explicit review before the flag may be removed.

Remove `fuzzy` only when:

* the current `msgid` has been reviewed against `msgstr`
* the translation accurately matches the current source
* protected syntax and placeholders are valid

Do not remove unrelated PO flags.

## Sphinx and reStructuredText Integrity

Preserve all syntax required by Sphinx and reStructuredText.

This includes:

* roles
* directives
* reference targets
* anchors
* substitutions
* inline literals
* code blocks
* literal blocks
* markup delimiters

For references containing visible text and a target, only the visible human-readable text may be translated.

Example:

`:ref:\`Motor driver <motor-driver>``

may become:

`:ref:\`Драйвер двигуна <motor-driver>``

The target `motor-driver` MUST remain unchanged.

This applies to roles including, but not limited to:

* `:doc:`
* `:ref:`
* `:class:`
* `:func:`
* `:meth:`
* `:mod:`
* `:download:`

Never translate identifiers required for Sphinx reference resolution.

## Placeholders

Every placeholder present in `msgid` MUST be preserved exactly in `msgstr`.

Examples include:

* `{name}`
* `{value}`
* `${variable}`
* `%s`
* `%d`
* `%(name)s`

Do not:

* rename placeholders
* remove placeholders
* duplicate placeholders accidentally
* alter placeholder syntax

## Code and Technical Identifiers

Do not translate or modify:

* source code
* shell commands
* function names
* class names
* variable names
* API identifiers
* package names
* configuration keys
* file names
* directory paths
* hardware model numbers
* URLs
* reference identifiers

Inline code and literals must preserve their exact technical content.

## Links and References

Preserve:

* URLs
* link targets
* reference identifiers
* anchors

When a construct contains both visible text and a technical target:

* visible human-readable text may be translated
* the target MUST remain unchanged

## PO Escaping

Preserve valid gettext escaping, including:

* escaped quotes
* backslashes
* newline escapes
* multiline string syntax

Never introduce invalid PO syntax.

## Scope Safety

Modify only entries required by the current task.

Do not perform unrelated:

* translation cleanup
* reformatting
* source documentation changes
* code changes
* generated-file modifications

If an apparent problem exists in `msgid`, do not fix it inside the `.po` file. Report the source issue separately.

## Non-Negotiable Invariants

For every modified translation:

1. `msgid` remains unchanged.
2. Required placeholders remain unchanged.
3. Sphinx reference targets remain unchanged.
4. Technical identifiers remain unchanged.
5. PO syntax remains valid.
6. Changes remain within the requested scope.

These invariants take priority over translation style or wording preferences.
