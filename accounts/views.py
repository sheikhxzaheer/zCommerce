from django.shortcuts import render

# Create your views here.
def zLogin(request):
    return render(request, "login.html")