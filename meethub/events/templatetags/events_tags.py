from django import template
# from meethub.events.models import Event
from meethub.comments.models import Comment

register = template.Library()


@register.simple_tag(name='total')
def total_attending():
    pass

@register.simple_tag()
def total_comments():
    return Comment.objects.count()