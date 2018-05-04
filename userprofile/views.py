from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin, TemplateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy

from events.views import EventList
from events.models import Event, Comment
from .forms import ProfileForm, UserForm
from .models import Profile


# Create your views here.


class EditProfile(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'userprofile/update_form.html'
    success_message = "%(Profile)s was updated successfully"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['user_form'] = UserForm(instance=request.user)
        context['profile_form'] = ProfileForm(instance=request.user.profile)
        return self.render_to_response(context)

    def post(self, request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        context = {'user_form': user_form, 'profile_form': profile_form}
        return self.render_to_response(context)


def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'userprofile/update_form.html', {'user_form': user_form, 'profile_form': profile_form})


class UserDetail(generic.DetailView):
    model = User
    template_name = 'userprofile/profile_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(creator=self.request.user)
        context['comments'] = Comment.objects.filter(created_by=self.request.user)
        return context
