from django.shortcuts import render,redirect
from .models import Order ,Cart ,CartDetail
from products.models import Products

def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': data})

def checkout(request):
    return render(request, 'order/checkout.html', {})



def add_to_cart(request):
    product_id = request.POST['product_id']
    quantity = int(request.POST['quantity'])

    product_instance = Products.objects.get(id=product_id)

    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_details, created = CartDetail.objects.get_or_create(cart=cart, product=product_instance)

    cart_details.quantity = quantity
    cart_details.total = round(product_instance.price * cart_details.quantity,2)
    

    return redirect(f'/products/{product_instance.slug}')