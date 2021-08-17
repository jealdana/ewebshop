from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
import datetime
from django.views.generic.base import TemplateView
from backend.models import Product
from frontend.forms import ProductForm, ProductFormSet

class LandingPage(TemplateView):
    initial = {'key': 'value'}
    template_name = 'frontend/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_info'] = Product.objects.all().order_by('name')
        context['productForm'] = ProductForm()
        list_for_random = range(100)
        context['list_for_random'] = list_for_random
        return context

from .forms import ProductForm

def createProduct(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            productForm.save()
            return JsonResponse({'success':True})
        else:
            print('invalid form')
            print(productForm)
            return HttpResponse('Error')