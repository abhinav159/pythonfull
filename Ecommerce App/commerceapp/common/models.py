from django.db import models

# Create your models here.
class Customer(models.Model):
    Customer_Name = models.CharField(max_length=30)
    E_mail = models.CharField(max_length=30)
    User_name = models.CharField(max_length=30)
    Mobile_number = models.BigIntegerField()
    Address = models.CharField(max_length=100)
    password = models.CharField(max_length=30,default='')
    gender = models.CharField(max_length=10)



class Seller(models.Model):
    seller_name = models.CharField(max_length=30)
    seller_address = models.CharField(max_length=30)
    seller_phone = models.CharField(max_length=30)
    seller_email = models.CharField(max_length=40)
    seller_companyname = models.CharField(max_length=100)
    seller_accholder = models.CharField(max_length=30,default='')
    seller_ifsc = models.CharField(max_length=30)
    seller_branch = models.CharField(max_length=30)
    seller_accno = models.CharField(max_length=30)
    seller_password = models.CharField(max_length=30)
    seller_pic = models.ImageField(upload_to='seller/',)
    seller_user = models.CharField(max_length=30,default='')
    approved = models.BooleanField(default=False)


     

    