from django.contrib import admin
from .models import Incident


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'latitude', 'longitude', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at']

    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'status')
        }),
        ('Координати', {
            'fields': ('latitude', 'longitude')
        }),
        ('Метадані', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )