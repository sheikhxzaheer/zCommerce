from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from cart.models import Cart
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
    relatedProduct = Product.objects.all()

    singleProductData ={
        "singleProduct": singleProduct,
        "relatedProduct": relatedProduct
    }
    return render(request, "product-details.html", singleProductData)


def add_to_cart(request, product_id):
    product = Product.objects.get(product_id=product_id)
    cart, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
    )
    if not created:
        cart.quantity += 1
        cart.save()
    return redirect('/cart/')
