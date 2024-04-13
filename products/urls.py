from django.urls import path
from .views import ProductDetails, ProductList, BrandDetail, BrandList  , add_review

from . import api


urlpatterns = [
    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>', BrandDetail.as_view()),
    
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetails.as_view()),

    path('<slug:slug>/add-review', add_review),

    #API
    path('api/list',api.ProductListAPI.as_view()),
    path('api/list/<int:pk>',api.ProductDetailAPI.as_view()),

    path('api/brands',api.BrandListAPI.as_view()),
    path('api/brands/<int:pk>',api.BrandDetailAPI.as_view()),

]
