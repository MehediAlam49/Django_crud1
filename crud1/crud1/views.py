from django.shortcuts import render,redirect
from product.models import *

def home(request):
    return render(request, 'home.html')

def addProduct(request):
    return render(request, 'addProduct.html')

def productList(request):
    productData = productModel.objects.all()
    return render(request, 'productList.html', {'product': productData})

def editProduct(request):
    return render(request, 'editProduct.html')

def deleteProduct(request):
    return redirect('productList.html')

def viewProduct(request):
    return render(request, 'viewProduct.html')