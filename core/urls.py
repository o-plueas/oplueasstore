from django.urls import path 

from .views import signup, index, add_to_cart
from django.contrib.auth import views as auth_views 
from django.contrib.auth import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', index, name = 'index'),
    path('signup/', signup, name = 'signup'), 
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name='logout')

]