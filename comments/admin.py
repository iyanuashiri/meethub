from django.contrib import admin

from .models import Comment
# Register your models here.


class CommentAdmin(admin.ModelAdmin):

    list_display = ('comment', 'created_date', 'created_time')
    fields = ('event', 'comment', 'created_by')
    search_fields = ('comment',)


admin.site.register(Comment, CommentAdmin)
