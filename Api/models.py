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
    image       = models.ImageField(upload_to=f'user/')

    def __str__(self):
        return self.First_Name


class Product(models.Model):
    name         = models.CharField(max_length = 150)
    price        = models.FloatField()
    image        = models.ImageField(upload_to=f'products/')
    
    def __str__(self):
        return self.name


class Order(models.Model):
    items   = models.ForeignKey(Product, on_delete=models.CASCADE)


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
    image       = models.ImageField(upload_to=f'checkout/')

    def __str__(self):
        return self.First_name

class Ads(models.Model):
    image       = models.ImageField(upload_to='ads/')
    url         = models.URLField()

    

