from django.contrib import admin
from backend.models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)