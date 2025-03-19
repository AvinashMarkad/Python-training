from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'electronics/home.html')


def product(request):
    prod = Product.objects.all()
    return render(request, 'electronics/product.html',{"prod":prod})

def card(request):
    return render(request, 'electronics/card.html')
