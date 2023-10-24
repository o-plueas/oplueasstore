from django.shortcuts import render, redirect 
from .forms import SignupForm 
from item.models import Item, Category
from .models import Cart
from django.http import JsonResponse

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold = False)
    categories =Category.objects.all()
    

    return render(request, 'core/index.html', {
        'items':items,
        'categories':categories
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form' : form
    })


def cart(request):
    user = Cart.objects.get(user = request.user)

    return render(request, 'cart.html', {'user':user})

def add_to_cart(request, item_id):
    print(item_id)
    item = Item.objects.get(id = item_id )
    print(item)
    
    cart= Cart.objects.filter(user =request.user)
    if cart.exists():
        usercart= Cart.objects.get(user =request.user)
        usercart.add(item)
        usercart.save()
    else:
        cart_creation= Cart.objects.create(user =request.user, item= item)
        cart_creation.save()

        
    user.add(item)


    # user = User.objects.create(name ='xxx', email ='email@gmail')

    # obj, created = Book.objects.get_or_create(name='two scoope', author='Daniel roy')


    return JsonResponse('success', safe=False)


