from django.contrib import admin
from .models import Product, Order

#admin panel modify
admin.site.site_header = "E-com store"
admin.site.site_title = "admin panel"
admin.site.index_title = "Table"

#show all product details
class ProductAll(admin.ModelAdmin):
    list_display = ('name','product_desc','real_price')
    search_fields = ('name','real_price')
# Register your models here.
admin.site.register(Product, ProductAll)
admin.site.register(Order)
