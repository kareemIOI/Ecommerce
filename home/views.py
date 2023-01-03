from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def product_details(request):
    return render(request, 'product-details.html')


def checkout(request):
    return render(request, 'checkout.html')


def cart(request):
    return render(request, 'cart.html')

def login(request):
    return render(request, 'login.html')