from django.contrib import admin
from urls_and_views.departments.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
