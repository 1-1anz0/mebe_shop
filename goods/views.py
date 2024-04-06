from django.shortcuts import render
from goods.models import *
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator

from goods.utils import query_search

# Create your views here.



def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)

    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)



    if category_slug == 'ahli-onumler':
        products = Products.objects.all()

    elif query:
        products = query_search(query)
        
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        products = Products.objects.filter(discount__gt=0)
    if order_by and order_by != 'default':
        products = Products.objects.order_by(order_by)


    paginator = Paginator(products, 3)
    current_page = paginator.page(int(page))

    
    context = {
        
        'products': current_page,
        'slug_url' : category_slug,
    }
    
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    products = Products.objects.get(slug=product_slug)
    context = {
        'products': products
    }
    return render(request, 'goods/product.html', context)