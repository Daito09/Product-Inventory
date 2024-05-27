from rest_framework import serializers
from .models import Category, Products

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductsCreateSerializer(serializers.Serializer):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'stock', 'category', 'expiry_date']

class ProductsSerializer(serializers.Serializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Products
        fields = ['name', 'description', 'price']