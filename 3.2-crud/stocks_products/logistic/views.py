from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
import django_filters

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class StockFilter(django_filters.FilterSet):
    product_name = django_filters.CharFilter(field_name='product__name', lookup_expr='icontains')
    product_description = django_filters.CharFilter(field_name='product__description', lookup_expr='icontains')

    class Meta:
        model = Stock
        fields = []

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination  # Добавляем пагинацию

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = StockFilter  # Используем filterset_class
    search_fields = ('product__name', 'product__description')

