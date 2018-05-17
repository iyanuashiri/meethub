import datetime
import mock
from django.test import TestCase

from events.models import Event, Category, Comment, User
from userprofile.models import Profile


class EventModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Technology', description='This is the future')
        user = User.objects.create(username='iyanu', password=12345, email='iyanu@gmail.com')
        Event.objects.create(name='Party Outside', details='This party is gonna be banging again', venue='Mapo Hall',
                             date='2018-05-18', time='12:25:00', category=category, creator=user)

    def test_name_label(self):
        event = Event.objects.get(name='Party Outside')
        field_label = event._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_details_label(self):
        event = Event.objects.get(name='Party Outside')
        field_label = event._meta.get_field('details').verbose_name
        self.assertEquals(field_label, 'Details')

    def test_venue_label(self):
        event = Event.objects.get(name='Party Outside')
        field_label = event._meta.get_field('venue').verbose_name
        self.assertEquals(field_label, 'venue')

    def test_date_label(self):
        event = Event.objects.get(name='Party Outside')
        field_label = event._meta.get_field('date').verbose_name
        self.assertEquals(field_label, 'date')

    def test_time_label(self):
        event = Event.objects.get(name='Party Outside')
        field_label = event._meta.get_field('time').verbose_name
        self.assertEquals(field_label, 'time')

    def test_name_max_length(self):
        event = Event.objects.get(name='Party Outside')
        max_length = event._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_venue_max_length(self):
        event = Event.objects.get(name='Party Outside')
        max_length = event._meta.get_field('venue').max_length
        self.assertEquals(max_length, 200)

    def test_event_object_name(self):
        event = Event.objects.get(name='Party Outside')
        expected_object_name = '{}'.format(event.name)
        self.assertEquals(expected_object_name, str(event))

    def test_get_absolute_url(self):
        event = Event.objects.get(name='Party Outside')
        self.assertEquals(event.get_absolute_url(), '/events/4/')

    def test_get_number_of_attendees(self):
        event = Event.objects.get(name='Party Outside')
        self.assertEquals(event.get_number_of_attendees(), 0)

    def test_get_comments_number(self):
        event = Event.objects.get(name='Party Outside')
        self.assertEquals(event.get_comments_number(), 0)

    def test_verbose_name_plural(self):
        self.assertEquals(str(Event._meta.verbose_name_plural), 'events')


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Technology', description='This is the future')

    def test_category_object_name(self):
        category = Category.objects.get(name='Technology')
        expected_object_name = '{}'.format(category.name)
        self.assertEquals(expected_object_name, str(category))

    def test_category_verbose_name_plural(self):
        self.assertEquals(str(Category._meta.verbose_name_plural), 'categories')


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
        self.assertEquals(comment.get_absolute_url(), '/events/2/')

    def test_get_comment_creator_photo(self):
        comment = Comment.objects.get(comment='Hey yo')
        self.assertEquals(comment.get_comment_creator_photo(), None)

    def test_comment_max_length(self):
        comment = Comment.objects.get(comment='Hey yo')
        max_length = comment._meta.get_field('comment').max_length
        self.assertEquals(max_length, 500)

