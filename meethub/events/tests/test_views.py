from django.test import TestCase
from django.urls import reverse

from meethub.comments.models import Comment
from meethub.comments.forms import CommentForm

from meethub.events.models import Event, Category, User



class EventListViewTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='iyanu', password=12345, email='iyanu@gmail.com')
        user.save()

        category = Category.objects.create(name='Technology', description='This is the future')

        number_of_events = 15
        for event_num in range(number_of_events):
            Event.objects.create(name='Party Outside', details='This party is gonna be banging again',
                                 venue='Mapo Hall',
                                 date='2018-05-18', time='12:25:00', category=category, creator=user)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='iyanu', password=12345)
        resp = self.client.get('')

        # Check the user is logged in
        self.assertEqual(str(resp.context['user']), 'iyanu')

        # Check that we got a response 'success'
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='iyanu', password='12345')
        resp = self.client.get(reverse('events:event-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='iyanu', password='12345')
        resp = self.client.get(reverse('events:event-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'events/list_of_events.html')

    def test_pagination_is_ten(self):
        self.client.login(username='iyanu', password='12345')
        resp = self.client.get(reverse('events:event-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['events']) == 10)

    def test_list_all_events_on_second_page(self):
        self.client.login(username='iyanu', password='12345')
        resp = self.client.get(reverse('events:event-list') + '?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['events']) == 5)


class EventDetailViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='iyanu', password=12345, email='iyanu@gmail.com')
        self.attendee = User.objects.create_user(username='tobi', password=56789)
        self.attendee.save()
        self.user.save()
        self.category = Category.objects.create(name='Technology', description='This is the future')
        self.event = Event.objects.create(name='Party Outside', details='This party is gonna be banging again',
                                          venue='Mapo Hall',
                                          date='2018-05-18', time='12:25:00', category=self.category, creator=self.user)

    def test_detail_of_event(self):
        self.client.login(username='iyanu', password=12345)
        response = self.client.get(self.event.get_absolute_url())

        # Check the user is logged in
        self.assertEqual(str(response.context['user']), 'iyanu')

        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-detail', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-detail', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/detail.html')

    def test_name_of_event(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(self.event.get_absolute_url())
        self.assertContains(response, self.event.name, html=True)

    def test_details_of_event(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(self.event.get_absolute_url())
        self.assertContains(response, self.event.details, html=True)

    def test_category_of_event(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(self.event.get_absolute_url())
        self.assertEqual(self.category, self.event.category)

    def test_creator_of_event(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(self.event.get_absolute_url())
        self.assertContains(response, self.event.creator.username)

    def test_list_attendees_for_a_detail_event(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-detail', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['attending'])

    def test_list_of_comments_for_a_detail_event(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-detail', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEquals(len(response.context['comments']), self.event.comments.all().count())

    def test_comment_form_on_event_detail_page(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-detail', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'])

    def test_create_comment_form_displays_comment_on_event_detail_page(self):
        self.client.login(username='iyanu', password='12345')
        comment = Comment.objects.create(comment='Wow, how far', created_by=self.user, event=self.event)
        response = self.client.get(self.event.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Wow')

    def test_valid_create_comment_form_on_event_detail_page_can_post_comment(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.post(self.event.get_absolute_url(),
                                    data={'comment': 'Wow, how far tobi', 'event': 'self.event.pk',
                                          'created_by': 'self.user'})
        new_response = self.client.get(self.event.get_absolute_url())
        self.assertEqual(new_response.status_code, 200)
        self.assertEqual(Comment.objects.last().comment, 'Wow, how far tobi')


class EventCreateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='iyanu', password=12345, email='iyanu@gmail.com')
        self.attendee = User.objects.create_user(username='tobi', password=56789)
        self.attendee.save()
        self.user.save()
        self.category = Category.objects.create(name='Technology', description='This is the future')
        self.event = Event.objects.create(name='Party Outside', details='This party is gonna be banging again',
                                          venue='Mapo Hall',
                                          date='2018-05-18', time='12:25:00', category=self.category, creator=self.user)

    def test_create_event_url_exists_at_desired_location(self):
        self.client.login(username='iyanu', password=12345)
        response = self.client.get('/events/new/')

        # Check the user is logged in
        self.assertEqual(str(response.context['user']), 'iyanu')

        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/create_form.html')

    def test_event_form_is_on_create_event_page(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-create'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'])

    def test_create_event_form_displays_event_on_event_detail_page(self):
        self.client.login(username='iyanu', password='12345')
        event = Event.objects.create(name='Party Outside', details='This party is gonna be banging again',
                                     venue='Mapo Hall',
                                     date='2018-05-18', time='12:25:00', category=self.category, creator=self.user)
        response = self.client.get(event.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'party is gonna')

    def test_valid_create_event_form_on_can_post_event(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.post(reverse('events:event-create'),
                                    data={'name': 'Party Outside', 'details': 'This party is gonna be banging again',
                                          'venue': 'Mapo Hall', 'date': '2018-05-18', 'time': '12:25:00',
                                          'category': self.category, 'creator': self.user})
        new_response = self.client.get(self.event.get_absolute_url())
        self.assertEqual(new_response.status_code, 200)
        self.assertEqual(Event.objects.last().details, 'This party is gonna be banging again')


class EventUpdateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='iyanu', password=12345, email='iyanu@gmail.com')
        self.attendee = User.objects.create_user(username='tobi', password=56789)
        self.attendee.save()
        self.user.save()
        self.category = Category.objects.create(name='Technology', description='This is the future')
        self.event = Event.objects.create(name='Party Outside', details='This party is gonna be banging again',
                                          venue='Mapo Hall',
                                          date='2018-05-18', time='12:25:00', category=self.category, creator=self.user)

    def test_update_event_url_exists_at_desired_location(self):
        event = Event.objects.create(name='Google io', details='Android is coming for you',
                                          venue='Google Plex',
                                          date='2018-11-18', time='10:25:00', category=self.category, creator=self.user)
        self.client.login(username='iyanu', password=12345)
        response = self.client.get(reverse('events:event-update', kwargs={'pk': self.event.pk}))

        # Check the user is logged in
        # self.assertEqual(str(response.context['user']), 'iyanu')

        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-update', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-update', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/update_form.html')

    def test_event_form_is_on_update_event_page(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-update', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'])

    def test_valid_update_event_form_on_can_update_event(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.post(reverse('events:event-update', kwargs={'pk': self.event.pk}),
                                    data={'name': 'Party Outside', 'details': 'This party is gonna be banging again',
                                          'venue': 'Mapo Hall', 'date': '2018-05-18', 'time': '12:25:00',
                                          'category': self.category, 'creator': self.user})
        new_response = self.client.get(self.event.get_absolute_url())
        self.assertEqual(new_response.status_code, 200)
        self.assertEqual(Event.objects.last().details, 'This party is gonna be banging again')


class EventDeleteViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='iyanu', password=12345, email='iyanu@gmail.com')
        self.attendee = User.objects.create_user(username='tobi', password=56789)
        self.attendee.save()
        self.user.save()
        self.category = Category.objects.create(name='Technology', description='This is the future')
        self.event = Event.objects.create(name='Party Outside', details='This party is gonna be banging again',
                                          venue='Mapo Hall',
                                          date='2018-05-18', time='12:25:00', category=self.category, creator=self.user)

    def test_delete_event_url_exists_at_desired_location(self):
        event = Event.objects.create(name='Google io', details='Android is coming for you',
                                          venue='Google Plex',
                                          date='2018-11-18', time='10:25:00', category=self.category, creator=self.user)
        self.client.login(username='iyanu', password=12345)
        response = self.client.get(reverse('events:event-delete', kwargs={'pk': self.event.pk}))

        # Check the user is logged in
        # self.assertEqual(str(response.context['user']), 'iyanu')

        # Check that we got a response 'success'
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-delete', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.get(reverse('events:event-delete', kwargs={'pk': self.event.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/delete.html')

    def test_delete_view_redirect_to_list_view(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.post(reverse('events:event-delete', kwargs={'pk': self.event.pk}))
        # self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/')


class AttendEventTestView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='iyanu', password=12345, email='iyanu@gmail.com')
        self.attendee = User.objects.create_user(username='tobi', password=56789)
        self.attendee.save()
        self.user.save()
        self.category = Category.objects.create(name='Technology', description='This is the future')
        self.event = Event.objects.create(name='Party Outside', details='This party is gonna be banging again',
                                          venue='Mapo Hall',
                                          date='2018-05-18', time='12:25:00', category=self.category, creator=self.user)

    def test_attend_event_url_exists_at_desired_location(self):
        event = Event.objects.create(name='Google io', details='Android is coming for you',
                                          venue='Google Plex',
                                          date='2018-11-18', time='10:25:00', category=self.category, creator=self.user)
        self.client.login(username='iyanu', password=12345)
        response = self.client.post(reverse('events:attend_event', kwargs={'event_id': self.event.id}))
        self.assertNotEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.post(reverse('events:attend_event', kwargs={'event_id': self.event.id}))
        self.assertNotEqual(response.status_code, 200)

    def test_attend_event_view_redirect_to_event_detail(self):
        self.client.login(username='iyanu', password='12345')
        response = self.client.post(reverse('events:attend_event', kwargs={'event_id': self.event.id}))
        self.assertRedirects(response, reverse('events:event-detail', kwargs={'pk': self.event.pk}))






