from django.urls import path
from .views import order_list , checkout , add_to_cart
from .api import OrderListAPI,OrderDetailsAPI,ApplyCouponAPI ,CreateOrderAPI ,CartCreateUpdateDelete

urlpatterns = [
    path('',order_list),
    path('checkout/',checkout),  
    path('add-to-cart/',add_to_cart),  


#api
    path('api/<str:username>/orders',OrderListAPI.as_view()),
    path('api/<str:username>/orders',OrderDetailsAPI.as_view()),
    path('api/<str:username>/apply-coupon',ApplyCouponAPI.as_view()),
    path('api/<str:username>/cart',CreateOrderAPI.as_view()),
    path('api/<str:username>/orders/create',CartCreateUpdateDelete.as_view()),

]


