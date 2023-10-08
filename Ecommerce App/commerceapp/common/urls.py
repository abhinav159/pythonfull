from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [

    path('commonhome',views.commonhome),
    path('customer_login',views.customer_login, name='customer_login'),
    path('customer_reg',views.customer_reg),
    path('seller_reg',views.seller_reg),
    path('seller_login',views.seller_login, name='seller_login' ),
    path('email_exist',views.email_exist, name = 'email_exist'),
   
]