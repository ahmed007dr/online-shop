from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Products , Brand , Review ,ProductsImages
# Create your views here.

class ProductList(ListView):
    model = Products
    paginate_by = 100 # 3lashn listView support Paginate_by
    

class ProductDetails(DetailView):
    model = Products

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] = ProductsImages.objects.filter(product=self.get_object())
        context['related'] = Products.objects.filter(brand=self.get_object().brand)

        return context
    

 #context {'': } queryset : Product.objects.all()
 #queryset : main query : detail product  | 
 #context : extra data : review & image (extra) becouse we get new data from new table class

class BrandList(ListView):
    model = Brand
    paginate_by = 20 # 3lashn listView support Paginate_by cbv

# class BrandDetail(DetailView):
#     model = Brand
#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context["products"] = Products.objects.filter(brand=self.get_object())
#         return context
    
    
    #to handel pagnation from genric listview
class BrandDetail(ListView):
    model = Products
    paginate_by = 100 # 3lashn listView support Paginate_by cbv
    template_name = "products/brand_detail.html"

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
