#!/usr/bin/env python3
import json
from jinja2 import Environment, FileSystemLoader

def translate(text, locale='en', translations={}):
    return translations.get(locale, {}).get(text, text)

# Load translations from JSON file
with open('templates/translations.json', 'r') as file:
    translations = json.load(file)

# Set up Jinja environment
env = Environment(
    loader=FileSystemLoader('templates')
)

# Add the function as a filter
env.filters['translate'] = translate

# Load and render the template with the appropriate context
template = env.get_template('index.html.j2')
context = {
    'locale': 'es',  # Change locale as needed
    'translations': translations  # Pass translations to the context
}
print(template.render(context))
