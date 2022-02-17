from email.headerregistry import Group 
from django.contrib import admin

from .models import Category, Product

class products(admin.ModelAdmin):
    list_display = (
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "branch"
    )
    list_filter = ("date_added",)
    search_fields = ('product_name__startswith',)

class categories(admin.ModelAdmin):
    list_display = (
            "name",
    )
    search_fields = ('categories_name__startswith',)
          

admin.site.register(Category,categories)
admin.site.register(Product ,products)

