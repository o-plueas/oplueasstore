from django.shortcuts import render, redirect, get_object_or_404 
from .forms import NewItemForm, EditItemForm
from .models import Category, Item
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()

    items = Item.objects.filter(is_sold = False)

    if category_id:
        items = items.filter(category_id = category_id)

    if query:
        query = items.filter(Q(name__icontains=query) | Q(description__icontains=query))




    return render(request, 'item/items.html', {
        'items':items,
        'query':query,
        'category_id': int(category_id),
        'categories' : categories
    })



def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_item = Category.objects.filter(name =item.category).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_item': related_item

    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit =  False)
            item.created_by = request.user 
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form' : form, 
        'title' : 'New Item'

    })


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk = pk, created_by = request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance = item)
        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance =item)
        
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item'

    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk =pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')