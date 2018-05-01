from django.contrib import admin

from .models import Profile
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'photo')


admin.site.register(Profile, ProfileAdmin)