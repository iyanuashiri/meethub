from rest_framework import serializers

from events.models import Category, Event, Comment
from userprofile.models import Profile
from actions.models import Action


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'description')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Event
        fields = ('id', 'url', 'name', 'details', 'venue', 'date', 'time', 'category', 'creator',
                  'attendees')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.ReadOnlyField(source='event.name')

    class Meta:
        model = Comment
        fields = ('id', 'url', 'comment', 'created_date', 'created_time', 'event', 'created_by')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ('id', 'url', 'user', 'date_of_birth', 'photo')


class ActionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Action
        fields = ('id', 'url', 'user', 'verb', 'created')