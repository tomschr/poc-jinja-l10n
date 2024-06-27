#!/usr/bin/env python3
import json
import sys

from jinja2 import Environment, FileSystemLoader

# Load translations from JSON file
with open('templates/translations.json', 'r') as file:
    translations = json.load(file)

def translate(text, locale='en', translations=translations):
    return translations.get(locale, {}).get(text, text)

# Set up Jinja environment
env = Environment(
    loader=FileSystemLoader('templates')
)

if len(sys.argv) > 1:
   lang = sys.argv[1]
else:
   lang = "en"


# Add the function as a filter
env.filters['trans'] = translate

# Load and render the template with the appropriate context
template = env.get_template('index-custom.html.j2')
context = {
    'locale': lang,  # Change locale as needed
    'translations': translations  # Pass translations to the context
}
print(template.render(context))
