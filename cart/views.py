from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
# Create your views here.
def cart(request):
    subtotal = 0 
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        item.total_price = item.product.product_price * item.quantity
        subtotal += item.total_price
    return render(request, 'cart.html', {'cart_items': cart_items, "subtotal": subtotal,})

def addToCart(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart_items = Cart.objects.filter(user=request.user)
    product = cart.product
    cart.quantity += 1
    cart.save()
    subtotal = 0 
    for item in cart_items:
        item.total_price = item.product.product_price * item.quantity
        subtotal += item.total_price
    cartData = {
        "cart": cart.quantity,
        "subtotal": subtotal,
        'product': {
            'price': product.product_price,
        }
    }
    return JsonResponse(cartData)

def minusFromCart(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart_items = Cart.objects.filter(user=request.user)
    product = cart.product
    cart.quantity -= 1
    cart.save()
    subtotal = 0 
    for item in cart_items:
        item.total_price = item.product.product_price * item.quantity
        subtotal += item.total_price
    cartData = {
        "cart": cart.quantity,
        "subtotal": subtotal,
        'product': {
            'price': product.product_price,
        }
    }
    return JsonResponse(cartData)