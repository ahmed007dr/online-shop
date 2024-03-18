from django.shortcuts import render,redirect
from .models import Order ,Cart ,CartDetail
from products.models import Products

def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': data})

def checkout(request):
    return render(request, 'orders/checkout.html', {})


def add_to_cart(request):
    product_id = request.POST['product_id']
    quantity = int(request.POST['quantity'])

    # Use a different name for the variable representing the model
    product_instance = Products.objects.get(id=product_id)

    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_details, created = CartDetail.objects.get_or_create(cart=cart, product=product_instance)
    return redirect (f'/products/{product_instance.slug}')
