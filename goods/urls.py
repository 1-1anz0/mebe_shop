from .views import *
from django.urls import path, include
from .api import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('products', ProductsViewSet)
router.register('category', CategoryViewSet)


app_name='catalog'



urlpatterns = [

    path('search/', catalog, name='search'),
    path('<slug:category_slug>/', catalog, name='catalog'),
    path('product/<str:product_slug>/', product, name='product'),
    path('api/', include(router.urls))
]