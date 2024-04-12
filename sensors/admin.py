import json

import manage
from django.contrib import admin

from .models import Sensor, SensorLog


@admin.action(description='Активация')
def activate(modeladmin, request, queryset):
    queryset.update(sensor_active=True)


@admin.action(description='Деактивация')
def deactivate(modeladmin, request, queryset):
    queryset.update(sensor_active=False)


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['sensor_name', 'sensor_MAC', 'sensor_description', 'sensor_email', 'sensor_status']
    search_fields = ['sensor_name', 'sensor_MAC', 'sensor_title', 'sensor_description', 'sensor_email']
    list_filter = ['sensor_status', 'sensor_email']
    actions = [deactivate, activate]


@admin.register(SensorLog)
class SensorLogAdmin(admin.ModelAdmin):
    list_display = ['sensor_name', 'sensor_MAC', 'sensor_status_change', 'sensor_status']
    search_fields = ['sensor_name', 'sensor_MAC', 'sensor_status_change', 'sensor_status']
    list_filter = ['sensor_name', 'sensor_MAC']
