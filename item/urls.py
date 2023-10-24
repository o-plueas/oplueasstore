from django.urls import path 
from .views import new, detail, items, edit, delete

app_name = 'item'

urlpatterns = [
    path('new/', new, name = 'new'),
    path('<int:pk>/edit', edit, name = 'edit'),
    path('', items, name = 'items'),
    path('<int:pk>/', detail, name = 'detail'),
    path('<int:pk>/delete', delete, name='delete')
    


]