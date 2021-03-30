"""ewebshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.models import User
from frontend import urls
from frontend.views import LandingPage,createProduct
from backend.views import product_list, product_detail
from django.contrib.auth import views

app_name = 'frontend'

urlpatterns = [
    url(r'^$', LandingPage.as_view()),
    path('product/', product_list.as_view()),
    path('product/create/', createProduct),
    path('product/<int:pk>/', product_detail),
]
