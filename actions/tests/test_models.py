from django.test import TestCase
from django.contrib.auth.models import User

from actions.models import Action



class ActionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='iyanu', password=12345)
        action = Action.objects.create(user = user, verb='is attending', )
