from django import template

from polls.models import Quote


register = template.Library()


@register.simple_tag
def parsing_output():
    random_quote = Quote.objects.order_by('?').first()
    her_author = random_quote.author
    return random_quote.quote, her_author.name
