from django.test import TestCase

from events.models import Category, Event, User
from userprofile.models import Profile

from comments.models import Comment


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Technology', description='This is the future')
        user = User.objects.create(username='iyanu', password=12345, email='iyanu@gmail.com')
        event = Event.objects.create(name='Party Out', details='This party is gonna be banging', venue='Ibadan',
                                     date='2018-06-18', time='12:00:00', category=category, creator=user)
        Comment.objects.create(comment='Hey yo', event=event, created_by=user)
        Profile.objects.create(date_of_birth='2018-12-12', user=user)

    def test_comment_object_name(self):
        comment = Comment.objects.get(comment='Hey yo')
        expected_object_name = '{}'.format(comment)
        self.assertEquals(expected_object_name, str(comment))

    def test_get_absolute_url(self):
        comment = Comment.objects.get(comment='Hey yo')
        self.assertEquals(comment.get_absolute_url(), '/events/4/')

    def test_get_comment_creator_photo(self):
        comment = Comment.objects.get(comment='Hey yo')
        self.assertEquals(comment.get_comment_creator_photo(), None)

    def test_comment_max_length(self):
        comment = Comment.objects.get(comment='Hey yo')
        max_length = comment._meta.get_field('comment').max_length
        self.assertEquals(max_length, 500)
