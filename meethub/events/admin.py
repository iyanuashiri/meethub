from django.contrib import admin

from meethub.events.models import Category, Event

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'description')
    fields = ('name', 'description')


admin.site.register(Category, CategoryAdmin)


class EventAdmin(admin.ModelAdmin):

    list_display = ('name', 'venue', 'date', 'time')
    fields = ('category', 'name', 'creator', 'details', 'venue', ('date', 'time'))
    search_fields = ('name', 'details')

admin.site.register(Event, EventAdmin)


