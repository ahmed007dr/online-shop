from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
# Create your models here.

FLAG_TYPE=(
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature')
)

class Products(models.Model):
    name = models.CharField(max_length=120,verbose_name=_('Name'))
    flag = models.CharField(max_length=10,choices=FLAG_TYPE)
    price = models.FloatField(verbose_name=_('price'))
    image = models.ImageField(upload_to="product",verbose_name=_('image'))
    sku = models.IntegerField(verbose_name=_('sku'))
    subtitle = models.TextField(max_length=500,verbose_name=_('subtitle'))
    description = models.TextField(max_length=3000,verbose_name=_('description')) 
    tags = TaggableManager()
    brand = models.ForeignKey("Brand",related_name="Products_brand",on_delete=models.SET_NULL,null=True,verbose_name=_('brand'))

    slug = models.SlugField(blank=True,null=True,unique=True)
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Products, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name
    
    #copy from serializers
    @property #coulmn in db
    def reviews_count(self): #name of function (get_)+ name of column # self couz in class #object product activae
        reviews = self.reviews_product.all().count() # related name from class review
        return reviews
    @property 
    def avg_rate(self):
        total=0 #sum rate: object (one product)
        reviews=self.reviews_product.all() # related name from class review
        
        if len(reviews) > 0 :
            for item in reviews:
                total += item.rate
            avg= total / len(reviews)
        else:
            avg=0
        return avg

class ProductsImages(models.Model):
    product= models.ForeignKey(Products,related_name='product_image',on_delete=models.CASCADE,verbose_name=_('product'))
    image = models.ImageField(upload_to='productimages',verbose_name=_('image'))

    def __str__(self):
        return str(self.id)  # Adjust as needed
class Brand(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('brand'))
    image = models.ImageField(upload_to='brand',verbose_name=_('image'))

    slug = models.SlugField(blank=True,null=True,verbose_name=_('slug'))
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Brand, self).save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name
    @property
    def total_ratings(self):
        total = 0
        for product in self.Products_brand.all():
            total += product.reviews_product.count()
        return total


class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user', on_delete=models.SET_NULL,null=True,verbose_name=_('user'))
    product = models.ForeignKey(Products, related_name='reviews_product', on_delete=models.CASCADE,verbose_name=_('product'))
    review = models.TextField(max_length=500,verbose_name=_('review'))
    rate = models.IntegerField(choices=[(i,i) for i in range (1,6)],verbose_name=_('rate'))
    created_at = models.DateTimeField(default=timezone.now,verbose_name=_('created at'))


    def __str__(self):
        return f'{self.user} - {self.product} - {self.rate}'