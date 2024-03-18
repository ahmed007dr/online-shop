from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
import datetime
from django.utils import timezone
from products.models import Products  # Assuming the model is named Product, not Products
from accounts.models import Address

ORDER_STATUS = (
    ('Received', 'Received'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered')
)

class Order(models.Model):
    user = models.ForeignKey(User, related_name="order_owner", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=ORDER_STATUS, max_length=150)
    code = models.CharField(default=generate_code, max_length=8)
    order_time = models.DateTimeField(default=timezone.now)  
    delivery_time = models.DateTimeField(null=True, blank=True)
    delivery_address = models.ForeignKey(Address, related_name='delivery_address', on_delete=models.SET_NULL, null=True, blank=True)
    coupon = models.ForeignKey('Coupon', related_name='order_coupon', null=True, blank=True, on_delete=models.SET_NULL)  # Added related_name
    total = models.FloatField()
    total_with_coupon = models.FloatField(null=True, blank=True)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name="order_details", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='orderdetails_product', on_delete=models.SET_NULL, null=True, blank=True)  # Assuming Product model
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()

CART_STATUS = (
    ('Inprogress', 'Inprogress'),
    ('Completed', 'Completed')
)

class Cart(models.Model):
    user = models.ForeignKey(User, related_name="cart_owner", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=CART_STATUS, max_length=150)
    coupon = models.ForeignKey('Coupon', related_name='cart_coupon', null=True, blank=True, on_delete=models.SET_NULL)  # Added related_name
    total_with_coupon = models.FloatField(null=True, blank=True)

    @property
    def cart_total(self):
        total = 0
        for item in self.cart_details.all():
            if item.total is not None:  # Check if item.total is not None
                total += item.total
        return round(total, 2)



class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_details", on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='cartdetails_product', on_delete=models.SET_NULL, null=True, blank=True)  # Assuming Product model
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True,blank=True) 


class Coupon(models.Model):
    code = models.CharField(max_length=20)  
    start_date = models.DateField(default=timezone.now)  
    end_date = models.DateField()
    quantity = models.IntegerField()
    discount = models.FloatField()

    def save(self, *args, **kwargs):
        week = datetime.timedelta(days=7)

        self.end_date = self.start_date + week
        super(Coupon, self).save(*args, **kwargs)
