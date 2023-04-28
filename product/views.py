from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def Products(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 3)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    productData = {
       "products": products,
    }
    return render(request, "products.html", productData)

def productDetails(request, product_id):
    singleProduct = Product.objects.get(product_id=product_id)
    singleProductData ={
        "singleProduct": singleProduct,
    }
    return render(request, "product-details.html", singleProductData)
