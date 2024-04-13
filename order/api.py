from rest_framework import generics #CBV
from django.contrib.auth.models import User
from rest_framework.response import responses
from rest_framework.generics import ListAPIView ,RetrieveAPIView

from .serializers import CartDetailSerializers , CartSerializers ,OrderDetailSerializers ,OrderSerializers
from .models import Order , OrderDetail , Cart , CartDetail , Coupon
from products.models import Products # from anther app
from settings.models import DeliveryFee # from anther app

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

    #     user = User.objects.get(username=self.kwargs['username']) # جيبت اليوزر 

    #     queryset = queryset.filter(user=user) # فلترت الكويري دا
    #     data = OrderSerializers(queryset,many=True).data # +
    #     return responses({'order':data}) # رجعت بيه  # +

class OrderDetailsAPI(RetrieveAPIView):
    serializer_class = OrderDetailSerializers
    queryset = OrderDetail.objects.all()
