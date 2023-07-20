# bluetooth_data_app/serializers.py
from rest_framework import serializers
from .models import TimestampedData, Device

class TimestampedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimestampedData
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['device_id', 'device_name']  # Include the required fields only
