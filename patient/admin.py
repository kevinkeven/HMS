from django.contrib import admin
from .models import Patient, Condition
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city', 'phone', 'email', 'gender']
    list_filter = ['city', 'gender', 'created', 'state']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    search_fields = ('first_name', 'last_name', 'gender', 'created')
    date_hierarchy = 'added'

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ['owner', 'blood_type']
    list_filter = ['blood_type']
    search_fields = ('owner',)