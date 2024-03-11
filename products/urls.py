from django.urls import path
from .views import ProductDetails,ProductList,BrandDetail,BrandList

urlpatterns = [
    path('brands/',BrandList.as_view()),
    path('brands/<slug:slug>',BrandDetail.as_view()),
    #products are accessible through the brand they belong to or directly by their slug
    path('',ProductList.as_view()),
    path('<slug:slug>',ProductDetails.as_view()),

]
