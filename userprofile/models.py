from django.db import models
from django.conf import settings

from cloudinary.models import CloudinaryField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = CloudinaryField('image')

    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return '{0}\'s profile'.format(self.user.username)

    def get_date_of_birth(self):
        return self.user.date_of_birth
