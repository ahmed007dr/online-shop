from rest_framework import generics
from .models import Products, Brand, Review, ProductsImages
from . import serializers
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 10

class ProductListAPI(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = serializers.ProductListSerializer

class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = serializers.ProductDetailsSerializer

class BrandListAPI(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandListSerializer
    pagination_class = MyPagination

class BrandDetailAPI(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = serializers.BrandDetailsSerializer
