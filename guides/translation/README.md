# Translation Overview
# Огляд перекладів

Complete guide to translating ByByte documentation.

Повний посібник з перекладу документації ByByte.

---

## 🌍 Supported Languages / Підтримувані мови

| Language | Code | Status | Maintainer |
|----------|------|--------|------------|
| 🇬🇧 English | `en` | ✅ 100% | ByByte Team |
| 🇺🇦 Ukrainian | `uk` | 🔄 1% | - |
| 🇷🇺 Russian | `ru` | 🔄 1% | - |

---

## 📚 Translation Guides / Посібники з перекладу

### For Translators / Для перекладачів

1. **[Translation Workflow](workflow.md)** - Step-by-step process / Покроковий процес
2. **[Translation Guidelines](guidelines.md)** - Rules and best practices / Правила та кращі практики
3. **[Translation Tools](tools.md)** - Software and utilities / Програми та утиліти
4. **[Translation Examples](examples.md)** - Visual examples / Візуальні приклади
5. **[LOCALIZATION.md](LOCALIZATION.md)** - Full localization guide / Повний посібник локалізації

---

## 🚀 Quick Start for Translators / Швидкий старт для перекладачів

```bash
# 1. Setup / Налаштування
git clone https://github.com/vergilium/ByByteDoc.git
cd ByByteDoc
pip install -r docs/requirements.txt

# 2. Extract translation strings / Витягти рядки для перекладу
make gettext
make update

# 3. Open translation file in Poedit / Відкрити файл перекладу в Poedit
poedit docs/locale/uk/LC_MESSAGES/installation.po

# 4. Translate all msgstr fields / Перекласти всі поля msgstr

# 5. Build and test / Зібрати та протестувати
make html-uk
xdg-open docs/_build/html/uk/installation.html

# 6. Submit PR / Відправити PR
git add docs/locale/
git commit -m "Add Ukrainian translation for installation"
git push
```

---

## 📊 Translation Progress / Прогрес перекладів

Check current status / Перевірити поточний статус:

```bash
./scripts/check-translations.sh
```

Output / Вивід:
```
╔════════════════════════════════════════════════╗
║  Translation Progress Check                    ║
╚════════════════════════════════════════════════╝

Language: Ukrainian / Українська (uk)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 index.po:         ✅ 18 translated
📄 installation.po:  ✅ 18 translated
📄 quickstart.po:    ❌ 0 translated, 24 untranslated
📄 usage.po:         ❌ 0 translated, 34 untranslated
📄 api.po:           ❌ 0 translated, 19 untranslated

📊 Total for Ukrainian:
   ✅ Translated: 36
   ❌ Untranslated: 166
   📈 Progress: 17%
```

---

## 🎯 Translation Priorities / Пріоритети перекладів

### High Priority / Високий пріоритет

Most visited pages / Найбільш відвідувані сторінки:

1. ✅ **index.po** - Main page / Головна сторінка (100%)
2. ✅ **installation.po** - Installation guide / Посібник встановлення (100%)
3. ⏳ **quickstart.po** - Quick start / Швидкий старт (0%)

### Medium Priority / Середній пріоритет

4. ⏳ **usage.po** - Usage guide / Посібник використання (0%)
5. ⏳ **api.po** - API reference / Довідник API (0%)

### Low Priority / Низький пріоритет

6. ⏳ **contributing.po** - Contributing / Контрибуції (0%)
7. ⏳ **changelog.po** - Changelog / Історія змін (0%)

---

## 🔧 Translation System / Система перекладів

### How It Works / Як це працює

```
┌─────────────┐
│ English RST │  ← Write documentation in English
│  files      │     Пишіть документацію англійською
└──────┬──────┘
       │
       │ make gettext
       │
       ▼
┌─────────────┐
│  POT files  │  ← Translation templates
│  (templates)│     Шаблони перекладів
└──────┬──────┘
       │
       │ make update
       │
       ▼
┌─────────────┐
│  PO files   │  ← Translate here in Poedit
│ (uk, ru)    │     Перекладайте тут у Poedit
└──────┬──────┘
       │
       │ make html-uk
       │
       ▼
┌─────────────┐
│ Translated  │  ← Built HTML documentation
│    HTML     │     Зібрана HTML документація
└─────────────┘
```

### File Structure / Структура файлів

```
docs/
├── installation.rst              ← English source / Англійське джерело
├── _build/
│   └── gettext/
│       └── installation.pot      ← Template / Шаблон
└── locale/
    ├── uk/LC_MESSAGES/
    │   └── installation.po       ← Ukrainian translation / Український переклад
    └── ru/LC_MESSAGES/
        └── installation.po       ← Russian translation / Російський переклад
```

---

## 🛠️ Translation Tools / Інструменти перекладу

### Recommended / Рекомендовано

**Poedit** ⭐ - Best GUI tool / Найкращий GUI інструмент

- Visual interface / Візуальний інтерфейс
- Translation memory / Пам'ять перекладів
- Spell check / Перевірка орфографії
- Auto-suggestions / Автопідказки

Install / Встановити:
```bash
sudo apt install poedit  # Ubuntu/Debian
brew install poedit      # macOS
```

### Alternative Tools / Альтернативні інструменти

- **Lokalize** - KDE translation tool
- **GTranslator** - GNOME tool
- **Virtaal** - Cross-platform
- **Text editor** - Manual editing / Ручне редагування

See [Translation Tools](tools.md) for details.

---

## 📖 Translation Examples / Приклади перекладів

### Simple Text / Простий текст

```po
msgid "Installation"
msgstr "Встановлення"
```

### Paragraph / Параграф

```po
msgid "This guide will help you install and set up ByByte."
msgstr "Цей посібник допоможе вам встановити та налаштувати ByByte."
```

### With Formatting / З форматуванням

```po
msgid "**Important:** Disconnect power first."
msgstr "**Важливо:** Спочатку відключіть живлення."
```

### Code (Don't Translate) / Код (Не перекладати)

```po
msgid "pip install bybyte"
msgstr "pip install bybyte"  ← Keep as-is / Залишити як є
```

More examples: [Translation Examples](examples.md)

---

## 🎓 Learning Resources / Навчальні ресурси

### Documentation / Документація

- [Sphinx i18n](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx-intl docs](https://sphinx-intl.readthedocs.io/)
- [gettext manual](https://www.gnu.org/software/gettext/manual/)

### Video Tutorials / Відео уроки

- Search YouTube for "Poedit tutorial"
- "How to translate with gettext"

---

## FAQ

### How do I start translating? / Як почати перекладати?

See [Translation Workflow](workflow.md)

### What should I translate first? / Що перекладати спочатку?

Start with high-priority pages: index, installation, quickstart

### Can I use machine translation? / Чи можу я використовувати машинний переклад?

Yes, but always review and fix! DeepL/Google Translate for first pass, then manual review.

Так, але завжди перевіряйте та виправляйте! DeepL/Google Translate для першого проходу, потім ручна перевірка.

### How do I test my translation? / Як протестувати мій переклад?

```bash
make html-uk
xdg-open docs/_build/html/uk/index.html
```

### What if English changes? / Що якщо англійська змінюється?

Run `make update` - it marks changed strings as "fuzzy". Update them and remove fuzzy flag.

Запустіть `make update` - він позначає змінені рядки як "fuzzy". Оновіть їх та видаліть прапорець fuzzy.

### Where do I report translation errors? / Де повідомляти про помилки перекладу?

Open issue on GitHub: https://github.com/vergilium/ByByteDoc/issues

---

## 🤝 Translation Team / Команда перекладачів

Want to become a language maintainer? / Хочете стати мейнтейнером мови?

- Complete at least 50% translation / Завершіть щонайменше 50% перекладу
- Be active and responsive / Будьте активними та відповідальними
- Contact project maintainers / Зв'яжіться з мейнтейнерами проекту

---

## 📝 Next Steps / Наступні кроки

1. Read [Translation Workflow](workflow.md) - Understand the process
2. Install [Translation Tools](tools.md) - Get Poedit
3. Follow [Translation Guidelines](guidelines.md) - Learn best practices
4. Check [Examples](examples.md) - See real examples

---

**Ready to translate?** Start with [Translation Workflow](workflow.md)!

**Готові перекладати?** Почніть з [Робочого процесу перекладу](workflow.md)!

