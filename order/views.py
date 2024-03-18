from django.shortcuts import render,redirect
from .models import Order ,Cart ,CartDetail
from products.models import Products

def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': data})

def checkout(request):
    return render(request, 'order/checkout.html', {})
