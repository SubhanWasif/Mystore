from django.db import models
from django.contrib.auth.models import User


from django.utils.text import slugify








class Customer(models.Model):
    user  = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name  = models.CharField( max_length=50,null=True)
    email = models.EmailField( max_length=254,null=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    title = models.CharField(max_length=200) 
    description=models.TextField()
    category = models.CharField( max_length=50)
    price = models.FloatField()
    Availibilty =models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, auto_now_add=False) 
    class Meta:
        verbose_name_plural = "Products"
        ordering = ("create_time",)
    def __str__(self):
        return self.title
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(self,*args, **kwargs)
    
    

    
class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,blank=True,null=True)
    transactionID = models.BigAutoField(primary_key=True,blank=True)
    def __str__(self):
        return str(self.transactionID)
    class Meta:
        ordering = ("-date_ordered",)
    


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,null=True,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.order.transactionID)

    

    
    
    
class Shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True, blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    phone_number = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=255)
    city = models.CharField( max_length=50)
    state = models.CharField( max_length=50)
    # total = models.IntegerField(default=0,blank=True,null=True)
    zipcode = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.first_name)



    class Meta:
        ordering = ("date_added", )
    
    
    
    