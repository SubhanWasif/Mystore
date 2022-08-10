


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Shipping

from django.forms import ModelForm




class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password confirm'}))


    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username','class': 'input'}),
            'email': forms.TextInput(attrs={'placeholder': 'email','class': 'input'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password','class': 'input'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'input'}),
            
        }




class ShippingForm(forms.ModelForm):
    
    
    
    class Meta:
        model = Shipping
        fields = ['first_name','last_name','phone_number','address','city','zipcode','state']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name','class': 'input'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name','class': 'input'}),
            'phone_number': forms.NumberInput(attrs={'placeholder': 'Phone Number','class': 'input'}),
            'city': forms.TextInput(attrs={'placeholder': 'City','class': 'input'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address','class': 'input'}),
            'zipcode': forms.NumberInput(attrs={'placeholder': 'Zipcode','class': 'input'}),
            'state': forms.TextInput(attrs={'placeholder': 'State','class': 'input'})
        }