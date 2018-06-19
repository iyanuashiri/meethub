from django.test import TestCase

from events.models import Category, Event, User
from userprofile.models import Profile

from comments.models import Comment
from comments.forms import CommentForm


class CommentFormTest(TestCase):

    def setUp(self):
        category = Category.objects.create(name='Technology', description='This is the future')
        self.user = User.objects.create(username='iyanu', password=12345, email='iyanu@gmail.com')
        self.event = Event.objects.create(name='Party Out', details='This party is gonna be banging', venue='Ibadan',
                                          date='2018-06-18', time='12:00:00', category=category, creator=self.user)
        Comment.objects.create(comment='Hey yo', event=self.event, created_by=self.user)
        Profile.objects.create(date_of_birth='2018-12-12', user=self.user)

    def test_comment_form_valid(self):
        form = CommentForm(data={'comment': 'Hey yo'})
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form = CommentForm(
            data={'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'comment': ['This field is required.']})

    def test_comment_form_comment_field_label(self):
        form = CommentForm()
        self.assertTrue(form.fields['comment'].label == None or form.fields['comment'].label == 'Comment')
