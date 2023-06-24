from django.shortcuts import render, HttpResponse
from product.models import Product

# Create your views here.
def Home(request):
    homeProduct = Product.objects.all()
    return render(request, "index.html", {'homeProduct': homeProduct})

