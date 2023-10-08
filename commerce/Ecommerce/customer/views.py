from django.shortcuts import render

# Create your views here.
def change_pass(request):
    return render(request,'customertemp/change_pass.html')

def profile(request):
    return render(request,'customertemp/profile.html')

def product_details(request):
    return render(request,'customertemp/product_details.html')

def my_cart(request):
    return render(request,'customertemp/my_cart.html')

def my_order(request):
    return render(request,'customertemp/my_order.html')

def customer_home(request):
    return render(request,'customertemp/customer_home.html')