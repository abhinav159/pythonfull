from django.urls import path
from . import views

app_name = "com_adm"
urlpatterns = [

    path('home',views.home),
    path('approve_seller',views.approve_seller, name = "approveseller"),
    path('view_seller',views.view_seller,name = "viewseller"),
    path('view_customer',views.view_customer,name = "viewcust"),
    path('projecthome',views.projecthome),
    path('approve_cust',views.approve_cust, name = "approvecust"),
    path('approve/<int:sid>', views.approve, name='approve'),
    path('remove/<int:sid>', views.remove, name='remove'),
]