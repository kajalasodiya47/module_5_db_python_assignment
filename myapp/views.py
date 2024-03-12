from django.shortcuts import render,redirect
from . models import *
# Create your views here.

# logic for add the products
def add_product(request):
    if request.POST:
         pid =  ProductMst.objects.create(product_name=request.POST['p_name'])
         if pid:
           ProductSubCat.objects.create(
               product = pid,
               product_price = request.POST['p_price'],
               product_model = request.POST['p_model'],
               product_ram = request.POST['p_ram'],
               product_image = request.FILES['p_image']
           )
         return redirect('view_product')
    else:
      return render(request,"add_product.html")
    
# logic for view all the products
def view_product(request):
      products =  ProductMst.objects.all()
      product_details = {}
      for product in products:
         productcat = ProductSubCat.objects.filter(product=product) 
         product_details[product] = productcat
      return render(request,"view_product.html",{'product_details':product_details})

# logic for show particular product for the edit purpose
def pedit(request,pk):
    product = ProductMst.objects.get(pk=pk)
    product_cat = ProductSubCat.objects.filter(product=product)
    return render(request,"edit_product.html",{'product_cat':product_cat,'product':product})

# logic for the update particular product
def p_edit(request,pk):
    product = ProductMst.objects.get(pk=pk)
    product.product_name = request.POST['p_name']
    product.save()
    product_cats = ProductSubCat.objects.filter(product=product)
    for product_cat in product_cats:
      product_cat.product = product
      product_cat.product_price = request.POST['p_price']
      product_cat.product_model = request.POST['p_model']
      product_cat.product_ram = request.POST['p_ram']
      if "p_image" in request.FILES:
         product_cat.product_image = request.FILES['p_image']
      product_cat.save()
    return redirect('view_product')

# logic for delete product
def pdelete(request,pk):
     product = ProductMst.objects.get(pk=pk)
     product.delete()
     return redirect('view_product')

# logic for search particular product
def search_product(request):
    if request.POST:
      query = request.POST.get('p_name',None)
      if query:
        products = ProductMst.objects.filter(product_name__contains=query)
        product_cats = ProductSubCat.objects.filter(product__in=products)
        return render(request,"search_product.html",{'products':products,'product_cats':product_cats})
      else:
         return render(request,"search_product.html")  
    else:  
      return render(request,"search_product.html")  
  
       