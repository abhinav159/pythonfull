from django.shortcuts import render,redirect
import random
from django.core.mail import send_mail
from .models import Customer,Seller
from django.conf import settings


# Create your views here.
def commonhome(request):
    return render(request,'commontemplates/commonhome.html')

def customer_login(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            customer = Customer.objects.get(E_mail = email, password = password)
            request.session['customer'] = customer.id
            return redirect('customer:customer_home')
        except:
            msg = 'incorrect email or password'
    return render(request,'commontemplates/customer_login.html',{'msg':msg})

def seller_login(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            seller = Seller.objects.get(seller_user = username, seller_password = password)
            request.session['seller'] = seller.id
            return redirect('seller:sellerhome')
        except:
            msg = 'incorrect username or password'
    return render(request,'commontemplates/seller_login.html',{'msg':msg})

def customer_reg(request):
    if request.method == 'POST':
        Customer_Name = request.POST['cst_name']
        E_mail = request.POST['cst_email']
        Mobile_number = request.POST['cst_phone']
        Address = request.POST['cst_address']
        password = request.POST['cst_pass']
        gender = request.POST['cst_gender']

        new_customer = Customer(Customer_Name = Customer_Name, E_mail = E_mail,
         Mobile_number = Mobile_number, Address = Address, password = password, gender = gender)

        new_customer.save()

    return render(request,'commontemplates/customer_reg.html')

def seller_reg(request):
    if request.method == 'POST':
        seller_name = request.POST['s_sellername']
        seller_address = request.POST['s_address']
        seller_phone = request.POST['s_phone']
        seller_email = request.POST['s_email']
        seller_companyname = request.POST['s_cmpny']
        seller_accholder = request.POST['s_accname']
        seller_ifsc = request.POST['s_ifsc']
        seller_branch = request.POST['s_branch']
        seller_accno = request.POST['s_accnum']
        seller_pic = request.FILES['s_pic']

        user_name = random.randint(1111,9999)
        seller_password = 'sel' + seller_name.lower() + str(user_name)
        message = 'here is your username....' + str(user_name) + 'your password is...' + seller_password

        send_mail(
            'username and temporary password',
            message,
            settings.EMAIL_HOST_USER,
            [seller_email,],
            fail_silently=False
        )
        new_seller = Seller(seller_name = seller_name, seller_address = seller_address, seller_phone = seller_phone
        , seller_email = seller_email, seller_companyname = seller_companyname, seller_accholder = seller_accholder
        , seller_ifsc = seller_ifsc, seller_branch = seller_branch, seller_accno = seller_accno, seller_pic = seller_pic
        , seller_user = user_name, seller_password = seller_password)

        new_seller.save()



    return render(request,'commontemplates/seller_reg.html')