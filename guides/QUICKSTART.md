# Quick Start for Developers
# Швидкий старт для розробників

Get started in 5 minutes!

Почніть за 5 хвилин!

---

## I want to... / Я хочу...

### 📝 Edit Documentation / Редагувати документацію

```bash
# 1. Edit English source / Редагувати англійське джерело
nano docs/installation.rst

# 2. Build and view / Зібрати та переглянути
make html
xdg-open docs/_build/html/installation.html
```

📖 Full guide: [Building Documentation](development/building.md)

---

### 🌍 Translate Documentation / Перекласти документацію

```bash
# 1. Extract & update / Витягти та оновити
make gettext
make update

# 2. Translate in Poedit / Перекласти в Poedit
poedit docs/locale/uk/LC_MESSAGES/installation.po

# 3. Build translated version / Зібрати перекладену версію
make html-uk
xdg-open docs/_build/html/uk/installation.html
```

📖 Full guide: [Translation Workflow](translation/workflow.md)

---

### 🐛 Fix a Typo / Виправити помилку

```bash
# 1. Create branch / Створити гілку
git checkout -b fix/typo-in-docs

# 2. Fix typo / Виправити помилку
nano docs/installation.rst

# 3. Test / Тестувати
make html

# 4. Commit & push / Закомітити та запушити
git add docs/installation.rst
git commit -m "Fix typo in installation guide"
git push origin fix/typo-in-docs

# 5. Create PR on GitHub / Створити PR на GitHub
```

📖 Full guide: [Contributing](CONTRIBUTING.md)

---

### 🚀 Add New Page / Додати нову сторінку

```bash
# 1. Create .rst file / Створити .rst файл
nano docs/troubleshooting.rst

# 2. Add to index / Додати до індексу
nano docs/index.rst  # Add to toctree

# 3. Build / Зібрати
make html

# 4. Extract for translation / Витягти для перекладу
make gettext
make update

# 5. Build all languages / Зібрати всі мови
make html-all
```

📖 Full guide: [Project Structure](development/structure.md)

---

### 🔍 Check Translation Progress / Перевірити прогрес перекладів

```bash
./scripts/check-translations.sh
```

Output / Вивід:
```
📊 Total for Ukrainian:
   ✅ Translated: 36
   ❌ Untranslated: 166
   📈 Progress: 17%
```

---

### ⚙️ Setup Development Environment / Налаштувати середовище розробки

```bash
# 1. Clone / Клонувати
git clone https://github.com/vergilium/ByByteDoc.git
cd ByByteDoc

# 2. Install dependencies / Встановити залежності
pip install -r docs/requirements.txt

# 3. Test build / Тестова збірка
make html

# 4. Install Poedit (optional) / Встановити Poedit (опціонально)
sudo apt install poedit
```

📖 Full guide: [Setup Guide](development/setup.md)

---

## Common Commands / Поширені команди

```bash
# Build / Збірка
make html         # English / Англійська
make html-uk      # Ukrainian / Українська  
make html-ru      # Russian / Російська
make html-all     # All languages / Всі мови

# Translation / Переклад
make gettext      # Extract strings / Витягти рядки
make update       # Update .po files / Оновити .po файли

# Maintenance / Обслуговування
make clean        # Clean build / Очистити збірку
make help         # Show all commands / Показати всі команди
```

---

## Directory Structure / Структура директорій

```
ByByteDoc/
├── doc/          ← Developer docs (YOU READ THIS!)
│   ├── README.md
│   ├── CONTRIBUTING.md
│   ├── development/
│   └── translation/
│
├── docs/         ← User docs (Sphinx)
│   ├── *.rst     ← Edit these for documentation
│   └── locale/   ← Edit these for translations
│
└── scripts/      ← Helper scripts
```

---

## Need Help? / Потрібна допомога?

| Question | Where to Look |
|----------|---------------|
| How to setup? | [Setup Guide](development/setup.md) |
| How to build? | [Building Documentation](development/building.md) |
| How to translate? | [Translation Workflow](translation/workflow.md) |
| What's the structure? | [Project Structure](development/structure.md) |
| How to contribute? | [Contributing Guide](CONTRIBUTING.md) |

---

## Quick Reference / Швидкий довідник

**Edit Documentation:**
`docs/*.rst` → `make html` → view in browser

**Translate:**
`make update` → edit `.po` → `make html-uk` → view

**Contribute:**
branch → edit → test → commit → push → PR

---

📖 **Full documentation:** [README.md](README.md)

🤝 **Want to contribute?** [CONTRIBUTING.md](CONTRIBUTING.md)

