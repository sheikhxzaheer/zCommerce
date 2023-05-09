from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.
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