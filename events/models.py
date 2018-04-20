from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(max_length=1000)
    venue = models.CharField(max_length=50)
    date = models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
    time = models.TimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attending', blank=True)

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def get_absolute_url(self):
        return reverse('meet: event-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def num_of_attendees(self):
        return Event.attendees.count()


class Comment(models.Model):
    post = models.TextField(max_length=500)
    created_date = models.DateField(auto_now=True)
    created_time = models.TimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_date', 'created_time')

    def get_absolute_url(self):
        return reverse('meet:event-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.post
