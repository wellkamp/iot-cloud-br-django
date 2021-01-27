from django.contrib import admin
from sensors.models import Sensor

# Register your models here.


class Sensors(admin.ModelAdmin):
    list_display = ('id', 'user', 'sensor_name',
                    'temperature', 'humidity', 'last_date', 'last_hour')
    list_display_links = ('id', 'user')
    search_fields = ('user',)
    list_per_page = 10


admin.site.register(Sensor, Sensors)
