from django.shortcuts import render,redirect
from common.models import Seller
from .models import Product
from django.http import JsonResponse

# Create your views here.
def seller_signup(request):
    return render(request,'sellertemplates/seller_signup.html')

def product_catalog(request):
    seller_products = Product.objects.filter(seller = request.session['seller'])
    return render(request,'sellertemplates/product_catalog.html',{'products': seller_products})

def seller_home(request):
    seller_data = Seller.objects.get(id = request.session['seller'])
    return render(request,'sellertemplates/seller_home.html',{'data':seller_data})

def login(request):
    return render(request,'sellertemplates/seller_login.html')

def addproduct(request):
    if request.method == 'POST':
        msg = ''
        product_name = request.POST['s_productname']
        product_description = request.POST['s_description']
        product_number = request.POST['s_productnumber']
        current_stock = request.POST['s_currentstock']
        product_image = request.FILES['s_fileuploads']
        price = request.POST['s_price']


        products = Product(product_name = product_name,product_description = product_description,
        product_number = product_number, current_stock = current_stock, product_image = product_image,
        price = price, seller_id = request.session['seller']) 
        products.save()
        msg = 'product added sucessfully'
    return render(request,'sellertemplates/addproduct.html',{'msg':msg})

def update_product(request):
    product_data = Product.objects.filter(seller = request.session['seller'])
 
    if request.method == 'POST':

        new_stock = request.POST['new_stock']
        product_id = request.POST['product_id']
        product = Product.objects.get(id = product_id)
        product.current_stock = product.current_stock + int(new_stock)
        product.save()
        msg = 'updated successfully'
    return render(request,'sellertemplates/update_product.html',{'data':product_data})
def change_pass(request):
    msg = ''

    if request.method == 'POST':
        seller_pass = Seller.objects.get(id = request.session['seller'])
        current_pass = request.POST['c_pass']
        new_password = request.POST['new_pass']
        confirm_pass = request.POST['confirm_pass']
        if seller_pass.seller_password == current_pass:
            if new_password == confirm_pass:
                seller_pass.seller_password = new_password
                seller_pass.save()
                msg = 'password changed successfully'
                
            else:
                 msg = 'cant change to same password'
        else:
            msg = 'incorrect password'

            
    return render(request,'sellertemplates/change_pass.html',{'msg':msg})
    

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:customer_login')               #to remove session data from django session table


def getstock(request):
    id = request.POST['id']
    product = Product.objects.get(id = id)
    product_name = product.product_name
    current_stock = product.current_stock
    p_id = product.id
    return JsonResponse({'p_name':product_name,
    'c_stock':current_stock,
    'pid':p_id})
def update_stock(request):
   
    return redirect('seller:update_product')

