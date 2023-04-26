from django.shortcuts import render
from .models import *
# Create your views here.
def Products(request):
    product_list = Product.objects.all()
    productData = {
       "product_list": product_list,
    }
    return render(request, "products.html", productData)
