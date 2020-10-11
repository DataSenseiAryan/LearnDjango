from django.db import models

# Create your models here.
class Destination(models.Model):
    
    price = models.IntegerField(default= 0)
    name = models.CharField(max_length =100)
    desc =models.TextField()
    img = models.ImageField(upload_to = 'pics')
    offer = models.BooleanField(default = False)

