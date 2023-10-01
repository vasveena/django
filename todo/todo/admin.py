from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    list_filter = ('is_completed',)
    search_fields = ('task',)
    ordering = ('-updated_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('task', 'is_completed')
        }),
        ('Date information', {
            'fields': ('created_at', 'updated_at')
        }),
    )
# Register your models here.
admin.site.register(Task, TaskAdmin)
