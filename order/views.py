from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
import datetime
from .models import Order ,OrderDetail ,Cart ,CartDetail ,Coupon
from products.models import Products
from settings.models import DeliveryFee

def order_list(request):
    data = Order.objects.filter(user=request.user)
    return render(request, 'order/order_list.html', {'orders': data})

def checkout(request):
    cart = Cart.objects.get(user=request.user,status='Inprogress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee

    if request.method == 'POST':
        code = request.POST['coupon_code']
        #coupon = Coupon.objects.get(code=code)
        coupon = get_object_or_404(Coupon,code=code)
        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = round(cart.cart_total / 100  * coupon.discount,2)
                sub_total = cart.cart_total - coupon_value
                total = sub_total + delivery_fee
                cart.coupon = coupon
                cart.total_with_coupon = round(sub_total,2)
                cart.save()
                return render(request, 'order/checkout.html', {
                'cart_detail': cart_detail, 
                'delivery_fee' : delivery_fee,
                'sub_total':sub_total,
                "discound": coupon_value,
                'total': total
                                })

 

    sub_total = round(cart.cart_total,2)
    discound = 0
    total = round(sub_total + delivery_fee,2)
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

