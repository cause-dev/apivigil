from django.contrib import admin
from .models import Monitor

# Register your models here.

@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'expected_status_code', 'created_at')
    list_filter = ('expected_status_code', 'created_at')
    search_fields = ('name', 'url')
    ordering = ('-created_at',)