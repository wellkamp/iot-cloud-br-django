from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sensors.views import SensorsViewSet
from auth.views import RegisterView


router = DefaultRouter()
router.register('sensor', SensorsViewSet, basename='Sensor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
]