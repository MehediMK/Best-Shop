from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=20, blank=False)
    category_image = models.ImageField(upload_to='category_image')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_title = models.CharField(max_length=250, blank=False)
    product_image = models.ImageField(upload_to='product_image', blank=False)
    product_price = models.DecimalField(max_digits=6,decimal_places=2)
    descrount_price = models.DecimalField(max_digits=6,decimal_places=2)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_description = models.TextField(max_length=600,blank=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_title
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)

class Carousel(models.Model):
    Catitle = models.CharField(max_length=100,verbose_name='Title',blank=False)
    CaSubTitle = models.CharField(max_length=150,verbose_name='Subtitle',blank=False)
    CaImage = models.ImageField(upload_to='carouselImage',verbose_name='Image',blank=False)
    offer_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Catitle

class OrderPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    fname = models.CharField(max_length=20,null=False)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50,null=False)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    zip =  models.CharField(max_length=10)
    total_amout = models.DecimalField(max_digits=6,decimal_places=2)
    bkashTrxID = models.CharField(max_length=30)
    status  = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"
        
    @property
    def total_price(self):
        return self.quantity*self.total_amout
    
    @staticmethod
    def get_orders_by_customer(user):
        return OrderPlace.objects.filter(user = user).order_by('-id')

class ContactUs(models.Model):
    name = models.CharField(max_length=40,blank=False)
    email = models.EmailField(max_length=50)
    subject = models.EmailField(max_length=50,blank=False)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"
