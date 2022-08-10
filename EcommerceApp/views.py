from django.shortcuts import redirect, render
from .models import Product, Order,OrderItem, Customer, Shipping
from .forms import UserForm,ShippingForm
from django.contrib import messages
from django.db.models import F
from django.contrib.auth import authenticate, login,logout






def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, "Username OR Password is incorrect!")
            return redirect('login')
    else:
        return render(request, "HTML/login.html", context={})
            


def signuppage(request):
    form  = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)  
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            customer = Customer.objects.create(user=user,name=username,email=email)
            messages.success(request, "Account has been made successfully ")
            return redirect('login')
    context = {'form':form}
    return render(request, "HTML/signpage.html", context)


def logoutpage(request):
    logout(request)
    return redirect('index')
    


def index(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                customer = request.user.customer
                order ,created = Order.objects.get_or_create(customer=customer,complete=False)
                id = request.POST.get('id')    
                product = Product.objects.get(id=id)
                if OrderItem.objects.filter(product=product,order=order):
                        orderitem = OrderItem.objects.filter(product=product).update(quantity=F('quantity')+1)  
                else:
                    orderitem = OrderItem.objects.create(product=product,order=order,quantity=1)

                return redirect('index')
            except:
                category = request.POST.get('submit')
                
                if category =="All Products":
                    return redirect('index')
                products = Product.objects.filter(category=category)
                return render(request, "HTML/index.html",{'products':products})
            
        else:
            id = request.POST.get('id')    
            obj_id = Product.objects.get(id=id)
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(id)
                if quantity:
                    cart[id]= quantity+1
                else: 
                    cart[id] = 1
            else:
                cart={}
                cart[id] = 1
            request.session['cart'] = cart
            return redirect('index')

            
    else:
        if request.user.is_authenticated:
            customer = request.user.customer
            order ,created = Order.objects.get_or_create(customer=customer,complete=False)
            cart = request.session.get('cart')
            if cart:
                keys = cart.keys()
                for id in keys: 
                    product = Product.objects.get(id=id)
                    orderitem = OrderItem.objects.filter(product=product,order=order)
                    if orderitem:
                        orderitem = OrderItem.objects.filter(product=product,order=order).update(quantity=cart[id])  
                    else:
                        orderitem = OrderItem.objects.create(product=product,order=order,quantity=cart[id])
                del request.session['cart']
        products = Product.objects.all()
        return render(request, "HTML/index.html",{'products':products})



def cart(request):  
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('submit') 
            id = request.POST.get('id')
            orderitem = OrderItem.objects.get(id=id)
            if name == "⇓":
                if orderitem.quantity>0:
                    orderitem.quantity=F('quantity')-1
                    orderitem.save()
                else:   
                    orderitem.delete()
            elif name == "⇑":
                orderitem.quantity=F('quantity')+1
                orderitem.save()
            return redirect('cart')
        else:
            customer = request.user.customer
            order ,created = Order.objects.get_or_create(customer=customer,complete=False)
            items = OrderItem.objects.filter(order=order)
            total =0
            for item in items:
                tol = int(item.product.price)*int(item.quantity)
                total+=tol
            return render(request, 'HTML/cart.html',{'order':order,'items':items,'total':total})
    else:
        if request.method == "POST":
            name = request.POST.get('submit') 
            item_id = request.POST.get('id')
            cart = request.session.get('cart')
            keys = cart.keys()
            for id in keys:
                if int(id) == int(item_id):
                    quantity = cart[id]
                    if name == "⇓":
                        if quantity>0:       
                            quantity-=1
                            cart[id] = quantity
                        else:   
                            del cart[id]    
                        break
                    elif name == "⇑":
                        quantity+=1
                        cart[id] = quantity
                        break
            if cart == {}:
                del request.session['cart']                 
            else: 
                request.session['cart'] = cart
                
            return redirect('cart')
        else:
            cart = request.session.get('cart')
            if cart:
                items = Product.objects.all()
                return render(request, 'HTML/cart.html',{'items':items})
            else:
                return render(request, 'HTML/cart.html')



def Orders(request):
    customer = request.user.customer
    order = Order.objects.filter(customer=customer,complete=True)
    return render(request, 'HTML/MyOrder.html',{'orders':order})




def order_details(request,pk):
    order = Order.objects.get(transactionID=pk)
    orderitem = OrderItem.objects.filter(order=order)
    return render(request, 'HTML/order_details.html',{'orderitem':orderitem,'order':order,'pk':pk})

        

def shipping(request):  
    form = ShippingForm()
    customer =  request.user.customer
    order = Order.objects.get(customer=customer,complete=False)   
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state =request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        if form.is_valid():
            form.save()
        order.complete = True
        order.save()
        return redirect("orderplaced")
    
    return render(request,'HTML/shipping.html',{'form':form,'order':order})
    
    
    
    
def OrderedPlace(request):
    return render(request,'HTML/orderplaced.html')            
    


