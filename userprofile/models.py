from django.db import models
from django.conf import settings

from stream_django.activity import Activity

# Create your models here.


class Profile(models.Model, Activity):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '{0}\'s profile'.format(self.user.username)

    def get_date_of_birth(self):
        return self.user.date_of_birth
