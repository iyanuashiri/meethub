
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CategorySerializer, EventSerializer, CommentSerializer, ProfileSerializer, ActionSerializer
from events.models import Category, Event, Comment
from userprofile.models import Profile
from events.models import User


class CategoryViewset(viewsets.ReadOnlyModelViewSet):
    """
    This provides list and retrieve actions
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EventViewset(viewsets.ModelViewSet):
    """
    An authenticated user can list, retrieve, create, update, delete, and attend an event
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(detail=True)
    def attend_event(self, request, *args, **kwargs):
        event = self.get_object()
        event.attendees.add(request.user)
        return Response({'attend': True})


class CommentViewset(viewsets.ModelViewSet):
    """
    An authenticated user can list, create, edit and delete a comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ProfileViewset(viewsets.ModelViewSet):
    """
    An authenticated user can retrieve, create and edit their profile
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


