from django.db import models
from item.models import Item
from django.contrib.auth.models import User 

# Create your models here.
class Cart(models.Model):
    item = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    

