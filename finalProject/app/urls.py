from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('spreadsheet/', views.spreadsheet, name='spreadsheet'),
    path('bonus/', views.bonus, name='maps'),
    path('get_api/', views.get_api, name='live'),
    path('get_id/', views.get_api, name='live'),
    path('get_id/<int:item_id>/', views.get_id, name='live'),
]
