from django.shortcuts import render
from rest_framework.views import APIView
from products.serializers import Productserializers
from products.models import Product
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
class ProductList(APIView):
    """Fetching all the Product present"""
    def get(self, request):
        categories = Product.objects.all()
        serilaizer = Productserializers(categories, many=True)
        return Response(serilaizer.data)

    def post(self, request):
        """Creating the Data for Product"""
        serilaizer = Productserializers(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_201_CREATED)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetails(APIView):
    def put(self, request, pk):
        """Updating the Product"""
        product = get_object_or_404(Product, pk=pk)
        serilaizer = Productserializers(product, data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_200_OK)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Deleting the Product"""
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
