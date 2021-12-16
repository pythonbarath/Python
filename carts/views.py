from django.http.response import HttpResponse
from django.shortcuts import render,redirect 
from store.models import Product
from carts.models import Cart, CartItems 
from  django.http import HttpResponse



# from carts.models import CartItems



# Create your views here.

def _cart_id(request): 
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart 


def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)

        )
    cart.save()

    try:
        cart_item = CartItems.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItems.DoesNotExist:
        cart_item = CartItems.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return HttpResponse(cart_item.product)
    exit()   
    return redirect('cart')




def cart(request):
    return render(request,'store/cart.html')