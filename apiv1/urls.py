from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()
router.register(r'events', viewsets.EventViewset)
router.register(r'comments', viewsets.CommentViewset)
router.register(r'category', viewsets.CategoryViewset)
router.register(r'profile', viewsets.ProfileViewset)

urlpatterns = [
    path('', include(router.urls))
]
