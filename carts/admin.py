from dataclasses import asdict

from msilib import datasizemask
from this import d
from urllib.request import AbstractDigestAuthHandler
from django.contrib import admin
from .models import *
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemAdmin)

