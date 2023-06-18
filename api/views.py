from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer
from product.models import Product

# Create your views here.
@api_view(['GET'])
def ProductAPI(request):
    apiProduct = Product.objects.all()
    serializer = ProductSerializer(apiProduct, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def SingleProductAPI(request, singleproduct):
    apiProduct = Product.objects.get(product_id=singleproduct)
    serializer = ProductSerializer(apiProduct)
    return Response(serializer.data)