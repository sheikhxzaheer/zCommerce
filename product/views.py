from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from cart.models import Cart
from django.http import JsonResponse
# Create your views here.
def Products(request):
    data={}
    
    if request.method == 'POST':
        searchedKeyword = request.POST.get("product-search-input")
        searchproducts = Product.objects.filter(product_title__contains=searchedKeyword)
        data = {
            "title": "Search Results",
            "searchedproducts": searchproducts,
            "searchedKeyword": searchedKeyword,
        }
        return render(request, "products.html", data)
    else:
        product_list = Product.objects.all().order_by('?')
        paginator = Paginator(product_list, 8)
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



def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(product_title__icontains=query)
    data = {
        'products': [{
            'title': p.product_title,
            'id': p.pk,
            'price': p.product_price,
            'image': p.product_image.url if p.product_image else None,
        } for p in products]
    }
    return JsonResponse(data)