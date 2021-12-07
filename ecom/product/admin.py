from django.contrib import admin
from product.models import Product

# Register your models here.


admin.site.register(Product) # without this product app will not be available in website