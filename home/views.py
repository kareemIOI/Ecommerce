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


def account(request):
    return render(request, 'account.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def checkout(request):
    return render(request, 'checkout.html')


def bloglist(request):
    return render(request, 'bloglist.html')


def blogsingle(request):
    return render(request, 'blogsingle.html')



def error_404(request):
    return render(request, '404.html')


def contact(request):
    return render(request, 'contact-us.html')



def products(request):
    return render(request, 'products.html')