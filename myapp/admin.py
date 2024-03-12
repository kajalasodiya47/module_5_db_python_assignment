from django.contrib import admin
from . models import *

# Register your models here.

# register product model here
admin.site.register(ProductMst)
# register product sub category model here
admin.site.register(ProductSubCat)
