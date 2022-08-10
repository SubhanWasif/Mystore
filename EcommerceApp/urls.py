from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('cart', views.cart,name="cart"),
    path('orders', views.Orders,name="orders"),
    path('signup', views.signuppage,name="signup"),
    path('login', views.loginpage,name="login"),
    path('checkout', views.shipping,name="checkout"),
    path('orderplaced', views.OrderedPlace,name="orderplaced"),
    path('order_details/<int:pk>', views.order_details,name="order_details"),
    path('logout', views.logoutpage,name="logout"),   
    
]