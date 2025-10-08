# Localization Guide / Інструкція з локалізації / Руководство по локализации

This guide explains how to work with translations in the ByByte documentation project.

Ця інструкція пояснює, як працювати з перекладами в проекті документації ByByte.

Это руководство объясняет, как работать с переводами в проекте документации ByByte.

---

## Supported Languages / Підтримувані мови / Поддерживаемые языки

- **English** (en) - Default language
- **Ukrainian** (uk) - Українська
- **Russian** (ru) - Русский

---

## Quick Start / Швидкий старт / Быстрый старт

### Building Documentation for All Languages

```bash
# Build all language versions
make html-all

# Build specific language
make html       # English (default)
make html-uk    # Ukrainian
make html-ru    # Russian
```

### Збірка документації всіма мовами

```bash
# Зібрати всі мовні версії
make html-all

# Зібрати конкретну мову
make html       # Англійська (за замовчуванням)
make html-uk    # Українська
make html-ru    # Російська
```

### Сборка документации на всех языках

```bash
# Собрать все языковые версии
make html-all

# Собрать конкретный язык
make html       # Английский (по умолчанию)
make html-uk    # Украинский
make html-ru    # Русский
```

---

## Translation Workflow / Робочий процес перекладу / Рабочий процесс перевода

### Step 1: Extract Translatable Strings

```bash
make gettext
```

This creates `.pot` (Portable Object Template) files in `docs/_build/gettext/`.

Це створює `.pot` файли в `docs/_build/gettext/`.

Это создает `.pot` файлы в `docs/_build/gettext/`.

### Step 2: Update Translation Catalogs

```bash
make update
```

This updates `.po` files in `docs/locale/{uk,ru}/LC_MESSAGES/`.

Це оновлює `.po` файли в `docs/locale/{uk,ru}/LC_MESSAGES/`.

Это обновляет `.po` файлы в `docs/locale/{uk,ru}/LC_MESSAGES/`.

### Step 3: Edit Translations

Edit the `.po` files manually or using a translation tool:

```bash
# Edit Ukrainian translations
nano docs/locale/uk/LC_MESSAGES/index.po

# Edit Russian translations
nano docs/locale/ru/LC_MESSAGES/index.po
```

**Translation Tools / Інструменти перекладу / Инструменты перевода:**

- [Poedit](https://poedit.net/) - GUI editor
- [Lokalize](https://userbase.kde.org/Lokalize) - KDE translation tool
- [GTranslator](https://wiki.gnome.org/Apps/Gtranslator) - GNOME translation tool

### Step 4: Build Translated Documentation

```bash
# Compile translations and build
make html-all
```

---

## File Structure / Структура файлів / Структура файлов

```
docs/
├── locale/
│   ├── uk/                    # Ukrainian translations
│   │   └── LC_MESSAGES/
│   │       ├── index.po       # Main page translation
│   │       ├── installation.po
│   │       ├── quickstart.po
│   │       ├── usage.po
│   │       ├── api.po
│   │       ├── changelog.po
│   │       └── contributing.po
│   └── ru/                    # Russian translations
│       └── LC_MESSAGES/
│           ├── index.po
│           └── ...
├── _build/
│   ├── html/                  # English documentation
│   ├── html/uk/               # Ukrainian documentation
│   ├── html/ru/               # Russian documentation
│   └── gettext/               # Translation templates (.pot)
└── *.rst                      # Source files (English)
```

---

## Translation File Format / Формат файлів перекладу / Формат файлов перевода

Translation files (`.po`) consist of message pairs:

Файли перекладу (`.po`) складаються з пар повідомлень:

Файлы перевода (`.po`) состоят из пар сообщений:

```po
#: ../../index.rst:2
msgid "ByByte Documentation"
msgstr "Документація ByByte"
```

- `msgid` - Original English text / Оригінальний англійський текст / Оригинальный английский текст
- `msgstr` - Translated text / Перекладений текст / Переведенный текст

**Example / Приклад / Пример:**

```po
#: ../../index.rst:4
msgid "Welcome to ByByte's documentation!"
msgstr "Ласкаво просимо до документації ByByte!"  # Ukrainian
msgstr "Добро пожаловать в документацию ByByte!"  # Russian
```

---

## Adding a New Language / Додавання нової мови / Добавление нового языка

### 1. Update Makefile

Edit `docs/Makefile` and add new language code:

```makefile
LANGUAGES = uk ru fr  # Add 'fr' for French
```

### 2. Create Translation Catalog

```bash
# Extract messages
make gettext

# Create .po files for new language
sphinx-intl update -p docs/_build/gettext -l fr
```

### 3. Add Build Target

Edit `docs/Makefile`:

```makefile
html-fr:
	@$(SPHINXBUILD) -b html -D language=fr $(SOURCEDIR) $(BUILDDIR)/html/fr $(SPHINXOPTS)
	@echo "French documentation built in $(BUILDDIR)/html/fr"
```

### 4. Translate

Edit files in `docs/locale/fr/LC_MESSAGES/*.po`

### 5. Build

```bash
make html-fr
```

---

## Translation Guidelines / Рекомендації з перекладу / Рекомендации по переводу

### Do's / Робити / Делать

✅ Keep technical terms consistent / Зберігайте технічні терміни послідовними / Сохраняйте технические термины последовательными

✅ Preserve formatting (`:ref:`, `**bold**`, etc.) / Зберігайте форматування / Сохраняйте форматирование

✅ Test builds after translating / Тестуйте збірку після перекладу / Тестируйте сборку после перевода

✅ Translate in context, not word-by-word / Перекладайте в контексті / Переводите в контексте

### Don'ts / Не робити / Не делать

❌ Don't translate code examples / Не перекладайте приклади коду / Не переводите примеры кода

❌ Don't translate :ref: targets / Не перекладайте цілі :ref: / Не переводите цели :ref:

❌ Don't translate URLs / Не перекладайте URL-адреси / Не переводите URL-адреса

❌ Don't leave empty msgstr / Не залишайте порожні msgstr / Не оставляйте пустые msgstr

---

## Common Translation Commands / Поширені команди перекладу / Распространенные команды перевода

```bash
# Extract all translatable strings
make gettext

# Update all language catalogs
make update

# Build English version
make html

# Build Ukrainian version
make html-uk

# Build Russian version
make html-ru

# Build all languages
make html-all

# Clean all builds
make clean
```

---

## Testing Translations / Тестування перекладів / Тестирование переводов

### 1. Check .po file syntax

```bash
msgfmt -c docs/locale/uk/LC_MESSAGES/index.po
msgfmt -c docs/locale/ru/LC_MESSAGES/index.po
```

### 2. Build and view

```bash
make html-uk
xdg-open docs/_build/html/uk/index.html
```

### 3. Check for missing translations

```bash
# Find empty translations
grep -n 'msgstr ""' docs/locale/uk/LC_MESSAGES/*.po
```

---

## Translation Statistics / Статистика перекладів / Статистика переводов

Check translation progress:

Перевірте прогрес перекладу:

Проверьте прогресс перевода:

```bash
# Ukrainian
msgfmt --statistics docs/locale/uk/LC_MESSAGES/index.po

# Russian
msgfmt --statistics docs/locale/ru/LC_MESSAGES/index.po
```

---

## Contributing Translations / Внесок у переклади / Вклад в переводы

1. Fork the repository / Зробіть форк репозиторію / Сделайте форк репозитория
2. Update translations / Оновіть переклади / Обновите переводы
3. Test builds / Протестуйте збірку / Протестируйте сборку
4. Create Pull Request / Створіть Pull Request / Создайте Pull Request

---

## Resources / Ресурси / Ресурсы

- [Sphinx i18n](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx-intl documentation](https://sphinx-intl.readthedocs.io/)
- [GNU gettext manual](https://www.gnu.org/software/gettext/manual/)

---

## Troubleshooting / Вирішення проблем / Устранение неполадок

### Translations not showing up

```bash
# Rebuild translation catalogs
make clean
make update
make html-all
```

### Missing .mo files

```bash
# Compile translations manually
sphinx-intl build
```

### Wrong language displayed

Check `language` setting in `docs/conf.py` and `READTHEDOCS_LANGUAGE` environment variable.

---

**Need help? / Потрібна допомога? / Нужна помощь?**

Open an issue on GitHub: https://github.com/vergilium/ByByteDoc/issues

