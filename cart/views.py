from django.shortcuts import render
from django.conf import settings 
from django.contrib.auth.decorators import login_required 
from .cart import Cart 
from item.models  import Item 
# Create your views here.
def add_to_cart(request, item_id):
    cart = Cart(request)
    cart.add(item_id)
    return render(request, 'cart/menu_cart.html')



def cart(request):
    return render(request, 'cart/cart.html')

def update_cart(request, item_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(item_id, +1, True)
    else:
        cart.add(item_id, -1, True)
    
    items = Item.objects.get(pk=item_id)
    quantity = cart.get_item(item_id)
    if quantity:
        quantity = quantity['quantity']

        item = {
            'item':{
                'id': items.id,
                'name': items.name,
                'image': items.image, 
                'price': items.price,

            },
            'total_price': (quantity * items.price) /100, 
            'quantity' : quantity,
        }

    else:
        item = None 

        response = render(request, 'cart/partials/cart_item.html', {'item': item})
        response['HX-Trigger'] = 'update-menu-cart'
        return response
    
def checkout(request):
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE 
    
    return render(request, 'cart/checkout.html', {'pub_key':pub_key})


def hx_menu_cart(request):
    return render(request, 'cart/menu_cart.html')

def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')