from django.shortcuts import render
from .models import Order

def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': data})

def checkout(request):
    return render(request, 'order/checkout.html', {})
