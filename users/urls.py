from .views import *
from django.urls import path

app_name = 'users'

urlpatterns = [
        path('login/', login, name='login'),
        path('registration/', registration, name='registration'),
        path('profile/', profile, name='profile'),
        path('users-cart/', user_cart, name='users-cart'),
        path('logout/', logout, name='logout'),
]
