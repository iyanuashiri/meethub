from django import template
from ..models import Event, Comment

register = template.Library()


@register.simple_tag(name='total')
def total_attending():
    return

@register.simple_tag()
def total_comments():
    return Comment.objects.count()