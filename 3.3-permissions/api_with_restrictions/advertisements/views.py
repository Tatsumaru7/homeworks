from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from .serializers import AdvertisementSerializer
from rest_framework.throttling import UserRateThrottle
from .filters import AdvertisementFilter
from .permissions import IsAdvertisementOwnerPermission

class CustomUserThrottle(UserRateThrottle):
    rate = "10/day"  

class IsAdvertisementOwnerPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.annotate(open_count=Count('id', filter=Q(status='OPEN')))
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = AdvertisementFilter
    filterset_fields = ['created_at', 'status']
    ordering_fields = ['created_at']
    throttle_classes = [UserRateThrottle]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdvertisementOwnerPermission()]
        return []

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


