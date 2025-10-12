# Translation Workflow (EN / UK / RU)
# Робочий процес перекладу
# Рабочий процесс перевода

---

## Overview / Огляд / Обзор
This guide merges two approaches:
- Method A: Sphinx gettext/PO + Poedit (recommended for production)
- Method B: AI‑assisted translation → import to PO → QA

Цей посібник об’єднує два підходи:
- Метод A: Sphinx gettext/PO + Poedit (рекомендовано для продакшну)
- Метод B: Переклад за допомогою ШІ → імпорт у PO → перевірка

Это руководство объединяет два подхода:
- Метод A: Sphinx gettext/PO + Poedit (рекомендуется для продакшна)
- Метод B: Перевод с помощью ИИ → импорт в PO → проверка

---

## Prerequisites / Необхідні умови / Предварительные условия
- Sphinx, sphinx‑intl (див. / см. `docs/requirements.txt`)
- Glossary / Глосарій / Глоссарий: `docs/_static/glossary.yaml`
- Keep RST roles/targets intact; don’t translate code/pins/filenames
  Зберігайте RST‑ролі/цілі; не перекладайте код/піни/імена файлів
  Сохраняйте RST‑роли/цели; не переводите код/пины/имена файлов

---

## Method A — gettext/PO (Manual/Poedit)
### EN
1) Extract messages
```bash
scripts/i18n_sync.sh gettext
```
2) Update catalogs
```bash
scripts/i18n_sync.sh update
```
3) Translate `.po` in `docs/locale/{uk,ru}/LC_MESSAGES/...`
4) Optional normalize
```bash
scripts/i18n_sync.sh fixpo
scripts/i18n_sync.sh clean-suffix
```
5) Build
```bash
scripts/i18n_sync.sh build uk
scripts/i18n_sync.sh build ru
```

### UK
1) Витягнути рядки → `scripts/i18n_sync.sh gettext`
2) Оновити каталоги → `scripts/i18n_sync.sh update`
3) Перекладати `.po` у `docs/locale/{uk,ru}/LC_MESSAGES/...`
4) Нормалізувати (опційно) → `fixpo`, `clean-suffix`
5) Збірка → `build uk`, `build ru`

### RU
1) Извлечь строки → `scripts/i18n_sync.sh gettext`
2) Обновить каталоги → `scripts/i18n_sync.sh update`
3) Переводить `.po` в `docs/locale/{uk,ru}/LC_MESSAGES/...`
4) Нормализовать (опц.) → `fixpo`, `clean-suffix`
5) Сборка → `build uk`, `build ru`

---

## Method B — AI → Import to PO → QA
### EN
1) Prepare localized RST drafts (uk/ru) per section; keep RST/roles/code intact
2) Import to PO
```bash
scripts/i18n_sync.sh import
```
(Importer fills only empty msgstr; positional + normalized mapping)
3) Normalize (optional)
```bash
scripts/i18n_sync.sh fixpo
scripts/i18n_sync.sh clean-suffix
```
4) Remove `#, fuzzy` if needed; Build `build uk|ru`
5) Delete temporary localized RST drafts from `docs/` to avoid toctree warnings

### UK
1) Підготуйте локалізовані RST‑чернетки (uk/ru); зберігайте RST/ролі/код
2) Імпорт у PO → `scripts/i18n_sync.sh import` (заповнює лише порожні msgstr)
3) Нормалізація → `fixpo`, `clean-suffix`
4) Прибрати `#, fuzzy` за потреби; збірка `build uk|ru`
5) Видалити тимчасові локалізовані RST з `docs/`

### RU
1) Подготовьте локализованные RST‑черновики (uk/ru); сохраняйте RST/роли/код
2) Импорт в PO → `scripts/i18n_sync.sh import` (заполняет только пустые msgstr)
3) Нормализация → `fixpo`, `clean-suffix`
4) Удалить `#, fuzzy` при необходимости; сборка `build uk|ru`
5) Удалить временные локализованные RST из `docs/`

---

## Links & Targets / Посилання та цілі / Ссылки и цели
- Prefer `:ref:` with labels; for `:doc:` use valid paths (e.g. `:doc:`contributing/index``)
- If warnings “unknown document” appear, fix targets in `.po` (don’t translate the target!)

---

## Quick Reference / Швидкі команди / Быстрые команды
```bash
# Extract & update
scripts/i18n_sync.sh gettext && scripts/i18n_sync.sh update

# Import AI drafts → PO, then normalize
scripts/i18n_sync.sh import
scripts/i18n_sync.sh fixpo && scripts/i18n_sync.sh clean-suffix

# Build
scripts/i18n_sync.sh build uk
scripts/i18n_sync.sh build ru

# QA
msgfmt -c -v docs/locale/uk/LC_MESSAGES/*.po
grep -c '^msgstr ""$' docs/locale/uk/LC_MESSAGES/**/*.po || true
```

---

## Troubleshooting / Усунення проблем / Устранение проблем
- Unknown document: replace/restore `:doc:` target or switch to `:ref:`
- Fuzzy entries: remove `#, fuzzy` before build
- Toctree warnings (localized RST): delete temporary drafts from `docs/`

## CLI: import_translations.py (unified)

The importer now accepts docs-relative RST paths and computes localized targets automatically for both uk and ru.

- Input: source RST under `docs/` (e.g. `platforms/nano/index.rst`)
- Computed per locale:
  - localized RST: `platforms/nano/index.{locale}.rst`
  - PO path: `docs/locale/{locale}/LC_MESSAGES/platforms/nano/index.po`
- Behavior: fills only empty `msgstr` entries; does not overwrite existing translations.

Examples:
```bash
# Import one file
python3 scripts/import_translations.py platforms/nano/index.rst

# Import multiple files at once
python3 scripts/import_translations.py \
  platforms/nano/index.rst \
  platforms/nano/spec.rst \
  platforms/nano/faq.rst
```

Tip: pair with the i18n helper
```bash
scripts/i18n_sync.sh gettext && scripts/i18n_sync.sh update
python3 scripts/import_translations.py platforms/nano/index.rst platforms/nano/spec.rst
scripts/i18n_sync.sh fixpo && scripts/i18n_sync.sh clean-suffix
scripts/i18n_sync.sh build uk && scripts/i18n_sync.sh build ru
```
