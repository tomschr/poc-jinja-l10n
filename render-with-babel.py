#!/usr/bin/env python3
import json
import os
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape
from babel.support import Translations
# from gettext import translation, NullTranslations

# Set up Jinja environment
env = Environment(
  loader= FileSystemLoader(searchpath="templates" ),
  extensions=['jinja2.ext.i18n', ],
  autoescape=select_autoescape(['html', 'xml'])
)

# Get the language from the command line
# $PROG [<lang> [<count>]]
count = 1
if len(sys.argv) == 1:
   lang= "en"
elif len(sys.argv) == 2:
   lang = sys.argv[1]
elif len(sys.argv) == 3:
    lang = sys.argv[1]
    count = sys.argv[2]
else:
   pass


# Prepare translations
trans = Translations.load('locale', [lang])
env.install_gettext_translations(trans)
# env.newstyle_gettext = True

# Load and render the template with the appropriate context
template = env.get_template('index-babel.html.j2')

# Prepare the context
context = {
    'count': int(count),
    'user': os.environ.get('USER', 'Tux'),
    'locale': lang,
}

print(template.render(context))
