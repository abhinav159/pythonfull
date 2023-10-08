from django.urls import path
from . import views

app_name = 'seller'
urlpatterns = [

    path('seller_signup',views.seller_signup),
    path('product_catalog',views.product_catalog),
    path('seller_home',views.seller_home,name= "sellerhome"),
    path('seller_login',views.login, name = 'seller_login' ),
    path('addproduct',views.addproduct,name="addproduct" ),
    path('update_product',views.update_product,name='update_product' ),
    path('change_pass',views.change_pass, name = "change_pass" ),
    path('getstock',views.getstock, name = "get_stock" ),
    path('update_stock',views.update_stock, name = "update_stock" ),
   
]