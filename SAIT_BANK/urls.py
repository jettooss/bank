from django.contrib import admin
from django.urls import path
from bank.views import *
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bank.urls')),
]
