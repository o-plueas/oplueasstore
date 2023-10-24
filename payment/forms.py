from django import forms
from .models import Payment


class PaymentInitForm(forms.ModelForm):
    class Meta:
        model = Payment
        # model fields to include when creating form object
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'zipcode', 'amount' ,'city']
        
        first_name  =  forms.CharField(widget = forms.TextInput(attrs={
            'placeholder' : 'Your first name', 
            'class' : 'w-full py-4 px-6 rounded-xl'        
            }))
        last_name  =  forms.CharField(widget = forms.TextInput(attrs={
            'placeholder' : 'Your last name', 
            'class' : 'w-full py-4 px-6 rounded-xl'        
            }))

        email = forms.CharField(widget =forms.TextInput(attrs ={
            'placeholder': 'Your email', 
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
        

        phone = forms.CharField(widget =forms.TextInput(attrs ={
            'placeholder': 'Your email', 
            'class': 'w-full py-4 px-6 rounded-xl' 
            
        }))

        address = forms.CharField(widget =forms.TextInput(attrs ={
            'placeholder': 'Your adress', 
            'class': 'w-full py-4 px-6 rounded-xl'
        }))

        zipcode = forms.CharField(widget =forms.TextInput(attrs ={
        'placeholder': 'Your zipcode', 
        'class': 'w-full py-4 px-6 rounded-xl'
        }))

        amount = forms.CharField(widget =forms.TextInput(attrs ={
        'placeholder': 'Your amount', 
        'class': 'w-full py-4 px-6 rounded-xl'
        }))

