from django.shortcuts import render
from products.models import Products,Brand,Review
from django.db.models.aggregates import Count # create hidden column in database give me new value



def home(request):

    new_products = Products.objects.filter(flag='New')[:10]
    sale_products = Products.objects.filter(flag='Sale')[:10]
    feature_products = Products.objects.filter(flag='Feature')[:10]
    brand = Brand.objects.annotate(product_count=Count('Products_brand')) [:10] #كدا انا هجيب عدد البرندات من حدول العلاقات
    reviews = Review.objects.all()

    return render(request,'settings/home.html',{
        'new_products':new_products,
        'sale_products':sale_products,
        'feature_products':feature_products,
        'brand':brand,
        'reviews':reviews
    })