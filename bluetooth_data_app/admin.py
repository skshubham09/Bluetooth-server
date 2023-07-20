
from django.contrib import admin
from .models import Device, TimestampedData

admin.site.register(Device)
admin.site.register(TimestampedData)
