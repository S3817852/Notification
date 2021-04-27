from django.contrib import admin

from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Product, ProductAdmin)
