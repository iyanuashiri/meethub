from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Event
from .forms import CommentForm


# Create your views here.


class EventList(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'events/list_of_events.html'
    context_object_name = 'events'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Event.objects.all()
        else:
            return Event.objects.filter(creator=self.request.user)


def event_detail(request, pk):

    event = get_object_or_404(Event, pk=pk)

    comments = event.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.event = event
            new_comment.created_by = request.user
            new_comment.save()
            messages.success(request, 'Comment was created successfully')
            return redirect('meet:event-detail', pk=event.pk)
    else:
        form = CommentForm()

    return render(request, 'events/detail.html', {'event': event, 'comments': comments, 'form': form})


class EventFormMixin(object):
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EventCreate(LoginRequiredMixin, SuccessMessageMixin, EventFormMixin, generic.CreateView):
    model = Event
    template_name = 'events/create_form.html'
    fields = ('category', 'name', 'details', 'venue', 'time', 'date')
    context_object_name = 'event'
    success_message = "%(name)s was created successfully"


class EventUpdate(LoginRequiredMixin, SuccessMessageMixin, EventFormMixin, generic.UpdateView):
    model = Event
    template_name = 'events/update_form.html'
    template_name_suffix = '_update_form'
    fields = ('category', 'name', 'details', 'venue', 'time', 'date', 'creator')
    success_message = "%(name)s was updated successfully"


class EventDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Event
    template_name = 'events/delete.html'
    success_url = reverse_lazy('event-list')
    context_object_name = 'event'
    success_message = "%(name)s was deleted successfully"
