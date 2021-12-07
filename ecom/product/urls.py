from django.urls import path
from product.views import create_product, get_products, update_product, delete_product

urlpatterns = [
    path('', get_products, name ="get_all"),# its a indexpage for /product route#
    path('save', create_product, name="save"),
    path('update/<int:id>', update_product, name="update"),
    path('delete/<int:id>', delete_product, name="remove")
    # path('get', create_product, name="save")
]

# here '' is a index page
# we write only name of function from view file and we dont call it
# all above routes are after product/ route e.g. product/save, product/update etc