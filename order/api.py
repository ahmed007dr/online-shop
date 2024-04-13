from rest_framework import generics #CBV
from django.contrib.auth.models import User
from rest_framework.response import responses
from rest_framework.generics import ListAPIView ,RetrieveAPIView ,GenericAPIView
from django.shortcuts import get_list_or_404
from .serializers import CartDetailSerializers , CartSerializers ,OrderDetailSerializers ,OrderSerializers
from .models import Order , OrderDetail , Cart , CartDetail , Coupon
from products.models import Products # from anther app
from settings.models import DeliveryFee # from anther app
import datetime

class OrderListAPI(ListAPIView):
    serializer_class = OrderSerializers
    queryset = Order.objects.all()

    def get_queryset(self): # override queryset
        queryset = super(OrderListAPI, self).get_queryset() #الكويري اللي كان بيتنفذ

        user = User.objects.get(username=self.kwargs['username']) # جيبت اليوزر 

        queryset = queryset.filter(user=user) # فلترت الكويري دا
        return queryset # رجعت بيه


    # # plan B
    # def list(self,request,*args,**kwargs): # 39 number 
    #     queryset = super(OrderListAPI, self).get_queryset() #الكويري اللي كان بيتنفذ

    #     user = User.objects.get(username=self.kwargs['username']) # url جيبت اليوزر 

    #     queryset = queryset.filter(user=user) # فلترت الكويري دا
    #     data = OrderSerializers(queryset,many=True).data # +
    #     return responses({'order':data}) # رجعت بيه  # +

class OrderDetailsAPI(RetrieveAPIView):
    serializer_class = OrderDetailSerializers
    queryset = OrderDetail.objects.all()


class ApplyCouponAPI(GenericAPIView):
    def post(self,request,*args,**kwargs):
        user = User.objects.get(username=self.kwargs['username'])# from URL 
        coupon = get_list_or_404(Coupon , code = request.data['coupon_code']) # rquest body # fyas
        delivery_fee = DeliveryFee.objects.last().fee
        cart = Cart.objects.get(user=request.user,status='Inprogress')

        #copy from view
        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                coupon_value = round(cart.cart_total / 100  * coupon.discount,2)
                sub_total = cart.cart_total - coupon_value
                #total = sub_total + delivery_fee
                cart.coupon = coupon
                cart.total_with_coupon = round(sub_total,2)
                cart.save()
                return responses({'messge':' coupon was applied successfuly'})
            else:
                return responses({'invald':' invald coupon'})
        return responses ({'messge':'not found'})


