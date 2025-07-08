from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect

from meethub.events.models import Event
from meethub.actions.utils import create_action
from meethub.comments.models import Comment
from meethub.comments.forms import CommentForm


# Create your views here.


class CommentDelete(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Comment
    template_name = 'comments/delete.html'
    context_object_name = 'comment'
    success_message = "Comment was deleted successfully"

    def get_success_url(self):
        return reverse_lazy('events:event-detail', kwargs={'pk': self.get_object(Event.objects.all()).pk})


@login_required()
def comment_detail(request, comment_id, event_id):
    event = get_object_or_404(Event, pk=event_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.event = event
            new_comment.parent = comment
            new_comment.created_by = request.user
            create_action(request.user, 'you replied a comment', comment)
            new_comment.save()
            messages.success(request, 'You replied a comment')
            return redirect('events:event-detail', pk=event_id)

    else:
        form = CommentForm()
    return render(request, 'comments/detail.html', {'comment': comment, 'form': form})


class ReplyCreate(SuccessMessageMixin, generic.CreateView):
    model = Comment
    template_name = 'comments/detail.html'
    fields = ('comment',)
    success_message = 'Reply was added successfully'

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.instance.event = self.get_object(queryset=Event.objects.all())
        form.instance.parent = self.get_object(queryset=Comment.objects.all())
        form.instance.created_by = self.request.user
        create_action(self.request.user, 'added a comment', form.instance)
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('comments:comment-detail', kwargs={'pk': self.get_object(Comment.objects.all()).pk})


class CommentDisplay(generic.DetailView):
    model = Comment
    template_name = 'comments/detail.html'
    context_object_name = 'comment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentDetail(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = CommentDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReplyCreate.as_view()
        return view(request, *args, **kwargs)
