from django.shortcuts import render
from goods.models import *

# Create your views here.

app_name='main'

def index(request):

    

    return render(request, 'main/index.html',)

def about(request):
    context = {
        'content': 'Ahuyyenyy Магазин мебели HOME'
    }
    return render(request, 'main/about.html', context)