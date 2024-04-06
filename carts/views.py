from django.http import JsonResponse
from django.shortcuts import redirect, render
from carts.models import Carts
from django.template.loader import render_to_string
from carts.utils import get_user_cart

from goods.models import Products

# Create your views here.


def cart_add(request):
    product_id = request.GET.get('product_id')
    product = Products.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        carts = Carts.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Carts.objects.create(user=request.user, product=product, quantity=1)
    
    else:
        carts = Carts.objects.filter(session_key=request.session.session_key, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity +=1
                cart.save()
        else:
            Carts.objects.create(session_key=request.session.session_key, product=product, quantity=1)


    user_cart = get_user_cart(request)

    cart_items_html = render_to_string('carts/includes/included_cart.html', {'carts': user_cart}, request=request)

    response_data = {
        'message': 'Onum Sebede Gosuldy',
        'cart_items_html': cart_items_html
    }

    return JsonResponse(response_data)

def cart_change(request): 
    cart_id = request.POST.get('cart_id')
    quantity = request.POST.get('quantity')

    cart = Carts.objects.get(id=cart_id)
    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity
    cart_items_html = render_to_string(
        'carts/includes/included_cart.html', {'carts': cart}, request=request
    )
    response_data = {
        'message': 'Onum uytgedildi',
        'cart_items_html':cart_items_html,
        'quantity': updated_quantity
    }
    return JsonResponse(response_data)

def cart_remove(request):
    cart_id = request.POST.get('cart_id')
    cart = Carts.objects.get(id=cart_id)
    quantity = cart.quantity
    cart.delete()
    user_cart = get_user_cart(request)
    cart_items_html = render_to_string('carts/includes/included_cart.html', {'carts': user_cart}, request=request)
    responde_data = {
        'message' : 'Onum ayryldy',
        'cart_items_html' : cart_items_html,
        'quantity_deleted': quantity
    }
    return JsonResponse(responde_data)