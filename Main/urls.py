from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_contracts', views.all_contracts, name='all_contracts'),
    path('close/<int:contract_id>/', views.close_contract, name='close_contract'),
    path('add-contract/', views.add_contract, name='add_contract'),
]
