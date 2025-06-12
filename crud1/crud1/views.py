from django.shortcuts import render,redirect
from product.models import *

def home(request):
    return render(request, 'home.html')

def addProduct(request):
    if request.method == 'POST':
        product = productModel(
            productName = request.POST.get('productName'),
            category = request.POST.get('category'),
            price = request.POST.get('price'),
        )
        product.save()
        return redirect('productList')
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