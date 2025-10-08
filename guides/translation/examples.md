# Translation Example: Full Text, Not Just Headers
# Приклад перекладу: Весь текст, не тільки заголовки
# Пример перевода: Весь текст, не только заголовки

## Visual Example / Візуальний приклад / Визуальный пример

### Original English Source (installation.rst)

```rst
Installation
============

This guide will help you install and set up ByByte.

Requirements
------------

* Arduino IDE or compatible software
* Required hardware components
* Python 3.x (for tools)

Installation Steps
------------------

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/vergilium/ByByte.git
      cd ByByte

2. Install dependencies:

   .. code-block:: bash

      # Install Python dependencies
      pip install -r requirements.txt

3. Configure the project:

   .. code-block:: bash

      # Copy example config
      cp config.example.ini config.ini
      # Edit config.ini with your settings

Hardware Setup
--------------

Connect your Arduino board according to the wiring diagram.

.. warning::
   Make sure to disconnect power before making any hardware connections.

Verification
------------

To verify your installation:

.. code-block:: bash

   # Run test script
   python test_connection.py

If everything is configured correctly, you should see a success message.

Next Steps
----------

Continue to the :doc:`quickstart` guide to begin using ByByte.
```

---

### What Gets Extracted for Translation

After running `make gettext`, **EVERY text element becomes translatable**:

```
✅ "Installation" ← Header
✅ "This guide will help you install and set up ByByte." ← Paragraph
✅ "Requirements" ← Header
✅ "Arduino IDE or compatible software" ← List item
✅ "Required hardware components" ← List item
✅ "Python 3.x (for tools)" ← List item
✅ "Installation Steps" ← Header
✅ "Clone the repository:" ← Text before code
❌ "git clone https://github.com/..." ← Code (NOT translated)
✅ "Install dependencies:" ← Text before code
❌ "pip install -r requirements.txt" ← Code (NOT translated)
✅ "# Install Python dependencies" ← Comment in code (CAN translate!)
✅ "Configure the project:" ← Text
✅ "Hardware Setup" ← Header
✅ "Connect your Arduino board according to the wiring diagram." ← Paragraph
✅ "Make sure to disconnect power..." ← Warning text
✅ "Verification" ← Header
✅ "To verify your installation:" ← Text
✅ "# Run test script" ← Comment (CAN translate!)
✅ "If everything is configured correctly..." ← Paragraph
✅ "Next Steps" ← Header
✅ "Continue to the :doc:`quickstart` guide..." ← Paragraph with link
```

---

### Translation File (installation.po)

```po
# Every sentence/paragraph becomes a msgid/msgstr pair!

#: ../../installation.rst:2
msgid "Installation"
msgstr "Встановлення"  # ← TRANSLATE THIS

#: ../../installation.rst:4
msgid "This guide will help you install and set up ByByte."
msgstr "Цей посібник допоможе вам встановити та налаштувати ByByte."  # ← TRANSLATE THIS

#: ../../installation.rst:7
msgid "Requirements"
msgstr "Вимоги"  # ← TRANSLATE THIS

#: ../../installation.rst:9
msgid "Arduino IDE or compatible software"
msgstr "Arduino IDE або сумісне програмне забезпечення"  # ← TRANSLATE THIS

#: ../../installation.rst:10
msgid "Required hardware components"
msgstr "Необхідні апаратні компоненти"  # ← TRANSLATE THIS

#: ../../installation.rst:11
msgid "Python 3.x (for tools)"
msgstr "Python 3.x (для інструментів)"  # ← TRANSLATE THIS

#: ../../installation.rst:14
msgid "Installation Steps"
msgstr "Кроки встановлення"  # ← TRANSLATE THIS

#: ../../installation.rst:16
msgid "Clone the repository:"
msgstr "Клонуйте репозиторій:"  # ← TRANSLATE THIS

# Code blocks are preserved as-is
#: ../../installation.rst:20
msgid "git clone https://github.com/vergilium/ByByte.git\ncd ByByte"
msgstr "git clone https://github.com/vergilium/ByByte.git\ncd ByByte"  # ← DON'T TRANSLATE

#: ../../installation.rst:23
msgid "Install dependencies:"
msgstr "Встановіть залежності:"  # ← TRANSLATE THIS

# But comments CAN be translated!
#: ../../installation.rst:27
msgid "# Install Python dependencies"
msgstr "# Встановіть залежності Python"  # ← CAN TRANSLATE

#: ../../installation.rst:28
msgid "pip install -r requirements.txt"
msgstr "pip install -r requirements.txt"  # ← DON'T TRANSLATE

#: ../../installation.rst:30
msgid "Configure the project:"
msgstr "Налаштуйте проект:"  # ← TRANSLATE THIS

#: ../../installation.rst:34
msgid "# Copy example config"
msgstr "# Скопіюйте приклад конфігурації"  # ← CAN TRANSLATE

#: ../../installation.rst:35
msgid "cp config.example.ini config.ini"
msgstr "cp config.example.ini config.ini"  # ← DON'T TRANSLATE

#: ../../installation.rst:36
msgid "# Edit config.ini with your settings"
msgstr "# Відредагуйте config.ini своїми налаштуваннями"  # ← CAN TRANSLATE

#: ../../installation.rst:39
msgid "Hardware Setup"
msgstr "Налаштування обладнання"  # ← TRANSLATE THIS

#: ../../installation.rst:41
msgid "Connect your Arduino board according to the wiring diagram."
msgstr "Підключіть вашу плату Arduino згідно зі схемою підключення."  # ← TRANSLATE THIS

#: ../../installation.rst:44
msgid "Make sure to disconnect power before making any hardware connections."
msgstr "Переконайтеся, що живлення відключено перед виконанням будь-яких апаратних підключень."  # ← TRANSLATE THIS

#: ../../installation.rst:47
msgid "Verification"
msgstr "Перевірка"  # ← TRANSLATE THIS

#: ../../installation.rst:49
msgid "To verify your installation:"
msgstr "Щоб перевірити ваше встановлення:"  # ← TRANSLATE THIS

#: ../../installation.rst:53
msgid "# Run test script"
msgstr "# Запустіть тестовий скрипт"  # ← CAN TRANSLATE

#: ../../installation.rst:54
msgid "python test_connection.py"
msgstr "python test_connection.py"  # ← DON'T TRANSLATE

#: ../../installation.rst:56
msgid "If everything is configured correctly, you should see a success message."
msgstr "Якщо все налаштовано правильно, ви побачите повідомлення про успіх."  # ← TRANSLATE THIS

#: ../../installation.rst:59
msgid "Next Steps"
msgstr "Наступні кроки"  # ← TRANSLATE THIS

#: ../../installation.rst:61
msgid "Continue to the :doc:`quickstart` guide to begin using ByByte."
msgstr "Перейдіть до посібника :doc:`quickstart`, щоб почати використовувати ByByte."  # ← TRANSLATE THIS
```

---

### Resulting Ukrainian HTML

```html
<h1>Встановлення</h1>
<p>Цей посібник допоможе вам встановити та налаштувати ByByte.</p>

<h2>Вимоги</h2>
<ul>
  <li>Arduino IDE або сумісне програмне забезпечення</li>
  <li>Необхідні апаратні компоненти</li>
  <li>Python 3.x (для інструментів)</li>
</ul>

<h2>Кроки встановлення</h2>
<ol>
  <li>
    <p>Клонуйте репозиторій:</p>
    <pre>git clone https://github.com/vergilium/ByByte.git
cd ByByte</pre>
  </li>
  <li>
    <p>Встановіть залежності:</p>
    <pre># Встановіть залежності Python
pip install -r requirements.txt</pre>
  </li>
  <li>
    <p>Налаштуйте проект:</p>
    <pre># Скопіюйте приклад конфігурації
cp config.example.ini config.ini
# Відредагуйте config.ini своїми налаштуваннями</pre>
  </li>
</ol>

<h2>Налаштування обладнання</h2>
<p>Підключіть вашу плату Arduino згідно зі схемою підключення.</p>

<div class="warning">
  <p>Переконайтеся, що живлення відключено перед виконанням будь-яких апаратних підключень.</p>
</div>

<h2>Перевірка</h2>
<p>Щоб перевірити ваше встановлення:</p>
<pre># Запустіть тестовий скрипт
python test_connection.py</pre>

<p>Якщо все налаштовано правильно, ви побачите повідомлення про успіх.</p>

<h2>Наступні кроки</h2>
<p>Перейдіть до посібника <a href="quickstart.html">Швидкий старт</a>, щоб почати використовувати ByByte.</p>
```

---

## Key Points / Ключові моменти / Ключевые моменты

### ✅ What Gets Translated / Що перекладається / Что переводится

1. **All text content** / **Весь текстовий контент** / **Весь текстовый контент**
   - Headers / Заголовки / Заголовки
   - Paragraphs / Параграфи / Параграфы
   - List items / Елементи списків / Элементы списков
   - Notes, warnings / Примітки, попередження / Примечания, предупреждения
   - Link text / Текст посилань / Текст ссылок

2. **Code comments** (optional) / **Коментарі в коді** (опціонально) / **Комментарии в коде** (опционально)
   - `# Install dependencies` → `# Встановіть залежності`

### ❌ What Stays in English / Що залишається англійською / Что остается на английском

1. **Code** / **Код** / **Код**
   - `git clone`, `pip install`, `python script.py`
   - Function names, variable names
   - Command-line tools

2. **RST directives** / **RST директиви** / **RST директивы**
   - `.. code-block::`, `.. note::`, `.. warning::`
   - `:ref:`, `:doc:` targets

3. **URLs and file paths** / **URL та шляхи до файлів** / **URL и пути к файлам**
   - `https://github.com/...`
   - `config.example.ini`

---

## Workflow Summary / Підсумок процесу / Итог процесса

```bash
# 1. Write English .rst
nano docs/installation.rst

# 2. Extract ALL text for translation
make gettext
# Creates: docs/_build/gettext/installation.pot

# 3. Update .po files
make update
# Updates: docs/locale/uk/LC_MESSAGES/installation.po

# 4. Translate ALL msgstr fields
poedit docs/locale/uk/LC_MESSAGES/installation.po
# OR edit manually with any text editor

# 5. Build translated docs
make html-uk
# Result: docs/_build/html/uk/installation.html

# 6. View result
xdg-open docs/_build/html/uk/installation.html
```

---

## Tools Comparison / Порівняння інструментів / Сравнение инструментов

| Tool | Visual | Translation Memory | Spell Check | Best For |
|------|--------|-------------------|-------------|----------|
| **Poedit** | ✅ GUI | ✅ Yes | ✅ Yes | **Recommended** |
| **Lokalize** | ✅ GUI | ✅ Yes | ✅ Yes | KDE users |
| **Text Editor** | ❌ No | ❌ No | ⚠️ Maybe | Quick edits |
| **Weblate** | ✅ Web | ✅ Yes | ✅ Yes | Team collaboration |

---

## Progress Tracking / Відстеження прогресу / Отслеживание прогресса

```bash
# Check translation statistics
./scripts/check-translations.sh

# Output:
# 📄 installation.po:
#    18 translated messages.
# 
# 📊 Total for Ukrainian:
#    ✅ Translated: 36
#    ❌ Untranslated: 166
#    📈 Progress: 17%
```

---

## Remember / Пам'ятайте / Помните

**Every sentence, every paragraph, every list item = separate translatable string!**

**Кожне речення, кожен параграф, кожен пункт списку = окремий рядок для перекладу!**

**Каждое предложение, каждый параграф, каждый пункт списка = отдельная переводимая строка!**

This approach:
- ✅ Scales to ANY documentation size
- ✅ Maintains single source of truth (English .rst)
- ✅ Easy to update when English changes
- ✅ Supported by ReadTheDocs natively
- ✅ Professional translation tools available

Цей підхід:
- ✅ Масштабується на будь-який розмір документації
- ✅ Зберігає єдине джерело правди (англійська .rst)
- ✅ Легко оновлювати при зміні англійського тексту
- ✅ Підтримується ReadTheDocs нативно
- ✅ Доступні професійні інструменти перекладу

Этот подход:
- ✅ Масштабируется на любой размер документации
- ✅ Сохраняет единый источник истины (английский .rst)
- ✅ Легко обновлять при изменении английского текста
- ✅ Поддерживается ReadTheDocs нативно
- ✅ Доступны профессиональные инструменты перевода

