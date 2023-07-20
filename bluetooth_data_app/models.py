# bluetooth_data_app/models.py
from django.db import models

class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    device_mac_address = models.CharField(max_length=17)
    device_manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return self.device_name

class TimestampedData(models.Model):
    timestamped_data_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    health_data = models.FloatField()

    def __str__(self):
        return f"{self.device.device_name} - {self.timestamp}"
