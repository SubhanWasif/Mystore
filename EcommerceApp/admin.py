from django.contrib import admin

# Register your models here.

from .models import Product, Order,OrderItem, Customer,Shipping


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)



