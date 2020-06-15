from django.test import TestCase

import pytest
from events.models import Event, Category


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
