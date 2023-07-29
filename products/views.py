from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def products(request):
    return HttpResponse('<h1 style="text-align:center; color: blue">Products</h1>')

def new_products(request):
    return HttpResponse('<h1 style="text-align:center; color: green">New Products</h1>')
