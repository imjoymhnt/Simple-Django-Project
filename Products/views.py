from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

class ProductView(ListView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'products'