from django.test import TestCase
from django.contrib.auth.models import User

from userprofile.models import Profile


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='iyanu', password=12345, email='iyanu@gmail.com')
        Profile.objects.create(user=user, date_of_birth='2018-05-18', photo='')

    def test_user_label(self):
        profile = Profile.objects.get(date_of_birth='2018-05-18')
        field_label = profile._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')

    def test_date_of_birth_label(self):
        profile = Profile.objects.get(date_of_birth='2018-05-18')
        field_label = profile._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_photo_label(self):
        profile = Profile.objects.get(date_of_birth='2018-05-18')
        field_label = profile._meta.get_field('photo').verbose_name
        self.assertEquals(field_label, 'image')

    def test_profile_object_name(self):
        profile = Profile.objects.get(date_of_birth='2018-05-18')
        expected_object_name = '{0}\'s profile'.format(profile.user.username)
        self.assertEquals(expected_object_name, str(profile))

    def test_get_absolute_url(self):
        profile = Profile.objects.get(date_of_birth='2018-05-18')
        self.assertEquals(profile.get_absolute_url(), '/userprofile/detail/8/')

    def test_get_absolute_url_not_none(self):
        profile = Profile.objects.get(date_of_birth='2018-05-18')
        self.assertIsNotNone(profile.get_absolute_url())

    def test_verbose_name_plural(self):
        self.assertEquals(str(Profile._meta.verbose_name_plural), 'profiles')

    def test_get_date_of_birth(self):
        profile = Profile.objects.get(date_of_birth='2018-05-18')
        self.assertEquals(profile.get_date_of_birth(), '2018, 5, 18')







