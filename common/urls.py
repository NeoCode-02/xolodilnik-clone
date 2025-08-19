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
    #------- Sponsor APIlari
    path("sponsors", views.SponsorListAPIView.as_view(), name="sponsors"),
    path("sponsors/<int:pk>", views.SponsorDetailAPIView.as_view(), name="sponsor-detail"),
    path("sponsors/create", views.SponsorCreateAPIView.as_view(), name="sponsor-create"),
    path("sponsors/update/<int:pk>", views.SponsorUpdateAPIView.as_view(), name="sponsor-update"),
    path("sponsors/delete/<int:pk>", views.SponsorDeleteAPIView.as_view(), name="sponsor-delete"),
]
