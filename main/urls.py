from .views import *
from django.urls import path


urlpatterns = [
    path('main/', index, name='index'),
    path('about/', about, name='about'),
]