from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request, 'electronics/home.html')


def product(request):
    prod = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'electronics/product.html',{"prod":prod,"form":form})

def card(request):
    return render(request, 'electronics/card.html')


