from django.urls import reverse_lazy
from django.views import generic

from .forms import SignUpForm

# Create your views here.


class SignUp(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
