from django.forms import ModelForm, modelformset_factory
from backend.models import Product

# Create the form class.
class ProductForm(ModelForm):
     class Meta:
         model = Product
         fields = ['photo_url','name','code','price','description']

ProductFormSet = modelformset_factory(Product, fields=('photo_url','name','code','price','description'), exclude=('created',))