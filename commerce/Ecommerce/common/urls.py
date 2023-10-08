from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [

    path('commonhome',views.commonhome,name='commonhome'),
    path('customerlogin',views.customer_login, name='customer_login'),
    path('sellerlogin',views.seller_login,name='seller_login'),
    path('customer_reg',views.customer_reg,name='customer_reg'),
    path('seller_reg',views.seller_reg, name='seller_reg'),
]