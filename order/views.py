from django.shortcuts import render

from .models import Order

def order_list(request):
    data = Order.objects.all()
