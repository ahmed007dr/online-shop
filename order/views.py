from django.shortcuts import render,redirect
from .models import Order ,OrderDetail ,Cart ,CartDetail
from products.models import Products
from settings.models import DeliveryFee

def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': data})

def checkout(request):
    cart = Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    sub_total = cart.cart_total
    discound = 0
    total = sub_total + delivery_fee
    return render(request, 'order/checkout.html', {
        'cart_detail': cart_detail, 
        'delivery_fee' : delivery_fee,
        'sub_total':sub_total,
        "discound": discound,
        'total': total
    })



def add_to_cart(request):
    product =Products.objects.get(id=request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    cart = Cart.objects.get(user=request.user, status='Inprogress')
    cart_details, created = CartDetail.objects.get_or_create(cart=cart, product=product)

    cart_details.quantity = quantity
    cart_details.total = round(product.price * cart_details.quantity,2)
    cart_details.save()

    return redirect(f'/products/{product.slug}')

