from django.contrib import admin
from django.urls import path, include
from category.views import CategoryList, CategoryDetails

urlpatterns = [
    path("category_list", CategoryList.as_view(), name="Category_List"),
    path("category_details/<int:pk>", CategoryDetails.as_view(), name="Category_details"),
]
