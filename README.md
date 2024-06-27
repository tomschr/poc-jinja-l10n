# Custom Translations for Jinja templates
A proof-of-concept of a Jinja translation.

This project show two ways to use translatable strings:

* A custom method.
  It's a simple method using JSON as a translation format.
  Other formats are also possible.
* The Babel project.
  This is a more advanced method using Jinja extensions.


## Structure of this repository

* `babel.cfg`: configuration file for Babel
* `locale`: all translations of PO and MO files
* `README.md`: this file
* `render-custom-translations.py`: using a custom method
* `render-with-babel.py`: using the Jinja's extension functions with Babel
* `requirements.txt`: contains requirements for the virtual Python environment
* `templates`: contains all Jinja templates
* `templates/translations.json`: contains all translations 


## Comparison of the two methods
For the two methods the following files and directories are used:

* For the custom method:

   * The `render-custom-translations.py` script
   * The translations in `templates/translations.json`
   * The Jinja template `templates/index.html.j2`

* For the Babel method:

   * The `render-with-babel.py` script
   * The translations in `locale`
   * The Jinja template `templates/index-babel.html.j2`


## General Setup

Use the following steps to create a virtual Python environment which
contains everything you need for this proof-of-concept:

1. Create a virtual Python environment (Python 3.11 preferred):

       $ python3.11 -m venv .venv311

1. Activate the Python environment:

       $ source .venv311/bin/activate

   For Windows users using PowerShell use this:

       .\myenv\Scripts\Activate

1. Install all requirements:

       $ pip install -r requirements.txt



## Using of the custom method

Call the `render-custom-translations.py` command either without any argument:

    $ render-custom-translations.py

or call it with the required language:

    $ render-custom-translations.py de


## Using the Babel method

It's similar to the custom method:

    $ render-with-babel.py
    $ render-with-babel.py de

Before you can do that, you need to create a language catalog.

## Creating new language catalogs with Babel

Babel is a popular library for internationalizing and
localizing Python applications. It works well with Jinja
templates  and provides the following features:

* **Message Extraction**: Extract translatable strings from Python code and Jinja templates.
* **Catalog Management**: Manage translation catalogs.
* **Message Compilation**: Compile message catalogs to binary files for use in the application.
* **Localization**: Format dates, times, numbers, and currencies according to locale.

To create localized language catalogs, proceed as follows:

1. Extract the messages:

       $ pybabel extract -F babel.cfg -o locale/messages.pot .
       extracting messages from ...

1. Initialize a translation, for example Spanish and German:

       $ pybabel init -d locale -l es -i locale/messages.pot
       $ pybabel init -d locale -l de -i locale/messages.pot

1. Translate the PO files in `locale/<LANG>/LC_MESSAGES/messages.po`.

1. Compile all PO files into their respective MO files:

       $ pybabel compile -d locale -l es
       $ pybabel compile -d locale -l de

## Updating existing language catalogs

If you update your Jinja templates with additional translatable strings, proceed as follows:

1. Extract the messages:

       $ pybabel extract -F babel.cfg -o locale/messages.pot .
       extracting messages from ...

1. To update a language catalog, run:

       $ pybabel update -d locale -l es -i locale/messages.pot
    
    Repeat the last step.

1. Translate the missing strings in the PO file(s).

1. Compile all PO files into their respective MO files:

       $ pybabel compile -d locale -l es
       $ pybabel compile -d locale -l de


# Resources

* https://jinja.palletsprojects.com/en/3.0.x/
* https://babel.pocoo.org/en/latest/index.html