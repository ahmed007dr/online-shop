from django.shortcuts import render,redirect
from .models import Order ,OrderDetail ,Cart ,CartDetail
from products.models import Products

def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': data})

def checkout(request):
    return render(request, 'order/checkout.html', {})



def add_to_cart(request):
    product =Products.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    print('--------------------------------------------------------------------------------------------------')
    print(quantity)
    print('--------------------------------------------------------------------------------------------------')
    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_details, created = CartDetail.objects.get_or_create(cart=cart, product=product)

    cart_details.quantity = quantity
    cart_details.total = round(product.price * cart_details.quantity,2)
    cart_details.save()

    return redirect(f'/products/{product.slug}')

