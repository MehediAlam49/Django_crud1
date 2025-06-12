
from django.contrib import admin
from django.urls import path
from crud1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add-product/', addProduct, name='addProduct'),
    path('product-List/', productList, name='productList'),
    path('edit-product/<str:id>', editProduct, name='editProduct'),
    path('delete-product/<str:id>', deleteProduct, name='deleteProduct'),
    path('view-product/', viewProduct, name='viewProduct'),
]
