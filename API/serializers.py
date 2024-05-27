from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()