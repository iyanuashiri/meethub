from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    path('<int:pk>/delete/', views.CommentDelete.as_view(), name='comment-delete'),
    path('<comment_id>/<event_id>/detail/', views.comment_detail, name='comment-detail'),

]
