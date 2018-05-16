from rest_framework import serializers

from events.models import Category, Event, Comment, User
from userprofile.models import Profile
from actions.models import Action


class UserSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(many=True, view_name='event-detail', read_only=True)


    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'events')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    event = serializers.HyperlinkedRelatedField(read_only=True, view_name='event-detail')
    created_by = serializers.HyperlinkedRelatedField(read_only=True, view_name='comment-detail')

    class Meta:
        model = Comment
        fields = ('id', 'url', 'comment', 'created_date', 'created_time', 'event', 'created_by')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    creator = serializers.HyperlinkedRelatedField(read_only=True, view_name='event-detail')
    attendees = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='event-detail')
    comments = CommentSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'url', 'name', 'details', 'venue', 'date', 'time', 'category', 'creator',
                  'attendees', 'comments')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'description')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ('id', 'url', 'user', 'date_of_birth', 'photo')


class ActionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Action
        fields = ('id', 'url', 'user', 'verb', 'created')


