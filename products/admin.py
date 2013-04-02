from django.contrib import admin
from products.models import Model, Vendor, Category

__author__ = 'sergio'


admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Model)