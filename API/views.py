from django.shortcuts import render
from .serializers import CategorySerializer, ProductsCreateSerializer , ProductsSerializer
from .models import Products, Category
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,permissions

# Create your views here.
class AddCategoryEndpoint(generics.CreateAPIView):
    queryset= Products.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[permissions.AllowAny]

class CategoryListEndpoint(generics.ListAPIView):
    queryset= Products.objects.all()
    serializer_class=ProductsSerializer
    permission_classes=[permissions.AllowAny]

class ProductsEndpoint(generics.ListCreateAPIView):
    serializer_class= ProductsCreateSerializer
    queryset= Products.objects.all()