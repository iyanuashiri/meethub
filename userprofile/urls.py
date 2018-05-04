from django.urls import path


from . import views


app_name = 'userprofile'
urlpatterns = [
    path('edit/', views.edit_profile, name='edit'),
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='detail'),
]
