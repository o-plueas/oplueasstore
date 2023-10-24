from django.conf import settings 
from item.models import Item 

class Cart(object):
    def __init__(self, request):
        self.session = request.session 
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart 

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['items'] = Item.objects.get(pk=p)
        
        for item in self.cart.values():
            item['total_price'] = int(item['items'].price * item['quantity']) / 100

            yield item 
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart 
        self.session.modified = True
    
    def add(self, item_id, quantity=1, update_quantity=False):
        item_id = str(item_id)

        if item_id not in self.cart:
            self.cart[item_id] = {'quantity' :  1, 'id': 'item_id'}


        if update_quantity:
            self.cart[item_id]['quantity'] += int(quantity)
            if self.cart[item_id]['quantity'] == 0:
                self.remove(item_id)
        self.save()


    def remove(self, item_id):
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified - True 

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['items'] = Item.objects.get(pk=p)


        return int(sum(item['items'].price * item['quantity'] for item in self.cart.values())) / 100
    
    def get_item(self, item_id):
        if str(item_id) in self.cart:
            return self.cart[str(item_id)]
        else:
            return None





            