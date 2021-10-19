from enum import unique
from django.db import models

# Create your models here.
class User(models.Model):
    First_Name  = models.CharField(max_length = 150)
    Last_Name   = models.CharField(max_length = 150)
    Phone       = models.CharField(max_length=11)
    email       = models.EmailField()
    Address     = models.TextField()
    portal      = models.IntegerField()
    image       = models.ImageField(path=f'image/{First_Name}')

    def __str__(self):
        return self.name


class Product(models.Model):
    name         = models.CharField(max_length = 150)
    tag          = models.CharField(max_length = 50, unique=True)
    image        = models.ImageField(path=f'image/{name}')
    
    def __str__(self):
        return self.name


class Order(models.Model):
    items   = models.ManyToManyField(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    order   = models.ForeignKey(Order, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
        

class Checkout(models.Model):
    cart        = models.ForeignKey(Cart, on_delete=models.CASCADE)
    First_Name  = models.CharField(max_length = 150)
    Last_Name   = models.CharField(max_length = 150)
    Phone       = models.CharField(max_length=11)
    email       = models.EmailField()
    Address     = models.TextField()
    portal      = models.IntegerField()
    image       = models.ImageField(path=f'image/{First_Name}')

    def __str__(self):
        return self.name

class Ads(models.Model):
    image       = models.ImageField(path='ads/')
    url         = models.URLField()

    

