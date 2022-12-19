from django.contrib import admin
from .models import (Product, Category, Carousel, OrderPlace,ContactUs)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'product_title','product_category', 'product_price', 'descrount_price', 'create_date']
    search_fields = ('user', 'product_title','product_category', 'create_date')
    list_editable = ['product_title','product_price','descrount_price']
    list_display_links = ['pk', 'user']


admin.site.register(Category)
admin.site.register(Carousel)

@admin.register(OrderPlace)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'product', 'quantity', 'email', 'mobile', 'address', 'total_price','status','bkashTrxID']
    search_fields = ('product','user','email','mobile','bkashTrxID','city')
    list_editable = ['status']
    list_display_links = ['user','product']

admin.site.register(ContactUs)