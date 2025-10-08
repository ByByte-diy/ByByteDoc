# Development Environment Setup
# Налаштування середовища розробки

This guide will help you set up your development environment for working on ByByte documentation.

Цей посібник допоможе вам налаштувати середовище розробки для роботи над документацією ByByte.

---

## Prerequisites / Передумови

### Required / Необхідно

- **Git** - Version control / Система контролю версій
- **Python 3.10+** - Documentation build system / Система збірки документації
- **pip** - Python package manager / Менеджер пакетів Python
- **make** - Build automation / Автоматизація збірки

### Optional / Опціонально

- **Poedit** - Translation tool / Інструмент перекладу
- **VS Code** or preferred text editor / VS Code або інший редактор

---

## Step 1: Clone Repository / Крок 1: Клонування репозиторію

```bash
# Clone the repository / Клонуйте репозиторій
git clone https://github.com/vergilium/ByByteDoc.git
cd ByByteDoc

# Check current branch / Перевірте поточну гілку
git branch
git status
```

---

## Step 2: Install Python Dependencies / Крок 2: Встановлення залежностей Python

```bash
# Install documentation dependencies / Встановіть залежності документації
pip install -r docs/requirements.txt

# Verify installation / Перевірте встановлення
sphinx-build --version
sphinx-intl --version
```

**Expected output / Очікуваний результат:**
```
sphinx-build 8.1.3
sphinx-intl 2.3.2
```

---

## Step 3: Install Translation Tools / Крок 3: Встановлення інструментів перекладу

### On Ubuntu/Debian

```bash
# Install Poedit (GUI translation tool) / Встановіть Poedit
sudo apt update
sudo apt install poedit

# Install gettext utilities / Встановіть утиліти gettext
sudo apt install gettext
```

### On macOS

```bash
# Using Homebrew
brew install poedit
brew install gettext
```

### On Windows

Download and install Poedit from: https://poedit.net/download

---

## Step 4: Configure Git / Крок 4: Налаштування Git

```bash
# Set your name and email / Встановіть ім'я та email
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Configure line endings (optional) / Налаштуйте закінчення рядків
git config core.autocrlf input  # Linux/macOS
git config core.autocrlf true   # Windows
```

---

## Step 5: Test Build / Крок 5: Тестова збірка

```bash
# Build English documentation / Зберіть англійську документацію
make html

# Check for errors / Перевірте помилки
echo $?  # Should output: 0 (success) / Має вивести: 0 (успіх)

# Open built documentation / Відкрийте зібрану документацію
xdg-open docs/_build/html/index.html  # Linux
open docs/_build/html/index.html      # macOS
start docs/_build/html/index.html     # Windows
```

---

## Step 6: Build All Languages / Крок 6: Збірка всіх мов

```bash
# Build documentation for all languages / Зберіть документацію всіма мовами
make html-all

# Verify all language versions / Перевірте всі мовні версії
ls -la docs/_build/html/
# Should see: index.html, uk/, ru/ directories
```

---

## Step 7: Set Up IDE (Optional) / Крок 7: Налаштування IDE (Опціонально)

### VS Code

Install recommended extensions / Встановіть рекомендовані розширення:

```json
{
  "recommendations": [
    "lextudio.restructuredtext",
    "trond-snekvik.simple-rst",
    "ms-python.python",
    "mrorz.language-gettext",
    "davidanson.vscode-markdownlint"
  ]
}
```

Create `.vscode/settings.json`:

```json
{
  "files.associations": {
    "*.rst": "restructuredtext",
    "*.po": "gettext"
  },
  "restructuredtext.confPath": "${workspaceFolder}/docs",
  "python.linting.enabled": true,
  "files.exclude": {
    "**/_build": true,
    "**/__pycache__": true,
    "**/*.pyc": true
  }
}
```

---

## Verification Checklist / Контрольний список перевірки

- [ ] Git is installed and configured / Git встановлено та налаштовано
- [ ] Python 3.10+ is installed / Python 3.10+ встановлено
- [ ] All Python packages installed / Всі пакети Python встановлено
- [ ] `make html` builds successfully / `make html` збирається успішно
- [ ] `make html-all` builds all languages / `make html-all` збирає всі мови
- [ ] Can open built documentation in browser / Можна відкрити документацію в браузері
- [ ] Translation tools installed (optional) / Інструменти перекладу встановлено (опціонально)

---

## Troubleshooting / Вирішення проблем

### Python not found / Python не знайдено

```bash
# Check Python version / Перевірте версію Python
python3 --version
python --version

# Use python3 explicitly if needed / Використовуйте python3 явно
python3 -m pip install -r docs/requirements.txt
```

### Permission denied / Доступ заборонено

```bash
# Install for user only / Встановіть тільки для користувача
pip install --user -r docs/requirements.txt

# Or use virtual environment / Або використовуйте віртуальне середовище
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r docs/requirements.txt
```

### Build fails / Збірка не вдалася

```bash
# Clean and rebuild / Очистіть та перезберіть
make clean
make html

# Check for specific errors / Перевірте конкретні помилки
make html 2>&1 | tee build.log
```

### Missing dependencies / Відсутні залежності

```bash
# Reinstall all dependencies / Перевстановіть всі залежності
pip install --upgrade -r docs/requirements.txt

# Check installed packages / Перевірте встановлені пакети
pip list | grep -i sphinx
```

---

## Next Steps / Наступні кроки

1. Read [Project Structure](structure.md) to understand the codebase
2. Check [Building Documentation](building.md) for build commands
3. See [Contributing Guide](../CONTRIBUTING.md) to start contributing

1. Прочитайте [Структуру проекту](structure.md), щоб зрозуміти кодову базу
2. Перевірте [Збірку документації](building.md) для команд збірки
3. Дивіться [Посібник контриб'ютора](../CONTRIBUTING.md), щоб почати вносити зміни

---

## Quick Reference / Швидкий довідник

```bash
# Common commands / Поширені команди
make html         # Build English docs / Зібрати англійську документацію
make html-uk      # Build Ukrainian docs / Зібрати українську документацію
make html-ru      # Build Russian docs / Зібрати російську документацію
make html-all     # Build all languages / Зібрати всі мови
make clean        # Clean build / Очистити збірку
make gettext      # Extract translations / Витягти переклади
make update       # Update translation catalogs / Оновити каталоги перекладів
```

---

**Ready to contribute?** See [CONTRIBUTING.md](../CONTRIBUTING.md)

**Готові зробити внесок?** Дивіться [CONTRIBUTING.md](../CONTRIBUTING.md)

