from django.db import models
from django.conf import settings
from django.shortcuts import reverse

from events.models import Event
# Create your models here.


class Comment(models.Model):
    comment = models.TextField(max_length=500)
    created_date = models.DateField(auto_now=True)
    created_time = models.TimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    class Meta:
        ordering = ('created_date', 'created_time')

    def get_absolute_url(self):
        return reverse('comments:comment-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.comment

    def get_comment_creator_photo(self):
        return self.created_by.profile.photo

    def get_children(self):
        return self.children.all()

    def get_parents(self):
        return self.parent
