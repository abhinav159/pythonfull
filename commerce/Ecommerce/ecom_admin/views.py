from django.shortcuts import render

# Create your views here.
def approve_cust(request):
    return render(request,'ecomtemplates/approve_cust.html')


def approve_seller(request):
    return render(request,'ecomtemplates/approve_seller.html')


def home(request):
    return render(request,'ecomtemplates/home.html')


def view_customer(request):
    return render(request,'ecomtemplates/view_customer.html')


def view_seller(request):
    return render(request,'ecomtemplates/view_seller.html')