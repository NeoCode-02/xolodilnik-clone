from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("blog_single", views.blog_single, name="blog_single"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("contact", views.contact, name="contact"),
    path("shop", views.shop, name="shop"),
    path("single_product", views.single_product, name="single_product"),
    path("wishlist", views.wishlist, name="wishlist"),
]
