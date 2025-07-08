from django.urls import path
from meethub.comments import views


app_name = 'comments'
urlpatterns = [
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment-delete'),
    path('comments/<comment_id>/<event_id>/detail/', views.comment_detail, name='comment-detail'),

]
