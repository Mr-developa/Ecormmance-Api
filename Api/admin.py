from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Checkout)
admin.site.register(Cart)
admin.site.register(Ads)