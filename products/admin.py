from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Manufacturer)
admin.site.register(Image)
admin.site.register(Category)