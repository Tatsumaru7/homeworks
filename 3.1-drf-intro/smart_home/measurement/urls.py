
from django.urls import path
from .views import SensorView, MeasurementView, CreateMeasurementView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', CreateMeasurementView.as_view(), name='measurement-create'),
]