from django.shortcuts import render
from django.views.generic import ListView

from .models import Action

# Create your views here.


class NotificationList(ListView):
    model = Action
    template_name = 'actions/notifications.html'
    context_object_name = 'actions'

    def get_queryset(self):
        return Action.objects.exclude(user=self.request.user)