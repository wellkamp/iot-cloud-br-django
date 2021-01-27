from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Sensor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sensor_name = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    humidity = models.CharField(max_length=50)
    last_date = models.DateField()
    last_hour = models.TimeField()

    def __str__(self):
        return self.user


