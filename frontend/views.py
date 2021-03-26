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
            },
            {
                'id': 11,
                'photo_url':"https://ih1.redbubble.net/image.2042818921.5560/icr,iphone_12_soft,back,a,x1000-pad,1000x1000,f8f8f8.jpg",
                'name': "Thriving during winter iPhone Case & Cover",
                'code': '123CODE',
                'price': 16.9,
                'description': "Thriving through the winter's cold",
                'tag': "winter"
            },
            {
                'id': 12,
                'photo_url':"https://ih1.redbubble.net/image.2042818921.5560/icr,iphone_12_soft,back,a,x1000-pad,1000x1000,f8f8f8.jpg",
                'name': "Thriving during winter iPhone Case & Cover",
                'price': 16.9,
                'description': "Thriving through the winter's cold",
                'tag': "winter"
            },
            {
                'id': 13,
                'photo_url':"https://ih1.redbubble.net/image.2042818921.5560/icr,iphone_12_soft,back,a,x1000-pad,1000x1000,f8f8f8.jpg",
                'name': "Thriving during winter iPhone Case & Cover",
                'code': '123CODE',
                'price': 16.9,
                'description': "Thriving through the winter's cold",
                'tag': "winter"
            },
            {
                'id': 14,
                'photo_url':"https://ih1.redbubble.net/image.2042818921.5560/icr,iphone_12_soft,back,a,x1000-pad,1000x1000,f8f8f8.jpg",
                'name': "Thriving during winter iPhone Case & Cover",
                'price': 16.9,
                'description': "Thriving through the winter's cold",
                'tag': "winter"
            }
        ]
        
        list_for_random = range(100)
        context['list_for_random'] = list_for_random

        return context