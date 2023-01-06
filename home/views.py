from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import Register
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
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        user = auth.authenticate(first_name = first_name, email = email)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(first_name= first_name).exists():
                messages.info(request, 'User already registered')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name = first_name,username = username,email = email, password = password1)
                user.save();
                print("user created")
                return redirect('/')
        else:
            messages.info(request, 'password not matching...')
            return redirect('login')
        # return redirect('/')
    else:
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
    return render(request, 'blog-single.html')



def error_404(request):
    return render(request, '404.html')


def contact(request):
    return render(request, 'contact-us.html')



def products(request):
    return render(request, 'products.html')