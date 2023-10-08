from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Customer, Seller

                                          
class Useredit(admin.ModelAdmin):               
    search_fields = ['first_name']
    list_display = ['User_name', 'Customer_Name']
    list_filter=('Customer_Name','User_name') 

admin.site.register(Customer, Useredit)
admin.site.register(Seller)