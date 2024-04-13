from rest_framework import serializers
from .models import Cart , CartDetail , Order , OrderDetail ,Coupon


class CartDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartDetail
        fields = '__all__'



class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
       
class OrderDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'



class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
       