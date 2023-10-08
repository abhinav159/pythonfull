from django.shortcuts import render,redirect
from common.models import Customer,Seller
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request,'admtemplates/home.html')
def approve_seller(request):
    sellers = Seller.objects.all()
    return render(request,'admtemplates/approve_seller.html',{'seller_list':sellers})
def view_customer(request):
    return render(request,'admtemplates/view_customer.html')
def view_seller(request):
    return render(request,'admtemplates/view_seller.html')
def projecthome(request):
    return render(request,'admtemplates/projecthome.html')
def approve_cust(request):

    customers = Customer.objects.all()
    return render(request,'admtemplates/approve_cust.html',{"customer_list":customers})

def approve(request,sid):

    seller = Seller.objects.get(id=sid)
    email = Seller.objects.filter(seller_email = request.session['seller'])
    message = 'You are approved to login'
    send_mail(
        'Approved',
        message,
        settings.EMAIL_HOST_USER,
        [seller.seller_email,],
        
    )
    seller.approved = True
    seller.save()
    return redirect('ecom_admin:viewSeller')

def remove(request,sid):
    seller = Seller.objects.get(id = sid, seller_id = request.session['seller'])
    seller.delete()
    return redirect('com_adm:approveseller')