from django import forms

from tinymce import TinyMCE

from .models import Event, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class EventForm(forms.ModelForm):
    details = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required':False, 'cols':30, 'rows':10}
        )
    )

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
