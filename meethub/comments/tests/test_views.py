from django.test import TestCase
from django.shortcuts import reverse

from meethub.events.models import Event, User, Category
from meethub.comments.models import Comment



class CommentDeleteViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='iyanu', password=12345, email='iyanu@gmail.com')
        self.attendee = User.objects.create_user(username='tobi', password=56789)
        self.attendee.save()
        self.user.save()
        self.category = Category.objects.create(name='Technology', description='This is the future')
        self.event = Event.objects.create(name='Party Outside', details='This party is gonna be banging again',
                                          venue='Mapo Hall',
                                          date='2018-05-18', time='12:25:00', category=self.category, creator=self.user)
        self.comment = Comment.objects.create(comment='Hey yo', event=self.event, created_by=self.user)


    def test_delete_comment_url_exists_at_desired_location(self):
        comment = Comment.objects.create(comment='Hey yo', event=self.event, created_by=self.user)
        self.client.login(username='iyanu', password=12345)
        response = self.client.get(reverse('comments:comment-delete', kwargs={'pk': self.comment.pk}))

        # Check the user is logged in
        # self.assertEqual(str(response.context['user']), 'iyanu')

        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('comments:comment-delete', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('comments:comment-delete', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comments/delete.html')

    def test_delete_view_redirect_to_event_detail_view(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('comments:comment-delete', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, self.event.get_absolute_url())
