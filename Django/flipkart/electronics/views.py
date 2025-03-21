from django.shortcuts import render, get_object_or_404, redirect
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
        form = ProductForm()
    return render(request, 'electronics/product.html',{"prod":prod,"form":form})

def card(request):
    return render(request, 'electronics/card.html')

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('electronics/product')  # Update this line

def update_product(request, id):
    prod = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('electronics/product')  # Redirect to the product list page
    else:
        form = ProductForm(instance=prod)

    return render(request, 'electronics/update_product.html', {"form": form, "product": prod})