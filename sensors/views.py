from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Sensor
from .serializers import SensorSerializer
# Create your views here.


class SensorsViewSet(viewsets.ModelViewSet):
    """Exibir todos os sensores"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
