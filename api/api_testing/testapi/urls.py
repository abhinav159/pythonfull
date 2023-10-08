from django.urls import path
from . import views

urlpatterns = [
    path('load_user',views.load_user),
    path('add_user',views.add_user),
    path('update_user/<int:user_id>',views.update_user),
    path('delete_user/<int:user_id>',views.delete_user),
    path('index',views.index, name='index'),
    path('floa',views.floa, name='floa'),
]