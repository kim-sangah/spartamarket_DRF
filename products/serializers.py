from rest_framework import serializers
from .models import Product

# 물건
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'