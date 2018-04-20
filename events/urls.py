from django.urls import path
from . import views

app_name = 'events'
urlpatterns = [
    path('events/', views.EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', views.event_detail, name='event-detail'),
    path('events/new/', views.EventCreate.as_view(), name='event-create' ),
    path('events/<int:pk>/delete', views.EventDelete.as_view(), name='event-delete'),
    path('events/<int:pk>/update', views.EventUpdate.as_view(), name='event-update'),
]
