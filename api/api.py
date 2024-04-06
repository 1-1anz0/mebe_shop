from api.serailizer import *
from rest_framework import viewsets, permissions
from goods.models import *

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()

    serializer_class = ProductsS