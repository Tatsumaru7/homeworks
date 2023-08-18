from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.annotate(open_count=Count('id', filter=Q(status='OPEN')))
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['created_at', 'status']
    ordering_fields = ['created_at']
    throttle_classes = [UserRateThrottle]  # Применение ограничений на частоту запросов

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []

    def perform_create(self, serializer):
        """Создание объявления с автоматическим указанием создателя."""
        serializer.save(creator=self.request.user)