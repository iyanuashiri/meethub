from django.test import TestCase
from django.contrib.auth.models import User

from userprofile.forms import ProfileForm
from userprofile.models import Profile


class ProfileFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='iyanu', password=12345, email='iyanu@gmail.com')
        Profile.objects.create(user=self.user, date_of_birth='2018-05-18', photo='')

    def test_profile_form_valid(self):
        form = ProfileForm(data={'user': 'self.user', 'date_of_birth': '2018-05-18', 'photo': ''})
        self.assertTrue(form.is_valid())

    def test_profile_form_date_of_birth_field_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['date_of_birth'].label == None or form.fields['date_of_birth'].label == 'Date of birth')

    def test_profile_form_photo_field_label(self):
        form = ProfileForm()
        self.assertTrue(form.fields['photo'].label == None or form.fields['photo'].label == 'Image')
