from django.urls import path 
from cart.views import add_to_cart, cart, update_cart, hx_menu_cart, hx_cart_total, checkout

urlpatterns = [
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('', cart, name='cart'),
    path('update_cart/<int:item_id>/<str:action>/', update_cart, name='update_cart'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total/', hx_cart_total, name='hx_cart_total'),
    path('checkout/', checkout, name='checkout'),


]   