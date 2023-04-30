from django.shortcuts import render
from .models import *
# Create your views here.
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
        item.total_price = item.product.product_price * item.quantity
    return render(request, 'cart.html', {'cart_items': cart_items})
