# Building Documentation
# Збірка документації

Complete guide to building ByByte documentation.

Повний посібник зі збірки документації ByByte.

---

## Quick Start / Швидкий старт

```bash
# Build English documentation / Зібрати англійську документацію
make html

# View in browser / Переглянути в браузері
xdg-open docs/_build/html/index.html
```

---

## Build Commands / Команди збірки

### Single Language Builds / Збірка однієї мови

```bash
# English (default) / Англійська (за замовчуванням)
make html
# Output: docs/_build/html/

# Ukrainian / Українська
make html-uk
# Output: docs/_build/html/uk/

# Russian / Російська
make html-ru
# Output: docs/_build/html/ru/
```

### Multi-Language Build / Мультимовна збірка

```bash
# Build all languages at once / Зібрати всі мови одразу
make html-all

# Output / Вивід:
# docs/_build/html/       (English)
# docs/_build/html/uk/    (Ukrainian)
# docs/_build/html/ru/    (Russian)
```

### Other Formats / Інші формати

```bash
# PDF (requires LaTeX) / PDF (потребує LaTeX)
make latexpdf

# EPUB
make epub

# Show all available commands / Показати всі доступні команди
make help
```

---

## Clean Builds / Чиста збірка

```bash
# Remove all built files / Видалити всі зібрані файли
make clean

# Clean and rebuild / Очистити та перезібрати
make clean && make html-all
```

---

## Translation Workflow / Робочий процес перекладів

### Extract Translatable Strings / Витягти рядки для перекладу

```bash
# Extract messages from .rst files / Витягти повідомлення з .rst файлів
make gettext

# Output: docs/_build/gettext/*.pot files
```

### Update Translation Catalogs / Оновити каталоги перекладів

```bash
# Update .po files for all languages / Оновити .po файли для всіх мов
make update

# This updates:
# - docs/locale/uk/LC_MESSAGES/*.po
# - docs/locale/ru/LC_MESSAGES/*.po
```

### Check Translation Progress / Перевірити прогрес перекладів

```bash
# Run translation checker / Запустити перевірку перекладів
./scripts/check-translations.sh
```

---

## Build Options / Опції збірки

### With Warnings as Errors / З попередженнями як помилками

```bash
# Fail build on warnings / Збірка з фейлом при попередженнях
make html SPHINXOPTS="-W"

# Useful for CI/CD / Корисно для CI/CD
```

### Verbose Output / Детальний вивід

```bash
# Show detailed build process / Показати детальний процес збірки
make html SPHINXOPTS="-v"

# Very verbose / Дуже детальний
make html SPHINXOPTS="-vv"
```

### Parallel Build / Паралельна збірка

```bash
# Use multiple cores / Використовувати кілька ядер
make html SPHINXOPTS="-j auto"

# Specify number of jobs / Вказати кількість потоків
make html SPHINXOPTS="-j 4"
```

---

## Development Workflow / Робочий процес розробки

### 1. Edit Documentation / 1. Редагувати документацію

```bash
# Edit English source / Редагувати англійське джерело
nano docs/installation.rst

# Or add new page / Або додати нову сторінку
nano docs/new-page.rst

# Don't forget to add to index.rst! / Не забудьте додати до index.rst!
```

### 2. Build and Check / 2. Зібрати та перевірити

```bash
# Build English version / Зібрати англійську версію
make html

# Check for errors / Перевірити помилки
echo $?  # 0 = success / 0 = успіх

# View in browser / Переглянути в браузері
xdg-open docs/_build/html/installation.html
```

### 3. Update Translations / 3. Оновити переклади

```bash
# Extract new/changed strings / Витягти нові/змінені рядки
make gettext

# Update translation files / Оновити файли перекладів
make update

# Translate in Poedit / Перекласти в Poedit
poedit docs/locale/uk/LC_MESSAGES/installation.po

# Build translated version / Зібрати перекладену версію
make html-uk
```

### 4. Verify All Languages / 4. Перевірити всі мови

```bash
# Build everything / Зібрати все
make clean && make html-all

# Quick visual check / Швидка візуальна перевірка
xdg-open docs/_build/html/index.html       # English
xdg-open docs/_build/html/uk/index.html    # Ukrainian
xdg-open docs/_build/html/ru/index.html    # Russian
```

---

## Troubleshooting / Вирішення проблем

### Build Fails / Збірка не вдається

**Check error messages / Перевірте повідомлення про помилки:**

```bash
# Build with full output / Зібрати з повним виводом
make html 2>&1 | tee build.log

# Check log file / Перевірте файл логу
less build.log
```

**Common issues / Поширені проблеми:**

1. **Syntax error in .rst file** / **Синтаксична помилка в .rst файлі**
   ```
   ERROR: Unknown directive type "code-blok"
   ```
   Solution / Рішення: Fix typo in .rst file / Виправте помилку в .rst файлі

2. **Missing dependency** / **Відсутня залежність**
   ```
   ModuleNotFoundError: No module named 'sphinx_rtd_theme'
   ```
   Solution / Рішення:
   ```bash
   pip install -r docs/requirements.txt
   ```

3. **Translation file error** / **Помилка файлу перекладів**
   ```
   ValueError: translation file has no header
   ```
   Solution / Рішення: Fix .po file header / Виправте заголовок .po файлу

### Slow Build / Повільна збірка

```bash
# Clean cached files / Очистити кешовані файли
make clean

# Use parallel build / Використовувати паралельну збірку
make html SPHINXOPTS="-j auto"
```

### Changes Not Showing / Зміни не відображаються

```bash
# Force rebuild / Примусова перебудова
make clean
make html

# Check you're viewing the right file / Перевірте, що переглядаєте правильний файл
ls -la docs/_build/html/
```

### Translation Not Working / Переклад не працює

```bash
# Verify .po file is translated / Перевірте, що .po файл перекладено
grep -A 1 'msgid "Installation"' docs/locale/uk/LC_MESSAGES/installation.po

# Should show: / Має показати:
# msgid "Installation"
# msgstr "Встановлення"

# Rebuild with clean / Перебудувати з очисткою
make clean
make html-uk
```

---

## CI/CD Integration / Інтеграція CI/CD

### GitHub Actions

Documentation is automatically built on every push / Документація автоматично збирається при кожному push:

```yaml
# .github/workflows/docs.yml
- name: Build documentation
  run: |
    pip install -r docs/requirements.txt
    make html SPHINXOPTS="-W"
```

### Local CI Simulation / Локальна симуляція CI

```bash
# Test as CI would / Тест як в CI
make clean
make html SPHINXOPTS="-W --keep-going"

# If this passes, CI should pass too
# Якщо це проходить, CI теж має пройти
```

---

## Performance Tips / Поради щодо продуктивності

### Incremental Builds / Інкрементальні збірки

Sphinx only rebuilds changed files / Sphinx перебудовує тільки змінені файли:

```bash
# First build (slow) / Перша збірка (повільна)
make html

# Subsequent builds (fast) / Подальші збірки (швидкі)
make html  # Only rebuilds changed files / Перебудовує тільки змінені
```

### Parallel Builds / Паралельні збірки

```bash
# Use all CPU cores / Використати всі ядра CPU
make html SPHINXOPTS="-j auto"
```

### Build Only What You Need / Збирайте тільки що потрібно

```bash
# Working on Ukrainian translation? / Працюєте над українським перекладом?
make html-uk  # Don't build all languages / Не збирайте всі мови

# Working on specific page? / Працюєте над конкретною сторінкою?
# Edit, save, then:
make html  # Quick incremental build / Швидка інкрементальна збірка
```

---

## Advanced Usage / Розширене використання

### Custom Build Directory / Кастомна директорія збірки

```bash
# Build to different location / Зібрати в іншу локацію
sphinx-build -b html docs /tmp/my-docs
```

### Build Specific Files / Зібрати конкретні файли

```bash
# Build only specific .rst file / Зібрати тільки конкретний .rst
sphinx-build -b html docs docs/_build/html docs/installation.rst
```

### Check Links / Перевірити посилання

```bash
# Check for broken links / Перевірити зламані посилання
make linkcheck

# View report / Переглянути звіт
cat docs/_build/linkcheck/output.txt
```

---

## Build Artifacts / Артефакти збірки

After build, you'll have / Після збірки у вас буде:

```
docs/_build/
├── html/           # English HTML / Англійський HTML
│   ├── index.html
│   ├── installation.html
│   ├── _static/
│   └── _sources/
├── html/uk/        # Ukrainian HTML / Український HTML
├── html/ru/        # Russian HTML / Російський HTML
├── gettext/        # Translation templates / Шаблони перекладів
│   ├── index.pot
│   ├── installation.pot
│   └── ...
└── doctrees/       # Sphinx cache / Кеш Sphinx
```

---

## Next Steps / Наступні кроки

- [Project Structure](structure.md) - Understand project organization
- [Testing](testing.md) - Test your changes
- [Translation Workflow](../translation/workflow.md) - Work with translations

- [Структура проекту](structure.md) - Зрозуміти організацію проекту
- [Тестування](testing.md) - Протестувати зміни
- [Робочий процес перекладів](../translation/workflow.md) - Працювати з перекладами

