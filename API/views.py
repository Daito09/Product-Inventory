from django.shortcuts import render
from .serializers import CategorySerializer, ProductsCreateSerializer , ProductsSerializer
from .models import Products, Category
from rest_framework import generics,permissions

# Create your views here.
class AddCategoryEndpoint(generics.CreateAPIView):
    queryset= Products.objects.all()
    serializer_class=CategorySerializer
    lookup_field= 'pk'
    permission_classes=[permissions.AllowAny]

class CategoryListEndpoint(generics.ListAPIView):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='pk'
    permission_classes=[permissions.AllowAny]

class ProductsAddListEndpoint(generics.ListCreateAPIView):
    queryset= Products.objects.all()
    serializer_class= ProductsCreateSerializer
    lookup_field= 'pk'
    queryset= Products.objects.all()