from django.shortcuts import render

# Create your views here.
from category.models import Category
from rest_framework.views import APIView
from category.serializers import Categoryserializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CategoryList(APIView):
    def get(self, request):
        """Fetching all the category present"""
        categories = Category.objects.all()
        serilaizer = Categoryserializers(categories, many=True)
        return Response(serilaizer.data)

    def post(self, request):
        """Creating the Data for category"""
        serilaizer = Categoryserializers(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetails(APIView):
    def put(self, request, pk):
        """Updating the category"""
        category = get_object_or_404(Category, pk=pk)
        serilaizer = Categoryserializers(category, data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_200_OK)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Deleting the category"""
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
