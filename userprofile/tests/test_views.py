from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from userprofile.models import Profile


class ProfileDetailViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='iyanu', password=12345, email='iyanu@gmail.com')
        self.user.save()
        self.profile = Profile.objects.create(user=self.user, date_of_birth='2018-05-18', photo='')

    def test_user_detail(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(self.profile.get_absolute_url())

        # Check the user is logged in
        self.assertEqual(str(response.context['user']), 'iyanu')

        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('userprofile:detail', kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('userprofile:detail', kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofile/profile_detail.html')

    def test_events_created_by_this_profile(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(self.profile.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['events'])

    def test_comments_created_by_this_profile(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('userprofile:detail', kwargs={'pk': self.profile.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['comments'])

    def test_date_of_birth_of_profile(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('userprofile:detail', kwargs={'pk': self.profile.pk}))
        self.assertContains(response, self.profile.date_of_birth)


class EditProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='iyanu', password=12345, email='iyanu@gmail.com')
        self.profile = Profile.objects.create(user=self.user, date_of_birth='2018-05-18', photo='')

    def test_edit_profile(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get('/userprofile/edit/')

        # Check the user is logged in
        self.assertEqual(str(response.context['user']), 'iyanu')

        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('userprofile:edit'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('userprofile:edit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userprofile/update_form.html')

    def test_valid_edit_profile_form_can_edit_profile(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.post(reverse('userprofile:edit'),
                                    data={'user': 'self.user', 'date_of_birth': '2018-06-18', 'photo': ''})

        self.assertEqual(response.status_code, 200)
        new_response = self.client.get(self.profile.get_absolute_url())
        self.assertEqual(new_response.status_code, 200)
        self.assertEqual(Profile.objects.last().date_of_birth, '2018-06-18')

    def test_edit_profile_form_is_on_edit_profile_page(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('userprofile:edit'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'])







