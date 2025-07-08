from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from meethub.accounts.models import Account
from meethub.profile.models import Profile
from meethub.actions.utils import create_action


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Input a valid email address')

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)
        widgets = {
            # 'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # This is an override of the save() method. It attaches a profile to a user when they register
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:

            user.save()

            # This is the attached profile
            profile = Profile.objects.create(user=user)

            # This creates an action that is displayed in the notifications page whenever an account is created
            create_action(user, 'has created an account')
            user.save()

            return user
