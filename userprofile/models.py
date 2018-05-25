from django.db import models
from django.conf import settings
from django.shortcuts import reverse

from cloudinary.models import CloudinaryField

from events.models import Event
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = CloudinaryField('image', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'profiles'

    def __str__(self):
        return '{0}\'s profile'.format(self.user.username)

    def get_absolute_url(self):
        return reverse('userprofile:detail', kwargs={'pk': self.pk})

    def get_date_of_birth(self):
        return self.date_of_birth

    def is_attending(self):
        if Event.objects.filter(pk=self.pk, attendees=self.user).exists():
            return True
