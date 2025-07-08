from django.urls import path
from django.contrib.auth import views as auth_views

from meethub.accounts import views

app_name = 'accounts'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
]