
from django.contrib import admin
from django.urls import path
from crud1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
