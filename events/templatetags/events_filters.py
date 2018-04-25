from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='all_caps')
def all_caps(text):
    return str.upper(text)