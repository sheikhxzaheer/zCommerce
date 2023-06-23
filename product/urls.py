from django.urls import path
from product import views

urlpatterns = [
    path('', views.Products, name='Product'),
    path('product-details/<product_id>', views.productDetails, name='productDetails'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('searchproducts/', views.search_products, name='searchproducts'),
]
