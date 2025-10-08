# Project Structure
# Структура проекту

Understanding the ByByte documentation project organization.

Розуміння організації проекту документації ByByte.

---

## Directory Layout / Структура директорій

```
ByByteDoc/
├── doc/                          # Developer documentation / Документація розробників
│   ├── README.md                # Developer guide index / Індекс посібника розробника
│   ├── CONTRIBUTING.md          # Contributing guidelines / Гайдлайни контрибуцій
│   ├── development/             # Development guides / Посібники розробки
│   │   ├── setup.md            # Environment setup / Налаштування середовища
│   │   ├── building.md         # Build instructions / Інструкції збірки
│   │   ├── structure.md        # This file / Цей файл
│   │   ├── standards.md        # Coding standards / Стандарти кодування
│   │   ├── testing.md          # Testing guide / Посібник тестування
│   │   └── code-review.md      # Review guidelines / Гайдлайни ревʼю
│   ├── translation/             # Translation guides / Посібники перекладів
│   │   ├── README.md           # Translation overview / Огляд перекладів
│   │   ├── workflow.md         # Translation process / Процес перекладу
│   │   ├── guidelines.md       # Translation rules / Правила перекладу
│   │   ├── tools.md            # Translation tools / Інструменти перекладу
│   │   ├── LOCALIZATION.md     # Localization guide / Посібник локалізації
│   │   └── examples.md         # Translation examples / Приклади перекладів
│   └── deployment/              # Deployment guides / Посібники деплою
│       ├── readthedocs.md      # ReadTheDocs setup / Налаштування ReadTheDocs
│       ├── cicd.md             # CI/CD configuration / Конфігурація CI/CD
│       └── release.md          # Release process / Процес релізу
│
├── docs/                         # User documentation (Sphinx) / Користувацька документація
│   ├── conf.py                  # Sphinx configuration / Конфігурація Sphinx
│   ├── index.rst                # Main page / Головна сторінка
│   ├── installation.rst         # Installation guide / Посібник встановлення
│   ├── quickstart.rst           # Quick start / Швидкий старт
│   ├── usage.rst                # Usage guide / Посібник використання
│   ├── api.rst                  # API reference / Довідник API
│   ├── changelog.rst            # Version history / Історія версій
│   ├── contributing.rst         # How to contribute / Як зробити внесок
│   ├── requirements.txt         # Python dependencies / Залежності Python
│   ├── Makefile                 # Sphinx build / Збірка Sphinx
│   ├── _static/                 # Static files / Статичні файли
│   │   └── (images, CSS, etc.)
│   ├── _templates/              # Custom templates / Кастомні шаблони
│   ├── locale/                  # Translations / Переклади
│   │   ├── uk/                  # Ukrainian / Українська
│   │   │   └── LC_MESSAGES/
│   │   │       ├── index.po
│   │   │       ├── installation.po
│   │   │       └── ...
│   │   └── ru/                  # Russian / Російська
│   │       └── LC_MESSAGES/
│   │           └── ...
│   └── _build/                  # Build output (gitignored) / Вивід збірки
│       ├── html/                # English HTML
│       ├── html/uk/             # Ukrainian HTML
│       ├── html/ru/             # Russian HTML
│       └── gettext/             # Translation templates
│
├── scripts/                      # Helper scripts / Допоміжні скрипти
│   └── check-translations.sh    # Translation checker / Перевірка перекладів
│
├── .github/                      # GitHub configuration / Конфігурація GitHub
│   └── workflows/
│       └── docs.yml             # GitHub Actions CI / CI GitHub Actions
│
├── .readthedocs.yaml            # ReadTheDocs config / Конфігурація ReadTheDocs
├── .gitignore                   # Git ignore patterns / Шаблони ігнорування Git
├── Makefile                     # Root makefile / Кореневий makefile
└── README.md                    # Project README / README проекту
```

---

## Key Files Explained / Пояснення ключових файлів

### Configuration Files / Файли конфігурації

#### `.readthedocs.yaml`
ReadTheDocs configuration / Конфігурація ReadTheDocs

```yaml
version: 2
build:
  os: ubuntu-24.04
  tools:
    python: "3.13"
sphinx:
  configuration: docs/conf.py
python:
  install:
    - requirements: docs/requirements.txt
formats:
  - pdf
  - epub
```

#### `docs/conf.py`
Sphinx configuration - controls how documentation is built

Конфігурація Sphinx - контролює як збирається документація

Key settings:
- Project metadata (name, version, author)
- Sphinx extensions
- HTML theme configuration
- Language support
- Internationalization settings

#### `docs/requirements.txt`
Python packages needed to build documentation

Пакети Python необхідні для збірки документації

```txt
sphinx>=7.0.0
sphinx-rtd-theme>=2.0.0
sphinx-intl>=2.0.0
docutils>=0.18
```

### Documentation Source Files / Вихідні файли документації

#### `.rst` files in `docs/`
reStructuredText source files - the actual documentation content

Вихідні файли reStructuredText - фактичний контент документації

- `index.rst` - Main landing page / Головна сторінка
- `installation.rst` - Installation instructions / Інструкції встановлення
- `quickstart.rst` - Quick start guide / Посібник швидкого старту
- `usage.rst` - Detailed usage / Детальне використання
- `api.rst` - API reference / Довідник API

### Translation Files / Файли перекладів

#### `.po` files in `docs/locale/*/LC_MESSAGES/`
Portable Object files - contain translations

Файли Portable Object - містять переклади

Structure / Структура:
```po
msgid "Installation"      # Original English / Оригінальна англійська
msgstr "Встановлення"     # Ukrainian translation / Український переклад
```

Each .rst file has corresponding .po file / Кожен .rst файл має відповідний .po файл

#### `.pot` files in `docs/_build/gettext/`
Template files - extracted from .rst, used to create/update .po files

Файли шаблонів - витягнуті з .rst, використовуються для створення/оновлення .po

Generated by `make gettext` / Генеруються командою `make gettext`

### Build Files / Файли збірки

#### `Makefile` (root)
Delegates commands to `docs/Makefile`

Делегує команди до `docs/Makefile`

#### `docs/Makefile`
Contains all Sphinx build commands

Містить всі команди збірки Sphinx

Key targets / Ключові цілі:
- `html` - Build English HTML
- `html-uk` - Build Ukrainian HTML
- `html-ru` - Build Russian HTML
- `html-all` - Build all languages
- `gettext` - Extract translations
- `update` - Update .po files

---

## File Naming Conventions / Конвенції іменування файлів

### Documentation Files / Файли документації

- Use lowercase / Використовуйте малі літери
- Use hyphens for multi-word names / Використовуйте дефіси для багатослівних назв
- Use `.rst` extension for Sphinx docs / Використовуйте розширення `.rst` для документів Sphinx
- Use `.md` extension for developer docs / Використовуйте розширення `.md` для документації розробників

**Good / Добре:**
```
installation.rst
quick-start.rst
api-reference.rst
```

**Bad / Погано:**
```
Installation.rst
quick_start.rst
API-Reference.RST
```

### Translation Files / Файли перекладів

- Follow .rst filename / Слідувати назві .rst файлу
- Use `.po` extension / Використовувати розширення `.po`
- Located in `locale/{lang}/LC_MESSAGES/` / Розташовані в `locale/{lang}/LC_MESSAGES/`

Example / Приклад:
```
docs/installation.rst
  → docs/locale/uk/LC_MESSAGES/installation.po
  → docs/locale/ru/LC_MESSAGES/installation.po
```

---

## Adding New Documentation / Додавання нової документації

### Step 1: Create .rst File / Крок 1: Створити .rst файл

```bash
# Create new documentation page / Створити нову сторінку документації
nano docs/new-feature.rst
```

```rst
New Feature
===========

Description of the new feature.

Usage
-----

How to use it...
```

### Step 2: Add to Table of Contents / Крок 2: Додати до змісту

Edit `docs/index.rst`:

```rst
.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   installation
   quickstart
   usage
   new-feature  ← Add here / Додати сюди
   api
```

### Step 3: Build and Test / Крок 3: Зібрати та протестувати

```bash
make html
xdg-open docs/_build/html/new-feature.html
```

### Step 4: Extract for Translation / Крок 4: Витягти для перекладу

```bash
make gettext
make update
```

Now translate in:
- `docs/locale/uk/LC_MESSAGES/new-feature.po`
- `docs/locale/ru/LC_MESSAGES/new-feature.po`

---

## Directory Purposes / Призначення директорій

### `doc/` vs `docs/`

| Directory | Purpose | Format | Audience |
|-----------|---------|--------|----------|
| `doc/` | Developer documentation | Markdown | Developers, contributors |
| `docs/` | User documentation | reStructuredText | End users |

| Директорія | Призначення | Формат | Аудиторія |
|------------|-------------|--------|-----------|
| `doc/` | Документація розробників | Markdown | Розробники, контриб'ютори |
| `docs/` | Документація користувачів | reStructuredText | Кінцеві користувачі |

### `_static/` - Static Assets / Статичні ресурси

Place images, custom CSS, JavaScript here / Розміщуйте зображення, кастомний CSS, JavaScript тут

```
docs/_static/
├── logo.png
├── custom.css
└── diagram.svg
```

Reference in .rst:

```rst
.. image:: _static/logo.png
   :alt: Project logo
```

### `_templates/` - Custom Templates / Кастомні шаблони

Override Sphinx/theme templates / Перевизначити шаблони Sphinx/теми

Rarely needed / Рідко потрібно

---

## Build Artifacts / Артефакти збірки

### Generated Files (Gitignored) / Згенеровані файли (ігноруються Git)

```
docs/_build/        # All build output / Весь вивід збірки
docs/locale/**/*.mo # Compiled translations / Скомпільовані переклади
```

### Tracked Files / Відстежувані файли

```
docs/*.rst          # Source documentation / Вихідна документація
docs/locale/**/*.po # Translation source / Джерело перекладів
docs/conf.py        # Configuration / Конфігурація
```

---

## Dependencies / Залежності

### Python Packages / Пакети Python

Defined in `docs/requirements.txt`:

- **sphinx** - Documentation builder / Збудовувач документації
- **sphinx-rtd-theme** - ReadTheDocs theme / Тема ReadTheDocs
- **sphinx-intl** - Internationalization / Інтернаціоналізація
- **docutils** - Document utilities / Утиліти документів

### System Tools / Системні інструменти

- **make** - Build automation / Автоматизація збірки
- **gettext** - Translation tools / Інструменти перекладу
- **git** - Version control / Контроль версій

---

## Next Steps / Наступні кроки

- [Building Documentation](building.md) - Learn build commands
- [Coding Standards](standards.md) - Documentation style guide
- [Translation Workflow](../translation/workflow.md) - Work with translations

- [Збірка документації](building.md) - Вивчити команди збірки
- [Стандарти кодування](standards.md) - Посібник стилю документації
- [Робочий процес перекладів](../translation/workflow.md) - Працювати з перекладами

