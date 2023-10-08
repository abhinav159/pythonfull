from django.urls import path
from . import views
app_name = 'customer'
urlpatterns = [
    path('customer_home',views.customer_home, name = 'customer_home'),
    path('product_details/<int:pid>',views.product_details, name='product_details'),
    path('change_password',views.change_password,name='change_pass'),
    path('my_cart',views.my_cart,name='mycart'),
    path('my_order',views.my_order),
    path('profile',views.profile, name='profile'),
    path('remove_item/<int:pid> ',views.remove_item, name = 'remove_item'),
    path('logout',views.logout, name = 'logout'),

]