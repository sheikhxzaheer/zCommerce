from django.urls import path
from accounts import views

urlpatterns = [
   path('login/', views.zLogin, name='loginPage'),
   path('logout/', views.logoutPage, name='logoutPage'),

]
