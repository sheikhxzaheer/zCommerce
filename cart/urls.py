from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('addcart/<int:cart_id>/', views.addToCart, name='addCart'),
    path('minuscart/<int:cart_id>/', views.minusFromCart, name='minusCart'),

]
