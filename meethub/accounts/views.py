from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
# from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render

from meethub.accounts.forms import SignUpForm
from meethub.accounts.models import Account
# Create your views here.


class SignUp(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('accounts:login')


class HomePageView(TemplateView):
    """
    Homepage view that displays the main landing page for MeetHub.
    Includes dynamic statistics and featured content.
    """
    template_name = 'registration/homepage.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add dynamic statistics
        context['stats'] = {
            'total_members': Account.objects.filter(is_active=True).count(),
            'total_events': self.get_total_events(),
            'total_groups': self.get_total_groups(),
            'total_cities': self.get_total_cities(),
        }
        
        # Add featured events or groups if you have them
        # context['featured_events'] = Event.objects.filter(is_featured=True)[:3]
        # context['featured_groups'] = Group.objects.filter(is_featured=True)[:3]
        
        return context
    
    def get_total_events(self):
        """
        Get total number of events.
        Replace with your actual Event model query.
        """
        # return Event.objects.count()
        return 10247  # Placeholder number
    
    def get_total_groups(self):
        """
        Get total number of groups.
        Replace with your actual Group model query.
        """
        # return Group.objects.count()
        return 512  # Placeholder number
    
    def get_total_cities(self):
        """
        Get total number of cities with active groups.
        Replace with your actual query.
        """
        # return Group.objects.values('city').distinct().count()
        return 50  # Placeholder number


# Function-based view alternative
# def homepage_view(request):
#     """
#     Function-based view alternative for the homepage.
#     """
#     context = {
#         'stats': {
#             'total_members': Account.objects.filter(is_active=True).count(),
#             'total_events': 10247,  # Replace with actual count
#             'total_groups': 512,    # Replace with actual count
#             'total_cities': 50,     # Replace with actual count
#         }
#     }
    
#     # If you have featured content models, add them here
#     # context['featured_events'] = Event.objects.filter(is_featured=True)[:3]
#     # context['featured_groups'] = Group.objects.filter(is_featured=True)[:3]
    
#     return render(request, 'homepage.html', context)

