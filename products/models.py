from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

FLAG_TYPE=(
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature')
)

class Products(models.Model):
    name = models.CharField(max_length=120)
    flag = models.CharField(max_length=10,choises=FLAG_TYPE)
    price = models.FloatField()
    image = models.ImageField(upload_to="product")
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=3000) 
    tags = TaggableManager()
    brand = models.ForeignKey("Brand",related_name="Products_brand",on_delete=models.SET_NULL,null=True)

class ProductsImages(models.Model):
    product= models.ForeignKey(Products,related_name='product_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')


class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user', on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Products, related_name='reviews_product', on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(choices=[(i,i) for i in range (1,6)])
    created_at = models.DateTimeField(defult=timezone.now)