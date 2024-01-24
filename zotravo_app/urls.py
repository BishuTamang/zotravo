# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('confirmation/', views.confirmation, name='Confirmation'),
    path('detailPage/', views.detailPage, name='detailPage'),
    path('orderPage/', views.orderPage, name='orderPage'),
    path('loginPage/', views.loginPage, name='loginPage'),
]