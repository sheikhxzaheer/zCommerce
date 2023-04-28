from django.urls import path
from product import views

urlpatterns = [
    path('', views.Products),
    path('<product_id>', views.productDetails, name='productDetails'),
]
