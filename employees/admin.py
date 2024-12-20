from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'designation', 'course', 'created_date')
    list_filter = ('designation', 'course', 'gender')
    search_fields = ('name', 'email', 'mobile')
    ordering = ('-created_date',)
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('image', 'name', 'email', 'mobile', 'gender')
        }),
        ('Professional Details', {
            'fields': ('designation', 'course')
        }),
    )