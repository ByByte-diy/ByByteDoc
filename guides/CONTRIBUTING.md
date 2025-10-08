# Contributing to ByByte Documentation
# Внесок у документацію ByByte

Thank you for your interest in contributing!

Дякуємо за ваш інтерес до внесків!

---

## ⚠️ Important: Discuss Before Contributing / Важливо: Обговоріть перед внеском

**Before making any changes or adding new contributions, please communicate and coordinate your intentions with the project moderators.**

This helps us:
- Understand the direction of the project
- Guide your skills and efforts in the right direction
- Maximize the impact for both the project and each contributor
- Ensure your efforts are not wasted

**We value every contribution and want to make sure your work is meaningful and aligned with project goals.**

---

**Перед тим як вносити правки, додавати нові внески, повідомте та узгодьте ваші наміри з модератором.**

Це дасть нам:
- Розуміння руху проекту
- Можливість направити ваші вміння та бажання в вірному напрямку
- Максимальний ефект як для проекту, так і для кожного контриб'ютора
- Впевненість, що ваші старання не будуть марними

**Ми цінимо кожний внесок, та хочемо щоб ваші старання не були марними.**

### How to Communicate / Як зв'язатися

1. **Open a Discussion / Відкрийте обговорення:**
   - Go to [GitHub Discussions](https://github.com/vergilium/ByByteDoc/discussions)
   - Describe what you want to contribute
   - Wait for feedback from maintainers

2. **Create an Issue / Створіть Issue:**
   - Go to [GitHub Issues](https://github.com/vergilium/ByByteDoc/issues/new)
   - Use template: "Contribution Proposal"
   - Explain your planned changes

3. **Contact Maintainers / Зв'яжіться з мейнтейнерами:**
   - Tag `@vergilium` in discussions or issues
   - Provide clear description of your intentions

**Only after receiving approval, proceed with your contribution.**

**Тільки після отримання схвалення, приступайте до внесення змін.**

---

## Quick Start / Швидкий старт

```bash
# 1. Fork and clone / 1. Форк і клон
git clone https://github.com/YOUR_USERNAME/ByByteDoc.git
cd ByByteDoc

# 2. Install dependencies / 2. Встановити залежності
pip install -r docs/requirements.txt

# 3. Create branch / 3. Створити гілку
git checkout -b fix/improve-installation-docs

# 4. Make changes / 4. Внести зміни
nano docs/installation.rst

# 5. Build and test / 5. Зібрати та протестувати
make html
xdg-open docs/_build/html/installation.html

# 6. Commit and push / 6. Закомітити та запушити
git add docs/installation.rst
git commit -m "Improve installation instructions"
git push origin fix/improve-installation-docs

# 7. Create Pull Request on GitHub / 7. Створити Pull Request на GitHub
```

---

## Ways to Contribute / Способи зробити внесок

### 📝 Documentation Improvements / Покращення документації

- Fix typos and grammar / Виправити друкарські помилки та граматику
- Improve clarity / Покращити ясність
- Add examples / Додати приклади
- Update outdated information / Оновити застарілу інформацію

### 🌍 Translations / Переклади

- Translate to Ukrainian / Перекласти українською
- Translate to Russian / Перекласти російською
- Add new language / Додати нову мову
- Fix translation errors / Виправити помилки перекладу

### 🐛 Bug Reports / Звіти про помилки

- Report documentation errors / Повідомити про помилки в документації
- Report broken links / Повідомити про зламані посилання
- Report build issues / Повідомити про проблеми збірки

### ✨ New Features / Нові функції

- Add new documentation pages / Додати нові сторінки документації
- Improve navigation / Покращити навігацію
- Add diagrams / Додати діаграми

---

## Contribution Guidelines / Гайдлайни контрибуцій

### Documentation Standards / Стандарти документації

1. **Write in English first** / **Спочатку пишіть англійською**
   - All source `.rst` files are in English
   - Translations come later via `.po` files

2. **Follow reStructuredText syntax** / **Дотримуйтесь синтаксису reStructuredText**
   - Use proper heading hierarchy
   - Include code blocks with language
   - Add cross-references

3. **Keep paragraphs concise** / **Тримайте параграфи стислими**
   - One idea per paragraph
   - Use lists for multiple items
   - Add examples

4. **Test your changes** / **Тестуйте зміни**
   ```bash
   make html
   # Verify in browser
   ```

### Translation Standards / Стандарти перекладів

1. **Preserve formatting** / **Зберігайте форматування**
   ```po
   msgid "**bold** and *italic*"
   msgstr "**жирний** і *курсив*"
   ```

2. **Don't translate code** / **Не перекладайте код**
   ```po
   msgid "pip install bybyte"
   msgstr "pip install bybyte"  # ← Keep as-is
   ```

3. **Keep technical terms consistent** / **Тримайте технічні терміни послідовними**
   - device → пристрій (завжди)
   - install → встановити (завжди)

4. **Test translated build** / **Тестуйте перекладену збірку**
   ```bash
   make html-uk
   xdg-open docs/_build/html/uk/index.html
   ```

---

## Branch Naming / Іменування гілок

Use descriptive branch names / Використовуйте описові назви гілок:

- `fix/typo-in-installation` - Bug fixes / Виправлення помилок
- `feat/add-troubleshooting-section` - New features / Нові функції
- `docs/improve-api-reference` - Documentation / Документація
- `translate/uk/installation` - Translations / Переклади
- `refactor/restructure-quickstart` - Refactoring / Рефакторинг

---

## Commit Messages / Повідомлення комітів

Write clear commit messages / Пишіть чіткі повідомлення комітів:

**Good / Добре:**
```
Fix typo in installation guide

Changed "instalation" to "installation" in docs/installation.rst
```

**Bad / Погано:**
```
fix
```

### Format / Формат:

```
<type>: <short description>

<detailed description>
<why the change was needed>

Fixes #123
```

Types / Типи:
- `docs:` - Documentation changes / Зміни документації
- `fix:` - Bug fixes / Виправлення помилок
- `feat:` - New features / Нові функції
- `translate:` - Translations / Переклади
- `refactor:` - Code restructuring / Реструктуризація коду
- `test:` - Testing / Тестування

---

## Pull Request Process / Процес Pull Request

### Before Submitting / Перед відправкою

1. **Update from main** / **Оновіть з main**
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-branch
   git rebase main
   ```

2. **Build and test** / **Зберіть та протестуйте**
   ```bash
   make clean
   make html-all
   ./scripts/check-translations.sh
   ```

3. **Check for errors** / **Перевірте помилки**
   ```bash
   make html SPHINXOPTS="-W"  # Fail on warnings
   ```

### Creating PR / Створення PR

1. **Use descriptive title** / **Використовуйте описовий заголовок**
   ```
   Fix installation instructions for macOS
   ```

2. **Fill out PR template** / **Заповніть шаблон PR**
   - What changed
   - Why it changed
   - How to test

3. **Link related issues** / **Пов'яжіть пов'язані issue**
   ```
   Fixes #42
   Related to #38
   ```

### After Submitting / Після відправки

1. **Respond to reviews** / **Відповідайте на ревʼю**
2. **Make requested changes** / **Внесіть запитані зміни**
3. **Keep PR updated** / **Тримайте PR оновленим**

---

## Code Review / Ревʼю коду

### As Author / Як автор

- Be open to feedback / Будьте відкриті до зворотного зв'язку
- Explain your decisions / Поясніть свої рішення
- Ask questions if unclear / Ставте питання, якщо незрозуміло

### As Reviewer / Як ревʼювер

- Be constructive / Будьте конструктивними
- Explain why changes are needed / Поясніть чому потрібні зміни
- Approve when ready / Схваліть коли готово

---

## Testing Checklist / Контрольний список тестування

Before submitting PR / Перед відправкою PR:

- [ ] Code builds without errors / Код збирається без помилок
- [ ] No Sphinx warnings / Немає попереджень Sphinx
- [ ] All links work / Всі посилання працюють
- [ ] Changes tested in browser / Зміни протестовані в браузері
- [ ] Translations updated (if applicable) / Переклади оновлені (якщо застосовно)
- [ ] Commit messages are clear / Повідомлення комітів чіткі
- [ ] PR description filled out / Опис PR заповнено

---

## Getting Help / Отримати допомогу

### Documentation / Документація

- Read [Developer Guide](README.md)
- Check [Building Documentation](development/building.md)
- See [Project Structure](development/structure.md)

### Translation Help / Допомога з перекладом

- Read [Translation Workflow](translation/workflow.md)
- Check [Translation Tools](translation/tools.md)
- See [Translation Examples](translation/examples.md)

### Ask Questions / Ставити питання

- Open an issue: [GitHub Issues](https://github.com/vergilium/ByByteDoc/issues)
- Tag with `question` label
- Be specific about your problem

---

## Community Guidelines / Гайдлайни спільноти

### Be Respectful / Будьте поважними

- Treat everyone with respect / Ставтеся до всіх з повагою
- Be patient with newcomers / Будьте терплячими з новачками
- Give constructive feedback / Давайте конструктивний фідбек

### Be Collaborative / Будьте колаборативними

- Share knowledge / Діліться знаннями
- Help others / Допомагайте іншим
- Learn together / Вчіться разом

---

## Recognition / Визнання

All contributors will be:
- Listed in project contributors / Перелічені в контриб'юторах проекту
- Credited in release notes / Згадані в release notes
- Part of the project history / Частина історії проекту

---

## License / Ліцензія

By contributing, you agree that your contributions will be licensed under the same license as the project.

Роблячи внесок, ви погоджуєтесь, що ваш внесок буде ліцензовано під тією ж ліцензією, що й проект.

---

## Thank You! / Дякуємо!

Thank you for contributing to ByByte documentation! Every contribution, no matter how small, makes a difference.

Дякуємо за внесок у документацію ByByte! Кожен внесок, навіть малий, має значення.

🎉 Happy contributing! / Успішних контрибуцій! 🎉

