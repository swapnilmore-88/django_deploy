from django.db import models


# Create your models here.
class Product(models.Model):
    class Meta:  # helps to diasplay name on portal bcoz django always put 's' at end of  models name
        # db_table="Product" ------ if this is not provided then table name will be product_product
        verbose_name = "Product"
        verbose_name_plural = "Products"

    pid = models.IntegerField(verbose_name='Product_id', primary_key=True)
    name = models.CharField(verbose_name="Product's name", max_length=40, null=False, blank=False)
    brand = models.CharField(verbose_name="Brand name", max_length=50, null=False, blank=False)
    price = models.FloatField(verbose_name="Product price", null=False, blank=False)
    qty = models.IntegerField(verbose_name="Quantity", default=1)
    warranty = models.IntegerField(verbose_name='Warranty in months', default=1)
    delivery = models.CharField(verbose_name="delivery_country", max_length=40, default="India")

    def __str__(self):  # helps to display on port
        return f"{self.name} --> {self.brand}"



