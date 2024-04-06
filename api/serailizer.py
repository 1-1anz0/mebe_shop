from rest_framework import serializers
from goods.models import *

class ProductsS(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'