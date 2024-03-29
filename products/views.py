from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render ,redirect
from django.views.generic import ListView,DetailView
from .models import Products , Brand , Review ,ProductsImages
from django.db.models.aggregates import Count # create hidden column in database give me new value

class ProductList(ListView):
    model = Products
    paginate_by = 20 # 3lashn listView support Paginate_by
    

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
    queryset = Brand.objects.annotate(product_count=Count('Products_brand')) #كدا انا هجيب عدد البرندات من حدول العلاقات

# class BrandDetail(DetailView):
#     model = Brand
#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context["products"] = Products.objects.filter(brand=self.get_object())
#         return context
    
    
    #to handel pagnation from genric listview
class BrandDetail(ListView):
    model = Products
    paginate_by = 20 # 3lashn listView support Paginate_by cbv
    template_name = "products/brand_detail.html"

    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('Products_brand'))[0] #كدا انا هجيب عدد البرندات من حدول العلاقات
        return context


def add_review(request,slug):
    product=Products.objects.get(slug=slug)
    review=request.POST['review'] #request.POST.get(review) # request.GET['review] # request.GET.get['review]
    rate=request.POST['rating']
#add review
    Review.objects.create(
        user=request.user,
        product=product,
        review=review,
        rate=rate
    )
    #get all reviews for this products
    review =Review.objects.filter(product=product)
    return redirect(f'/products/{slug}')