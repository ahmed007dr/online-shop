from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Products , Brand , Review
# Create your views here.

class ProductList(ListView):
    model = Products
    

class ProductDetails(DetailView):
    model = Products

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context
    


 #context {'': } queryset : Product.objects.all()
 #queryset : main query : detail product  | 
 #context : extra data : review & image (extra) becouse we get new data from new table class
