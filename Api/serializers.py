from rest_framework import serializers

from .models import *




class UserSeriallizer(serializers.ModelSerializer):

    class Meta:
       model= User
       fields = '__all__'

class ProductSeriallizer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

class CartSeriallizer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

class CheckoutSeriallizer(serializers.ModelSerializer):

    class Meta:
        model = Checkout
        fields = '__all__'

class AdsSeriallizer(serializers.ModelSerializer):

    class Meta:
        model = Ads
        fields = '__all__'
