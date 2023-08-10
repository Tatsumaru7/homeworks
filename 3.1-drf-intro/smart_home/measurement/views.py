from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer
from .models import Sensor, Measurement
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementView(RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class CreateMeasurementView(CreateAPIView):
    def post(self, request, format=None):
        print(request.data)  # Вывод данных из запроса для отладки
        data = request.data.copy()
        sensor_id = data.pop('sensor')
        sensor = Sensor.objects.get(pk=sensor_id)
        serializer = MeasurementSerializer(data=data)
        if serializer.is_valid():
            serializer.save(sensor=sensor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related('measurements')  # Важно добавить эту строку

