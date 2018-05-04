from django.urls import path

from . import views


app_name = 'actions'
urlpatterns = [
    path('', views.NotificationList.as_view(), name='notification_list')
]
