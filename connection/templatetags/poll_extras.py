from django import template
from django.template.defaultfilters import stringfilter

from polls.models import Quote

import json

import os

import re

dir_path = os.path.dirname(os.path.realpath("word.json"))


register = template.Library()


@register.simple_tag
def parsing_output():
    random_quote = Quote.objects.order_by('?').first()
    her_author = random_quote.author
    li = list()
    li.append(random_quote)
    li.append(her_author)
    return li


@register.filter
@stringfilter
def replace_func(value):
    with open(dir_path + '/' + 'word.json', 'r') as f:
        data = json.load(f)
    for word in data:
        change = re.sub(r'\b' + word + r'\b', '****', value)
        value = change
    return value
