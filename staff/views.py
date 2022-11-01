from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from home import urls
from django.contrib.auth.models import User

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print("credentials are incorrect.")
            return redirect("signup_page")
        # print(username,password)
    return render(request, 'login_page.html')

def signup_page(request):  
    return render(request, "signup_page.html")

def logout_page(request):
    print("logout")
    logout(request)
    return redirect("home")