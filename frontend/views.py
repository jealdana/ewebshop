from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.views.generic.base import TemplateView


class LandingPage(TemplateView):
    # form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'frontend/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context