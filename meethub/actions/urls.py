from django.urls import path

from meethub.actions import views


app_name = 'actions'
urlpatterns = [
    path('notifications/', views.NotificationList.as_view(), name='notification_list')
]
