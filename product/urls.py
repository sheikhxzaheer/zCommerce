from django.urls import path
from product import views

urlpatterns = [
    path('', views.Products, name='Product'),
    path('<product_id>', views.productDetails, name='productDetails'),
]
