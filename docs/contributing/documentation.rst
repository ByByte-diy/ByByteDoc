Documentation Development
==========================

Contributing to ByByte.DIY project documentation.

.. note::
   **Good documentation is essential for educational projects!**

Overview
--------

ByByte.DIY documentation includes:

* **User Guides** - For students and teachers
* **Developer Docs** - For contributors
* **API Reference** - For library users
* **Tutorials** - Step-by-step learning
* **Translations** - Multi-language support

All documentation must be:

* ✅ **Clear** - Easy to understand
* ✅ **Complete** - Cover all aspects
* ✅ **Accurate** - Technically correct
* ✅ **Accessible** - Well-structured
* ✅ **Translated** - Available in EN, UA, RU

Documentation Stack
-------------------

We use:

* **Sphinx** - Documentation generator
* **reStructuredText** - Markup language
* **ReadTheDocs** - Hosting platform
* **sphinx-intl** - Translation management
* **Git** - Version control

Requirements
------------

Writing Style
~~~~~~~~~~~~~

**For User Documentation:**

* Use simple, clear language
* Avoid technical jargon
* Provide examples
* Use active voice
* Keep sentences short

**For Technical Documentation:**

* Be precise and accurate
* Define terms
* Include code examples
* Reference related docs
* Use proper formatting

Structure
~~~~~~~~~

Each document should have:

1. **Title** - Clear, descriptive
2. **Overview** - Brief introduction
3. **Prerequisites** - What reader needs to know
4. **Main Content** - Detailed information
5. **Examples** - Practical demonstrations
6. **Troubleshooting** - Common issues
7. **Next Steps** - Where to go next

Formatting
~~~~~~~~~~

Use proper reStructuredText:

.. code-block:: rst

   Page Title
   ==========
   
   Brief introduction to the topic.
   
   Section Heading
   ---------------
   
   Content...
   
   Subsection
   ~~~~~~~~~~
   
   More content...
   
   .. warning::
      Important warnings use this format!
   
   .. note::
      Helpful tips use this format.
   
   .. code-block:: cpp
   
      // Code examples with syntax highlighting
      void setup() {
        Serial.begin(9600);
      }

Content Guidelines
------------------

Images
~~~~~~

* Use high-quality screenshots
* Add descriptive captions
* Optimize file sizes
* Place in ``_static/images/``
* Reference properly

.. code-block:: rst

   .. image:: _static/images/example.png
      :alt: Description of image
      :width: 600px
      :align: center

Code Blocks
~~~~~~~~~~~

Always specify language:

.. code-block:: rst

   .. code-block:: cpp
   
      // Arduino code
      void loop() {
        // code
      }
   
   .. code-block:: python
   
      # Python code
      def example():
          pass
   
   .. code-block:: bash
   
      # Shell commands
      make html

Links
~~~~~

**Internal links:**

.. code-block:: rst

   See :doc:`installation` for setup instructions.
   
   Jump to :ref:`specific-section`.

**External links:**

.. code-block:: rst

   Visit `Arduino <https://www.arduino.cc>`_ website.

Lists
~~~~~

.. code-block:: rst

   Unordered list:
   
   * Item 1
   * Item 2
     
     * Nested item
   
   Ordered list:
   
   1. First step
   2. Second step
   3. Third step

Tables
~~~~~~

.. code-block:: rst

   .. list-table:: Component List
      :header-rows: 1
      :widths: 30 20 20 30
   
      * - Component
        - Quantity
        - Price
        - Notes
      * - Arduino Nano
        - 1
        - $5
        - Clone acceptable
      * - HC-SR04
        - 1
        - $2
        - Ultrasonic sensor

Translation Workflow
--------------------

ByByte.DIY docs are available in 3 languages:

* **English (en)** - Primary language
* **Ukrainian (uk)** - Рідна мова
* **Russian (ru)** - Дополнительный язык

Translation Process
~~~~~~~~~~~~~~~~~~~

1. **Extract Translatable Strings**

   .. code-block:: bash

      make gettext

2. **Update Translation Catalogs**

   .. code-block:: bash

      make update

3. **Translate .po Files**

   Edit files in ``docs/locale/[lang]/LC_MESSAGES/``
   
   .. code-block:: po

      #: ../../index.rst:5
      msgid "Welcome to БАБАЙ documentation"
      msgstr "Ласкаво просимо до документації БАБАЙ"

4. **Build Translated Docs**

   .. code-block:: bash

      make html-uk    # Ukrainian
      make html-ru    # Russian
      make html-all   # All languages

Translation Guidelines
~~~~~~~~~~~~~~~~~~~~~~

* Keep technical terms consistent
* Preserve formatting (``**bold**``, code blocks)
* Don't translate code examples
* Translate comments in code
* Review translations before committing

Development Setup
-----------------

1. **Clone Repository**

   .. code-block:: bash

      git clone https://github.com/vergilium/ByByteDoc.git
      cd ByByteDoc

2. **Install Dependencies**

   .. code-block:: bash

      pip install -r docs/requirements.txt

3. **Test Local Build**

   .. code-block:: bash

      make html
      xdg-open docs/_build/html/index.html

4. **Create Branch**

   .. code-block:: bash

      git checkout -b docs/improve-installation

Making Changes
--------------

Workflow
~~~~~~~~

1. **Edit .rst Files**

   Use any text editor

2. **Build Locally**

   .. code-block:: bash

      make html

3. **Check for Errors**

   Fix any warnings or errors

4. **Preview Changes**

   Open in browser to verify

5. **Commit Changes**

   .. code-block:: bash

      git add docs/filename.rst
      git commit -m "Improve installation guide clarity"

6. **Push and Create PR**

   .. code-block:: bash

      git push origin docs/improve-installation

Submission Process
------------------

1. **Proposal**
   
   For major changes, open GitHub Issue first:
   
   * Describe what you want to improve
   * Explain why it's needed
   * Provide examples

2. **Make Changes**
   
   * Follow style guidelines
   * Build and test locally
   * Check for broken links

3. **Submit PR**
   
   Include in PR description:
   
   * What was changed
   * Why it was changed
   * Screenshots (if visual changes)

4. **Review**
   
   Maintainers will:
   
   * Check accuracy
   * Verify formatting
   * Test builds
   * Provide feedback

5. **Merge**
   
   Once approved, changes are merged

Quality Checklist
-----------------

Before submitting:

- [ ] Content is accurate
- [ ] Spelling and grammar checked
- [ ] Code examples tested
- [ ] Images optimized
- [ ] Links work
- [ ] Builds without warnings
- [ ] Follows style guide
- [ ] Translations updated (if applicable)
- [ ] Preview looks correct

Common Tasks
------------

Adding New Page
~~~~~~~~~~~~~~~

1. Create ``.rst`` file in ``docs/``
2. Add to ``toctree`` in ``index.rst``
3. Build and verify
4. Commit and submit

Updating Existing Page
~~~~~~~~~~~~~~~~~~~~~~

1. Edit ``.rst`` file
2. Build locally
3. Verify changes
4. Update translations if needed
5. Commit and submit

Adding Images
~~~~~~~~~~~~~

1. Place image in ``docs/_static/images/``
2. Optimize size (< 500KB)
3. Reference in ``.rst`` file
4. Add descriptive alt text
5. Test rendering

Fixing Broken Links
~~~~~~~~~~~~~~~~~~~

1. Identify broken link
2. Update or remove
3. Check related pages
4. Build and verify
5. Commit fix

Troubleshooting
---------------

Build Errors
~~~~~~~~~~~~

**"WARNING: document isn't included in any toctree"**

* Add document to ``index.rst`` toctree

**"WARNING: undefined label"**

* Check reference targets exist
* Fix typos in references

**"ERROR: Unknown directive type"**

* Check directive spelling
* Ensure extensions loaded in ``conf.py``

Translation Issues
~~~~~~~~~~~~~~~~~~

**Missing translations:**

.. code-block:: bash

   make update  # Regenerate .po files

**Encoding errors:**

* Ensure .po files are UTF-8
* Check for special characters

Tools
-----

Recommended Editors
~~~~~~~~~~~~~~~~~~~

* **VS Code** - With reStructuredText extension
* **Sublime Text** - With RST plugins
* **PyCharm** - Built-in RST support
* **Vim/Emacs** - With RST modes

Translation Tools
~~~~~~~~~~~~~~~~~

* **Poedit** - GUI for .po files
* **Lokalize** - KDE translation tool
* **Text editor** - Manual editing

Resources
---------

* **Sphinx Documentation** - https://www.sphinx-doc.org/
* **reStructuredText Primer** - https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
* **ReadTheDocs Guide** - https://docs.readthedocs.io/
* **Developer Guide** - See ``guides/development/`` in repository

Examples
--------

Good Documentation Examples:

* Clear installation instructions
* Step-by-step tutorials with images
* Complete API references
* Troubleshooting guides

Questions?
----------

* Open GitHub Issue with tag ``documentation``
* Contact ``@vergilium``
* Join documentation discussion

---

:doc:`Back to Contributing Overview <index>`
