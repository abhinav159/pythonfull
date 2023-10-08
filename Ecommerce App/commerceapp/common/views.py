from django.shortcuts import render,redirect
from .models import Customer,Seller
import random
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
# Create your views here.
def commonhome(request):
    return render(request,'commontemplates/commonhome.html')

def customer_login(request):
    msg = ''
    if request.method == 'POST':
        customer_name = request.POST['user_login']
        c_password = request.POST['user_pass']
        try:
            customer =Customer.objects.get(User_name = customer_name, password = c_password)
            request.session['customer'] = customer.id
            return redirect('customer:customer_home')
        except:
            msg = 'invalid username or password'


    return render(request,'commontemplates/customer_login.html',{'msg':msg})


def seller_login(request):
    msg = ''
    if request.method == 'POST':

        user_name = request.POST['username']
        password = request.POST['passwd']
        try:
            user = Seller.objects.get(seller_user = user_name, seller_password = password)

            request.session['seller'] = user.id
            return redirect('seller:sellerhome')
        except:
            msg = 'invalid username or password'

    return render(request,'commontemplates/seller_login.html', {'msg':msg})

def seller_reg(request):
    if request.method == 'POST':
        seller_name = request.POST['s_sellername']
        seller_address = request.POST['s_address']
        seller_phone = request.POST['s_phone']
        seller_email = request.POST['s_email']
        seller_companyname = request.POST['s_cmpny']
        seller_accountholder = request.POST['s_accname']
        seller_ifsc = request.POST['s_ifsc']
        seller_branch = request.POST['s_branch']
        seller_accountnumber = request.POST['s_accnum']
        seller_photo = request.FILES['s_file']
        
        seller_username = random.randint(1111,9999)
        seller_password = 'sel-' + seller_name.lower() + str(seller_username)
        message = 'hai! Your username is ' + str(seller_username) + ' and temporary password is ' + seller_password
        
        send_mail(
            'username and temporary password',
            message,
            settings.EMAIL_HOST_USER,
            [seller_email,],
            fail_silently=False

        )
        seller_new = Seller(seller_name = seller_name, seller_address = seller_address, 
        seller_phone = seller_phone, seller_email = seller_email, seller_companyname = seller_companyname,
        seller_accholder = seller_accountholder, seller_ifsc = seller_ifsc,seller_branch = seller_branch,
        seller_accno = seller_accountnumber, seller_password = seller_password, seller_pic = seller_photo, 
        seller_user = seller_username )
        
        seller_new.save()
    return render(request,'commontemplates/seller_reg.html')

def customer_reg(request):

    if request.method == 'POST':  # when submit button clicked
        cst_name =  request.POST['c_name']  # here we get data input in textbox , here c_name is name attribute of firstname textbox
        cst_mobile =  request.POST['c_mobile']
        cst_address =  request.POST['c_address']
        cst_gender =  request.POST['gender']
        cst_mail =  request.POST['c_mail']
        # cst_pass =  request.POST['c_pass']
        # to insert data into table
        customer_username = random.randint(1111,9999)
        customer_password = 'sel-' + cst_name.lower() + str(customer_username)
        message = 'hai! Your username is ' + str(customer_username) + ' and temporary password is ' + customer_password


        send_mail(
            'username and temporary password',
            message,
            settings.EMAIL_HOST_USER,
            [cst_mail,],
            fail_silently=False

        )


        # 1. create object of model class, eg : Customer

        new_customer = Customer(Customer_Name = cst_name , E_mail = cst_mail , User_name =  customer_username 
        ,Mobile_number = cst_mobile , Address = cst_address , gender = cst_gender, password = customer_password,)
       
        # call save() method, here save() method is equivalent to insert into sql query 
        new_customer.save()

    return render(request,'commontemplates/customer_reg.html')

def email_exist(request):
    email =request.POST['email']  # here email is the key inside json

    status = Customer.objects.filter(E_mail = email).exists()
    return JsonResponse({
        'status':status
    })
