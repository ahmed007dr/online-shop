from django.db import models
from django.contrib.auth.models import User
# Create your models here.

ADDRESS_TYPE = (
    ('home','home'),
    ('office','office'),
    ('Bussnines','Bussnines'),
    ('Other','Other')
)

class Address(models.Model):
    user = models.ForeignKey(User , related_name='user_address',on_deleted=models.CASCADE)
    address = models.TextField(max_length=200)
    type = models.CharField(max_length=12,choices=ADDRESS_TYPE)
    
