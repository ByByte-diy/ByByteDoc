# Developer Documentation / Документація для розробників

Welcome to the ByByte documentation developer guide!

Ласкаво просимо до посібника розробника документації ByByte!

---

## 📚 Table of Contents / Зміст

### 🚀 Quick Start / Швидкий старт

- [Setup Guide](development/setup.md) - Set up your development environment / Налаштування середовища розробки
- [Building Documentation](development/building.md) - Build and test docs locally / Збірка та тестування документації

### 🌍 Translation / Переклад

- [Translation Overview](translation/README.md) - Overview of translation system / Огляд системи перекладів
- [Translation Workflow](translation/workflow.md) - Complete translation process / Повний процес перекладу
- [Translation Guidelines](translation/guidelines.md) - Best practices and rules / Найкращі практики
- [Translation Tools](translation/tools.md) - Tools for translators / Інструменти для перекладачів

### 🔧 Development / Розробка

- [Project Structure](development/structure.md) - Project organization / Структура проекту
- [Coding Standards](development/standards.md) - Documentation writing standards / Стандарти написання документації
- [Testing](development/testing.md) - How to test changes / Як тестувати зміни

### 🚢 Deployment / Деплой

- [ReadTheDocs Setup](deployment/readthedocs.md) - RTD configuration / Налаштування ReadTheDocs
- [CI/CD](deployment/cicd.md) - Continuous Integration setup / Налаштування CI/CD
- [Release Process](deployment/release.md) - How to release new versions / Як випускати нові версії

### 📝 Contributing / Контрибуції

- [Contributing Guide](CONTRIBUTING.md) - How to contribute / Як зробити внесок
- [Code Review](development/code-review.md) - Review guidelines / Гайдлайни по ревʼю

---

## 🎯 Quick Links / Швидкі посилання

### For New Contributors / Для нових контриб'юторів

1. Read [Setup Guide](development/setup.md)
2. Check [Project Structure](development/structure.md)
3. Follow [Contributing Guide](CONTRIBUTING.md)

### For Translators / Для перекладачів

1. Read [Translation Workflow](translation/workflow.md)
2. Use [Translation Tools](translation/tools.md)
3. Follow [Translation Guidelines](translation/guidelines.md)

### For Maintainers / Для мейнтейнерів

1. Check [ReadTheDocs Setup](deployment/readthedocs.md)
2. Review [CI/CD Configuration](deployment/cicd.md)
3. Follow [Release Process](deployment/release.md)

---

## 📖 Documentation Formats / Формати документації

### For Users / Для користувачів

**Location:** `docs/` directory  
**Format:** reStructuredText (`.rst`)  
**Build:** Sphinx → HTML/PDF/EPUB  
**Output:** Published on ReadTheDocs

**Розташування:** директорія `docs/`  
**Формат:** reStructuredText (`.rst`)  
**Збірка:** Sphinx → HTML/PDF/EPUB  
**Вивід:** Публікується на ReadTheDocs

### For Developers / Для розробників

**Location:** `doc/` directory (this folder!)  
**Format:** Markdown (`.md`)  
**Build:** Not built, read directly on GitHub  
**Output:** Viewed in repository

**Розташування:** директорія `doc/` (ця тека!)  
**Формат:** Markdown (`.md`)  
**Збірка:** Не збирається, читається безпосередньо на GitHub  
**Вивід:** Переглядається в репозиторії

---

## 🔍 Finding What You Need / Знайти потрібне

### "I want to add new documentation page"

→ [Coding Standards](development/standards.md)  
→ [Project Structure](development/structure.md)

### "I want to translate documentation"

→ [Translation Workflow](translation/workflow.md)  
→ [Translation Tools](translation/tools.md)

### "I want to fix a typo"

→ [Contributing Guide](CONTRIBUTING.md)  
→ [Building Documentation](development/building.md)

### "I want to deploy/configure ReadTheDocs"

→ [ReadTheDocs Setup](deployment/readthedocs.md)  
→ [CI/CD Configuration](deployment/cicd.md)

---

## 🛠️ Essential Commands / Основні команди

```bash
# Setup / Налаштування
pip install -r docs/requirements.txt

# Build English docs / Збірка англійської документації
make html

# Build all languages / Збірка всіх мов
make html-all

# Extract translations / Витяг перекладів
make gettext

# Update translations / Оновити переклади
make update

# Check translation progress / Перевірити прогрес перекладів
./scripts/check-translations.sh

# Clean build / Очистити збірку
make clean
```

---

## 📂 Directory Structure / Структура директорій

```
ByByteDoc/
├── doc/                      ← Developer documentation (YOU ARE HERE!)
│   ├── README.md            ← This file / Цей файл
│   ├── CONTRIBUTING.md      ← How to contribute
│   ├── development/         ← Development guides
│   │   ├── setup.md
│   │   ├── building.md
│   │   ├── structure.md
│   │   ├── standards.md
│   │   ├── testing.md
│   │   └── code-review.md
│   ├── translation/         ← Translation guides
│   │   ├── README.md
│   │   ├── workflow.md
│   │   ├── guidelines.md
│   │   └── tools.md
│   └── deployment/          ← Deployment guides
│       ├── readthedocs.md
│       ├── cicd.md
│       └── release.md
│
├── docs/                     ← User documentation (Sphinx)
│   ├── conf.py
│   ├── index.rst
│   ├── installation.rst
│   ├── quickstart.rst
│   ├── usage.rst
│   ├── api.rst
│   └── locale/              ← Translations
│       ├── uk/
│       └── ru/
│
├── scripts/                  ← Helper scripts
│   └── check-translations.sh
│
├── .github/                  ← GitHub configuration
│   └── workflows/
│       └── docs.yml
│
├── .readthedocs.yaml        ← ReadTheDocs config
├── Makefile                 ← Build commands
└── README.md                ← Project README
```

---

## 🆘 Getting Help / Отримати допомогу

### Documentation Issues / Проблеми з документацією

- Open an issue: [GitHub Issues](https://github.com/vergilium/ByByteDoc/issues)
- Check existing docs: Read files in `doc/` and `docs/`

### Translation Questions / Питання про переклад

- See [Translation FAQ](translation/README.md#faq)
- Check [Translation Tools](translation/tools.md)

### Technical Problems / Технічні проблеми

- Check [Troubleshooting](development/building.md#troubleshooting)
- Review [CI/CD logs](deployment/cicd.md#debugging)

---

## 📜 License / Ліцензія

This documentation is part of the ByByte project.

Ця документація є частиною проекту ByByte.

---

## 🤝 Contributing / Внесок

We welcome all contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

Ми вітаємо всі внески! Дивіться [CONTRIBUTING.md](CONTRIBUTING.md) для деталей.

---

**Last Updated:** 2025-10-06  
**Maintained by:** ByByte Team

