from django.test import TestCase

from events.forms import EventForm, CommentForm
from events.models import Event, Comment, Category, User
from userprofile.models import Profile


class EventFormTest(TestCase):


    def setUp(self):
        self.category = Category.objects.create(name='Technology', description='This is the future')
        self.user = User.objects.create(username='iyanu', password=12345, email='iyanu@gmail.com')
        Event.objects.create(name='Party Outside', details='This party is gonna be banging again', venue='Mapo Hall',
                             date='2018-05-18', time='12:25:00', category=self.category, creator=self.user)

    def test_event_form_invalid(self):
        form = EventForm(data={'name': '', 'details': '', 'venue': 'Mapo Hall',
                               'date': '2018-05-18', 'time': '12:25:00', 'category': 'category', 'creator': 'user'})
        self.assertFalse(form.is_valid())

    def test_event_form_date_field_label(self):
        form = EventForm()
        self.assertTrue(form.fields['date'].label == None or form.fields['date'].label == 'Date')

    def test_event_form_date_field_help_text(self):
        form = EventForm()
        self.assertEqual(form.fields['date'].help_text, 'Please use the following format: <em>YYYY-MM-DD</em>.')

    def test_event_form_time_field_label(self):
        form = EventForm()
        self.assertTrue(form.fields['time'].label == None or form.fields['time'].label == 'Time')

    def test_event_form_time_field_help_text(self):
        form = EventForm()
        self.assertEqual(form.fields['time'].help_text, 'Please use the following format: <em>HH:MM:SS<em>')

    def test_event_form_name_field_label(self):
        form = EventForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Name')

    def test_event_form_details_field_label(self):
        form = EventForm()
        self.assertTrue(form.fields['details'].label == None or form.fields['details'].label == 'Details')

    def test_event_form_venue_field_label(self):
        form = EventForm()
        self.assertTrue(form.fields['venue'].label == None or form.fields['venue'].label == 'Venue')

    def test_event_form_category_field_label(self):
        form = EventForm()
        self.assertTrue(form.fields['category'].label == None or form.fields['category'].label == 'Category')


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



















