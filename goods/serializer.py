from rest_framework import serializers
from .models import *


class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class CategoryS(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'