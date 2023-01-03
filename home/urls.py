from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('productDetails', views.product_details, name = 'productDetails'),
    path('checkout', views.checkout, name = 'checkout'),
    path('cart', views.cart, name = 'cart'),
    path('login', views.login, name = 'login'),

]	