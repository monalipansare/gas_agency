from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_type', 'description', 'status')
    list_filter = ('status', 'service_type')
    search_fields = ('service_type', 'description', 'status')

