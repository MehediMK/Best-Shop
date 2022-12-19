from django.urls import path
from .views import (index,shop,product_detail,add_cart,cartlist,cart_item_pop,checkout,contact)

# for sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
# model import
from shop.models import Product

info_dict = {
    'queryset': Product.objects.all(),
}

urlpatterns = [
    path('', index, name='index'),
    path('products-list/', shop, name='shop'),
    path('product-detail/<int:id>/', product_detail, name='product_detail'),
    path('add-cart/', add_cart, name='add_cart'),
    path('products-cart/', cartlist, name='cartlist'),
    path('cart-remove/<int:id>/', cart_item_pop, name='cart_item_pop'),
    path('products-checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('sitemap.xml', sitemap, {'sitemaps': {'products': GenericSitemap(info_dict, priority=0.6)}}, 
        name='django.contrib.sitemaps.views.sitemap'),
]
