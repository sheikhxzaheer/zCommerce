from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls import reverse_lazy
# Create your views here.


def signUp(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        user = User.objects.create_user(
            username=username, first_name=first_name, email=email)
        user.set_password(password)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        return redirect('/')
    else:
        data={
            "title": "Register",
        }
        return render(request, "signup.html", data)



def zLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists(): 
            return redirect('loginPage')
        user_obj = authenticate(username=username, password=password)
        if user_obj:
            auth_login(request, user_obj)
            return redirect('/')
        return redirect('loginPage')
    data = {
        "title": "Log In"
    }
    return render(request, "login.html", data)



def logoutPage(request):
    logout(request)
    return redirect("loginPage")