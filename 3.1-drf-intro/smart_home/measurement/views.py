from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .serializers import MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement

# @api_view
class SensorView(ListCreateAPIView):
       queryset = Sensor.objects.all()
       serializer_class = SensorDetailSerializer
       def get_queryset(self):
               return Sensor.objects.all()
       
       def post(self, request, *args, **kwargs):
               return super().post(request, *args, **kwargs)

class MeasureView(RetrieveUpdateAPIView):
        queryset = Measurement.objects.all()
        serializer_class = MeasurementSerializer
        def get_queryset(self):
                return super().get_queryset()

# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

