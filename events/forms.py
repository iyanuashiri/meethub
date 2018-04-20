from django import forms

from .models import Event, Comment


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('category', 'name', 'details',
                  'venue', 'time', 'date',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('post',)
