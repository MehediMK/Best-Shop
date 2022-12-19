from django import template
from shop.models import Product, Category
from django.db.models import Max

register = template.Library()

"""
# {% sample_tag 1 2 "$" %}
@register.simple_tag
def sample_tag(a,b,c):
    print('৳')
    print(a,b,c)
    return "৳"
# {% my_tag 123 "abcd" book.title warning="This is warning"|lower profile=1 %}
@register.simple_tag
def my_tag(a, b, *args, **kwargs):
    warning = kwargs['warning']
    profile = kwargs['profile']
    return warning
"""
  
@register.inclusion_tag('common/navbar.html', takes_context=True)
def navbar_category(context):
    request = context['request']
    categories = Category.objects.all()
    return {'categories': categories, 'request':request}
  

@register.filter(name='description_short')
def description_short(value):
    if len(value)>100:
        return value[:100]+" ..."
    else:
        return value
  
@register.simple_tag
def discount_amount(product_price, descrount_price):
    return (float(product_price) - float(descrount_price))
  
@register.simple_tag
def cart_count(cart):
    cart_list = cart.keys()
    return len(cart_list)

@register.simple_tag
def product_quantity(cart, product_id):
    if cart and product_id:
        product = cart.get(str(product_id))
        return product
    else:
        return "1"

@register.simple_tag
def maxprice():
    max_price = Product.objects.all().aggregate(Max('product_price'))
    return max_price.get('product_price__max')

@register.simple_tag
def product_descrount_price(product_id):
    if product_id:
        product = Product.objects.get(id=product_id)
        product_price = product.product_price
        descrount_price = product.descrount_price
        return product_price-descrount_price
    else:
        return "0"

@register.simple_tag
def product_descrount_with_total_price(cart, product_id):
    if cart and product_id:
        product = Product.objects.get(id=product_id)
        product_quantity = cart.get(str(product_id))
        product_price = product.product_price
        descrount_price = product.descrount_price
        return (product_price-descrount_price)*product_quantity
    else:
        return "0"

@register.simple_tag
def cat_total_amount(session):
    if cart := session.get('cart'):
        if cart:
            total_price = 0
            cart_list = cart.keys()
            for product_id in cart_list:
                product = Product.objects.get(id=product_id)
                product_quantity = cart.get(str(product_id))
                product_price = product.product_price - product.descrount_price
                total_price += product_price * product_quantity
            session.cart_total_price = total_price
            return total_price
        else:
            return "0"
    else:
        return "0"

@register.simple_tag
def total_price_with_shiping_cost(cart_total_price, shipping_cost):
    if cart_total_price:
        return cart_total_price + int(shipping_cost)


@register.simple_tag
def currency_tk():
    return "৳ "

@register.simple_tag
def currency_usd():
    return "$ "