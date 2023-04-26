from django.contrib import admin
from .models import *
# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_price')

admin.site.register(Product, productAdmin),