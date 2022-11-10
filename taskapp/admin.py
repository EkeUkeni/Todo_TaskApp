from django.contrib import admin
from taskapp.models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user','title','preview','created_at', 'updated_at')
    list_display_links = ('title',)
    list_filter = ['completed','created_at', 'updated_at']
    date_hierarchy = "created_at"
    search_fields = ['title', 'description']

admin.site.register(Task, TaskAdmin)
# admin.site.register(ToDOlist)