from django import template

register = template.Library()


@register.filter()
def censor(text):
    return text
