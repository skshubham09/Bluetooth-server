# bluetooth_data_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('receive_bluetooth_data/', views.receive_bluetooth_data, name='receive_bluetooth_data'),
    path('get_bluetooth_data/', views.get_bluetooth_data, name='get_bluetooth_data'),
]
