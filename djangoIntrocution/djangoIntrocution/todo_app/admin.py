from django.contrib import admin

from djangoIntrocution.todo_app.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

