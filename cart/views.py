from django.shortcuts import render
from .models import *
# Create your views here.
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})
