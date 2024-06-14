from django.shortcuts import render, redirect

from preentrega.models import Product
from preentrega.forms import FindProduct


def index(request):

    return render(request, "index.html")


def products(request):    
    formulario = FindProduct(request.GET)
    if formulario.is_valid():
        description = formulario.cleaned_data['description']
        products = Product.objects.filter(description__icontains=description)
    
    return render(request, 'preentrega/products.html', {'products': products, 'formulario': formulario})
    

def add_product(request):
    if request.method == 'POST':
        description = request.POST.get("product_name")
        price = request.POST.get("product_price")
        product = Product(description=description, price=price)
        product.save()
        return redirect('products')

def find_product(request):
    return render(request, "preentrega/find_product.html")
