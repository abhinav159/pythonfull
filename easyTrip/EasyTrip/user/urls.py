from django.urls import path
from . import views

urlpatterns=[
    path('homepage',views.homepage),
    path('village',views.village),
    path('calculator',views.calculator),
    path('login',views.login),
    path('dom',views.dom),
    path('jquery',views.jquery)
]