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

    class Meta:
        ordering = ('created_date', 'created_time')

    def get_absolute_url(self):
        return reverse('events:event-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.comment

    def get_comment_creator_photo(self):
        return self.created_by.profile.photo
