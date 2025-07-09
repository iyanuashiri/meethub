from django import forms

from meethub.events.models import Event, Category


class EventForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Event
        fields = ('category', 'name', 'details', 'venue', 'time', 'date',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

