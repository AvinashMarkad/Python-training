from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'electronics/home.html')

def product(request):
    prod = Product.objects.all()
    return render(request, 'electronics/product.html',{"prod":prod})
