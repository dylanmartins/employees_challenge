from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email',
        'department', 
        'created_at',
        'updated_at'
    )

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)