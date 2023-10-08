from django.urls import path
from . import views


app_name = 'ecom_admin'
urlpatterns = [

    path('approve_cust',views.approve_cust,name='approve_cust'),
    path('approve_seller',views.approve_seller , name='approve_seller'),
    path('home',views.home, name='home'),
    path('view_seller',views.view_seller,name='view_seller'),
    path('view_customer',views.view_customer, name='view_customer'),
]