from django.contrib import admin

# Register your models here.
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'creation_date', 'user')
    list_filter = ('status', 'user')
    search_fields = ('title', 'description')