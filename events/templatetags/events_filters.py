from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='total_attendees')
def all_caps(text):
    pass