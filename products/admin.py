from django.contrib import admin
from .models import Products , ProductsImages , Review , Brand
# Register your models here.

class ProductImageInLine(admin.TabularInline):
    model = ProductsImages


class ProductAdmin(admin.ModelAdmin):
    inlines =[ProductsImages]

# to merge to class in same one product with products image 

admin.site.register(Products)
admin.site.register(ProductsImages)
admin.site.register(Review)
admin.site.register(Brand)