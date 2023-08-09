from django.urls import path
from measurement.views import SensorView, MeasureView
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/<pk>/', SensorView.as_view()),
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasureView.as_view()),
]

