from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.views.generic.base import TemplateView
from backend.models import Product

class LandingPage(TemplateView):
    # form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'frontend/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_info'] = Product.objects.all().order_by('name')
        
        list_for_random = range(100)
        context['list_for_random'] = list_for_random

        return context

from .forms import ProductForm

def createProduct(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        photo_url = request.POST['photo_url']
        print(request.POST['photo_url'])
        name = request.POST['name']
        code = request.POST['code']
        price = request.POST['price']
        description = request.POST['description']

        Product.objects.create(
            photo_url = photo_url,
            name = name,
            code = code,
            price = price,
            description = description
        )

        return HttpResponse('')