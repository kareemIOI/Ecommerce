from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('productDetails', views.product_details, name='productDetails'),
    path('checkout', views.checkout, name = 'checkout'),
    path('cart', views.cart, name = 'cart'),
    path('login', views.login, name = 'login'),
    path('account', views.account, name = 'account'),
    path('wishlist', views.wishlist, name = 'wishlist'),
    path('checkout', views.checkout, name = 'checkout'),
    path('bloglist', views.bloglist, name = 'bloglist'),
    path('blogsingle', views.blogsingle, name = 'blogsingle'),
    path('404', views.error_404, name = '404'),
    path('contact', views.contact, name = 'contact'),
    path('products', views.products, name = 'products'),
]	