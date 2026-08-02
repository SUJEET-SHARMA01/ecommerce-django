from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:id>/", views.productDetails, name="productDetails"),
    path("products/",views.products, name="products"),
    path("add_to_cart/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("cart/increase/<int:id>/", views.increase_quantity, name="increase_quantity"),
    path("cart/decrease/<int:id>/", views.decrease_quantity, name="decrease_quantity"),
    path("cart/remove/<int:id>/", views.remove_cart, name="remove_cart"),
]
