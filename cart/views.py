from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse
# Create your views here.
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        item.total_price = item.product.product_price * item.quantity
    return render(request, 'cart.html', {'cart_items': cart_items})

def addToCart(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart.quantity += 1
    cart.save()
    return JsonResponse({"cart": cart.quantity})

def minusFromCart(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id)
    cart.quantity -= 1
    cart.save()
    return JsonResponse({"cart": cart.quantity})