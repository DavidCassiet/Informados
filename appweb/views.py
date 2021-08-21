from django.http import request
from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages

class inicio(HttpRequest):
    def index(request):
        return render(request,"index.html")

class inicioUs(HttpRequest):
    def index(request):
        return render(request,"inicioUs.html")

def login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            messages.success(request,f"Usuario {username} creado")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "register.html", context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data["username"]
            messages.success(request,f"Usuario {username} creado")
            return redirect("index")
    else:
        form = UserRegisterForm()
    context = {"form": form}
    return render(request, "register.html", context)