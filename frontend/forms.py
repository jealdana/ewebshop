from django.forms import ModelForm
from backend.models import Product

# Create the form class.
class ProductForm(ModelForm):
     class Meta:
         model = Product
         fields = ['photo_url','name','code','price','description']