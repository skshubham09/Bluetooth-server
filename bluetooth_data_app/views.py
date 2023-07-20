# bluetooth_data_app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Device, TimestampedData
from .serializers import TimestampedDataSerializer, DeviceSerializer

@api_view(['POST'])
def receive_bluetooth_data(request):
    device_id = request.data.get('device_id')
    device_name = request.data.get('device_name')
    health_data = request.data.get('health_data')

    device, created = Device.objects.get_or_create(device_id=device_id, defaults={'device_name': device_name})

    timestamped_data = TimestampedData(device=device, health_data=health_data)
    timestamped_data.save()

    return Response({'message': 'Bluetooth data received successfully.'})

@api_view(['GET'])
def get_bluetooth_data(request):
    data = TimestampedData.objects.select_related('device').all()
    timestamped_serializer = TimestampedDataSerializer(data, many=True)

    # Fetch the distinct devices separately and serialize them
    devices = Device.objects.values('device_id', 'device_name').distinct()
    device_serializer = DeviceSerializer(devices, many=True)

    return Response({'timestamped_data': timestamped_serializer.data, 'devices': device_serializer.data})
