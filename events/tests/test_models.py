from django.test import TestCase

import pytest
from events.models import Event, Category, User


@pytest.mark.django_db
def test_category_model(category):
    assert category.name == 'Software'
    assert category.description == 'For software developers'
    assert str(Category._meta.verbose_name_plural) == 'categories'


@pytest.mark.django_db
def test_event_model(event, category, account):
    assert event.details == 'For Python developers'
    assert event.name == 'Pycon'
    assert event.venue == 'jand'
    assert event.creator == account
    assert event.category == category
    assert event.get_number_of_attendees() == 0
    assert event.get_comments_number() == 0


@pytest.mark.django_db
def test_event_label(event):
    assert event._meta.get_field('name') == 'name'
    assert event._meta.get_field('details') == 'details'
    assert event._meta.get_field('venue') == 'venue'
    assert event._meta.get_field('date') == 'date'
    assert event._meta.get_field('time') == 'time'
    assert event._meta.get_field('category') == 'category'
    assert event._meta.get_field('creator') == 'creator'
    assert event._meta.get_field('attendees') == 'attendees'
    assert event._meta.get_field('num_of_attendees') == 'num of attendees'


@pytest.mark.django_db
def test_field_attributes(event):
    assert event._meta.get_field('name').max_length == 50
    assert event._meta.get_field('venue').max_length == 200
    assert Event._meta.verbose_name_plural == 'events'


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
        self.assertEquals(event.get_absolute_url(), '/events/13/')

    def test_get_absolute_url_not_none(self):
        event = Event.objects.get(name='Party Outside')
        self.assertIsNotNone(event.get_absolute_url())

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
