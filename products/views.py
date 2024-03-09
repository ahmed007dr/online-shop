from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Products , Brand , Review
# Create your views here.

class ProductList(ListView):
    model = Products

class ProductDetails(DetailView):
    model = Products
