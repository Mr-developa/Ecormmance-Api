from django.contrib import admin
from django.urls import path

from .APIViews import *


urlpatterns = [
    path("", ProductList.as_view(), name='Product'),
    path("<int:pk>", ProductDetail.as_view(), name='ProductDetail'),
   
    # path("user", UserList.as_view(), name='user'),
    # path("user/<int:pk>", UserDetail.as_view(), name='UserDetail'),
   
    path("cart", CartList.as_view(), name='Cart'),
    path("cart/<int:pk>", CartDetail.as_view(), name='CartDetail'),
   
    path("checkout", CheckoutList.as_view(), name='Checkout'),
    path("checkout/<int:pk>", CheckoutDetail.as_view(), name='CheckoutDetail'),
   
    path("ads", AdsList.as_view(), name='Ads'),
    path("ads/<int:pk>", AdsDetail.as_view(), name='AdsDetail'),
   
]