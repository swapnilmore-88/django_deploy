from django.forms import ModelForm

from product.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product # here it will create a form by using 'Product' model automatically
        fields = "__all__" # here it will include all columns from Form
        # if we want specific colimn then we can add only those names in list above e.g.["price","qty"]