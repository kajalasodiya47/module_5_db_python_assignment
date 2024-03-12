from django.db import models

# Create your models here.

# # product model 
class ProductMst(models.Model):

     product_name = models.CharField(max_length=20)
     
     def __str__(self):
        return self.product_name

# product category model
class ProductSubCat(models.Model):
    product = models.ForeignKey(ProductMst,on_delete=models.CASCADE)
    product_price = models.IntegerField()
    product_image = models.FileField(default="",upload_to="product_picture")
    product_model = models.CharField(max_length=20)
    product_ram = models.CharField(max_length=20)
