from django.contrib import admin
from django.urls import path, include
from products.views import ProductList, ProductDetails

urlpatterns = [
    path("product_list", ProductList.as_view(), name="product_list"),
    path("product_details/<int:pk>", ProductDetails.as_view(), name="product_details"),
]
