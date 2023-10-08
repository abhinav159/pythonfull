from django.urls import path
from . import views

app_name = 'seller'
urlpatterns = [
    path('addproduct',views.addproduct),
    path('change_pass',views.change_pass),
    path('product_catalog',views.product_catalog),
    path('sellerhome',views.sellerhome,name='sellerhome'),
    path('update_product',views.update_product),
]
