from django.contrib import admin
from .models import *

# Register your models here.
class cartAdmin(admin.ModelAdmin):
    list_display = ['user', 'quantity']
admin.site.register(Cart, cartAdmin),