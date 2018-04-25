from django import forms

from .models import Event, Comment


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('category', 'name', 'details', 'venue', 'time', 'date',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
