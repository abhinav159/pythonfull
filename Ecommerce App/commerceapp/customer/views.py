from django.shortcuts import render,redirect
from seller.models import Product
from common.models import Customer
from .models import Cart
from .auth_gaurd import cust_auth

# Create your views here.
@cust_auth
def customer_home(request):
    seller_products = Product.objects.all()

    return render(request,'customertemplates/customer_home.html',{'productlist': seller_products})

@cust_auth

def product_details(request,pid):
    msg = ''
    product_details = Product.objects.get(id = pid)
    if request.method == 'POST':
        product_exist = Cart.objects.filter(product = pid, customer = request.session['customer']).exists()
        

        if not product_exist:
            cart = Cart(customer_id = request.session['customer'],product_id = pid)
            cart.save()
        else:
            msg = 'item already in cart' 
        
    context = {'details':product_details,'msg':msg}

    return render(request,'customertemplates/product_details.html',context)


@cust_auth

def change_password(request):
    msg = ''
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])
        customer_password = request.POST['c_pass']
        new_password = request.POST['n_pass']
        confirm_password = request.POST['confirm_pass']

        if customer.password == customer_password:
            if new_password == confirm_password:
                customer.password = new_password
                customer.save()
                msg = 'password changed sucessfully'
            else:
                msg = 'password does not match'
        else:
            msg = 'incorrect password'

    return render(request,'customertemplates/change_password.html',{'msg':msg})

@cust_auth

def my_cart(request):
    if 'customer' in request.session:
        cart = Cart.objects.filter(customer = request.session['customer'])
        return render(request,'customertemplates/my_cart.html',{'customer_cart':cart})
    else:
        return redirect('common:customer_login')
@cust_auth

def my_order(request):
    return render(request,'customertemplates/my_order.html')
@cust_auth

def profile(request):
    customer_data = Customer.objects.get(id = request.session['customer'])
    return render(request,'customertemplates/profile.html',{'data':customer_data})


def remove_item(request,pid):
    cart_item = Cart.objects.get(product = pid,customer = request.session['customer'])
    cart_item.delete() 
    return redirect('customer:mycart')


def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:customer_login')               #to remove session data from django session table