from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('addcart/<int:cart_id>/', views.addCart, name='addCart'),

]
