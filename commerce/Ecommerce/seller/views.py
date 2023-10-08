from django.shortcuts import render

# Create your views here.
def addproduct(request):
    return render(request,'sellertemp/addproduct.html')

def change_pass(request):
    return render(request,'sellertemp/change_pass.html')

def product_catalog(request):
    return render(request,'sellertemp/product_catalog.html')

def sellerhome(request):
    return render(request,'sellertemp/sellerhome.html')

def update_product(request):
    return render(request,'sellertemp/update_product.html')