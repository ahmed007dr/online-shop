from django.urls import path
from .views import ProductDetails, ProductList, BrandDetail, BrandList  , add_review

urlpatterns = [
    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>', BrandDetail.as_view()),
    
    path('', ProductList.as_view()),
    path('<slug:slug>', ProductDetails.as_view()),

    path('<slug:slug>/add-review', add_review),
]
