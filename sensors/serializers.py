from rest_framework import serializers
from .models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'user', 'sensor_name',
                  'temperature', 'humidity', 'last_date', 'last_hour']