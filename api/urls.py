from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductAPI),
    path('<str:singleproduct>', SingleProductAPI),
]