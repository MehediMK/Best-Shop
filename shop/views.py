from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import (Product, Category, Carousel, OrderPlace, ContactUs)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
from django.contrib import messages
from .filter import *

def index(request):
    context = {}
    context['categories'] = Category.objects.all()
    context['products'] = Product.objects.all()
    context['carousels'] = Carousel.objects.all()
    return render(request,'shop/index.html', context)

def shop(request):
    context = {}

    min_price = request.GET.get('min')
    max_price = request.GET.get('max')
    page = request.GET.get('page', 1)
    search = request.GET.get('search')
    category = request.GET.get('category')    
    
    sortby = request.GET.get('sortby')
    if sortby:
        request.session['sortby'] = sortby
    sortby = request.session.get('sortby')

    context['categories'] = Category.objects.all()

    products = []
    if category:
        products = product_search(category=category, session_sortby=sortby)        

    elif min_price and max_price:
        products = product_search(min_price=min_price, max_price=max_price)

    elif search:
        products = product_search(search=search, session_sortby=sortby)
        
    else:
        products = product_search(session_sortby=sortby)        

    products_paginator = Paginator(products, 20)
    try:
        products = products_paginator.page(page)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)
    context['products'] = products  
    return render(request,'shop/shop.html',context)

def product_detail(request,id):
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.all()[:10]
    return render(request,'shop/detail.html',{'product':product,'related_products':related_products})


def add_cart(request):
    if request.method == 'POST':
        cartpage = request.POST.get('cartpage')
        product_detail = request.POST.get('product_detail')
        remove = request.POST.get('remove')
        product_id = request.POST.get('product_id')

        if product_id:
            cart = request.session.get('cart')
            if cart:
                product = cart.get(product_id)
                if product:
                    if remove:
                        if product>1:
                            cart[product_id] = int(product)-1
                        else:
                            cart[product_id] = 1
                    else:
                        cart[product_id] = int(product)+1
                else:
                    cart[product_id] = 1
            else:
                cart = {}
                cart[product_id] = 1
            request.session['cart'] = cart
        else:
            print("product id not found")
        if cartpage:
            return redirect('cartlist')        
        elif product_detail:
            return redirect('product_detail')        
    return redirect('shop')

def cartlist(request):
    cart = request.session.get('cart')
    products = []
    if cart:
        product_ids = cart.keys()
        for product_id in product_ids:
            product = get_object_or_404(Product, id=product_id)
            products.append(product)
    return render(request,'shop/cart.html',{'products':products})

def cart_item_pop(request,id):
    cart = request.session.get('cart')
    if cart and id:
        key = str(id)
        del request.session.get('cart')[key]
        request.session['cart'] = cart
    return redirect('cartlist')
        
@login_required(login_url='/account/login/')
def checkout(request):
    shiping_cost = 500
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            city = request.POST.get('city')
            zip =  request.POST.get('zip')
            bkashTrxID = request.POST.get('bkashTrxID')
            cart = request.session.get('cart')
            if cart:
                cart_keys = [int(key) for key in cart.keys()]
                products = Product.get_product_by_id(cart_keys)
                for product in products:
                    discount_price = product.product_price - product.descrount_price
                    order = OrderPlace(user = user,product = product, quantity = cart.get(str(product.id)), fname = fname, lname = lname, email = email, mobile = mobile, address = address, city = city, zip =  zip, total_amout = discount_price, bkashTrxID = bkashTrxID)            
                    order.save()
                request.session['cart'] = {}
            return redirect('userprofile')
    
    return render(request,'shop/checkout.html',{'shiping_cost':shiping_cost})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')    
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)
        if name and email and subject and message:
            ContactUs(name=name, email=email, subject=subject, message=message).save()
            from_email = settings.DEFAULT_FROM_EMAIL
            if subject and message and email:
                try:
                    send_mail(subject, message, from_email, [email],  fail_silently=False,)
                    messages.success(request, f"Hello {name},\nThanks for contact with us!") 
                except BadHeaderError as error:
                    messages.error(request, f"{error}")                
            else:
                messages.error(request,f"Mail Subject or message body or your email error")
        else:
            messages.error(request,f"Mail Subject or message body or your email error")
                
    return render(request,'shop/contact.html')