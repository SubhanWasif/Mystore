from django import template
from EcommerceApp.models import Product, OrderItem

register = template.Library()


@register.filter(name="product_obj")
def product_obj(value,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == int(value.id):
            product = Product.objects.get(id=id)
            quantity = cart[id]
            return product 
    return False



    
    
@register.filter(name="return_quantity")
def return_quantity(value,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == int(value.id):
            quantity = cart[id]
            return quantity 
    return False



@register.filter(name="total_price")
def total_price(value,cart):
    try:
        keys = cart.keys()
        for id in keys:
            if int(id) == int(value.id):
                quantity = cart[id]
                return int(quantity * value.price)
        return False
    except:
        return int(value)*int(cart)  

@register.filter(name="all_total")
def all_total(value,cart=None):
    try:
        keys = cart.keys()
        total=0
        for var in value:
            for id in keys:
                if int(id) == int(var.id):
                    quantity = cart[id]
                    total1 = quantity * var.price
                    total+=total1
        return total
    except:
        total = 0
        orderitem = OrderItem.objects.filter(order=value)
        for i in orderitem:
            total1 = int(i.product.price)*int(i.quantity)
            total+=total1
        return total
            
            
            
            
        
        
        
    





