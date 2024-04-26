from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from .models import Products, Brand, Review, ProductsImages
from . import serializers
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 10

class ProductListAPI(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = serializers.ProductListSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'description','subtitle']
    ordering_fields = ['price']
    permission_classes = [IsAuthenticated] # any one can log in should give me token  to access the api's



class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = serializers.ProductDetailsSerializer

class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandListSerializer
    pagination_class = MyPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']




class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandDetailsSerializer
