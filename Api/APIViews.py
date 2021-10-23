from django.views import generic
from rest_framework import generics

from Api.models import *
from Api.serializers import * 


# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSeriallizer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSeriallizer



class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeriallizer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeriallizer



class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSeriallizer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSeriallizer



class CheckoutList(generics.ListCreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSeriallizer

class CheckoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSeriallizer



class AdsList(generics.ListCreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSeriallizer

class AdsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSeriallizer