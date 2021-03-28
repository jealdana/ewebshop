from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.views.generic.base import TemplateView


class LandingPage(TemplateView):
    # form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'frontend/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_info'] = [
            {
                'id': 10,
                'photo_url':"https://ih1.redbubble.net/image.2039039614.0432/icr,iphone_12_tough,back,a,x1000-pad,1000x1000,f8f8f8.jpg",
                'name': "Forest during winter iPhone Case & Cover",
                'price': 26.64,
                'description': "Lovely sight across the fields towards a snowed forest in winter",
                'tag': "winter"
            }
        ]
        
        list_for_random = range(100)
        context['list_for_random'] = list_for_random

        return context