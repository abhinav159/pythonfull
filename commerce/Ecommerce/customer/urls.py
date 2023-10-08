from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('change_pass',views.change_pass, name='change_pass'),
    path('profile',views.profile,name='profile'),
    path('product_details',views.product_details, name='product_details'),
    path('my_cart',views.my_cart,name='my_cart'),
    path('my_order',views.my_order,name='my_order'),
    path('customer_home',views.customer_home,name='customer_home'),
]
