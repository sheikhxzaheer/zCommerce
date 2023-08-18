from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_image = models.URLField(blank=True)
    product_title = models.CharField(max_length=50, default='')
    product_price = models.IntegerField(default=0, null=True, blank=True)
    product_offer_price = models.IntegerField(default=0, null=True, blank=True)
    product_description = HTMLField(default='')