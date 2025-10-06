Contributing
============

We welcome contributions to ByByte! This document provides guidelines for contributing.

Getting Started
---------------

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes
6. Submit a pull request

Development Setup
-----------------

Clone the repository:

.. code-block:: bash

   git clone https://github.com/vergilium/ByByte.git
   cd ByByte

Install development dependencies:

.. code-block:: bash

   pip install -r requirements-dev.txt

Coding Standards
----------------

* Follow PEP 8 style guide for Python code
* Use meaningful variable and function names
* Add docstrings to all functions and classes
* Write unit tests for new features
* Keep commits focused and atomic

Testing
-------

Run tests before submitting:

.. code-block:: bash

   # Run unit tests
   pytest tests/

   # Run with coverage
   pytest --cov=bybyte tests/

   # Run linting
   flake8 bybyte/
   pylint bybyte/

Documentation
-------------

Update documentation when adding new features:

1. Add docstrings to code
2. Update relevant .rst files in docs/
3. Build documentation locally to verify:

   .. code-block:: bash

      cd docs
      make html
      # Open docs/_build/html/index.html

Submitting Changes
------------------

Pull Request Process
~~~~~~~~~~~~~~~~~~~~

1. Update the README.md with details of changes if needed
2. Update the CHANGELOG.rst with your changes
3. Ensure all tests pass
4. Submit pull request with clear description

Commit Messages
~~~~~~~~~~~~~~~

Write clear commit messages:

* Use present tense ("Add feature" not "Added feature")
* Use imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit first line to 72 characters
* Reference issues and pull requests

Example:

.. code-block:: text

   Add temperature sensor support

   - Implement TemperatureSensor class
   - Add calibration methods
   - Update documentation
   - Add unit tests

   Fixes #123

Code Review
-----------

All submissions require review. We use GitHub pull requests for this purpose.

Reviewers will check:

* Code quality and style
* Test coverage
* Documentation completeness
* Backwards compatibility

Bug Reports
-----------

When filing a bug report, include:

* Clear description of the issue
* Steps to reproduce
* Expected behavior
* Actual behavior
* System information (OS, Python version, etc.)
* Error messages and stack traces

Feature Requests
----------------

We welcome feature requests! Please include:

* Clear description of the feature
* Use cases and benefits
* Possible implementation approach
* Willingness to contribute implementation

Community
---------

* Be respectful and inclusive
* Welcome newcomers
* Help others learn
* Give constructive feedback

License
-------

By contributing, you agree that your contributions will be licensed under the same license as the project.

Questions?
----------

If you have questions about contributing, feel free to:

* Open an issue on GitHub
* Contact the maintainers
* Join our community discussions

Thank you for contributing to ByByte! 🎉

