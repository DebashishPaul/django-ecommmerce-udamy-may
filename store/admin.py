from django.contrib import admin
from .models import Product, Order

#admin panel modify
admin.site.site_header = "E-com store"
admin.site.site_title = "admin panel"
admin.site.index_title = "Table"

#show all product details
class ProductAll(admin.ModelAdmin):
    def set_category_to_default(self, request, queryset):
        queryset.update(category='default')
    
    set_category_to_default.short_description = 'default category'
    
    list_display = ('name','product_desc','real_price','category',)
    search_fields = ('name','real_price',)
    actions = (set_category_to_default,)
    fields = ('name', 'product_desc', 'real_price', 'category',)
    list_editable = ('real_price','product_desc','category',)
# Register your models here.
admin.site.register(Product, ProductAll)
admin.site.register(Order)
