from django.shortcuts import render
from .models import *


# Create your views here.


def home(request):
    partners = Partner.objects.all()
    print('partner', partners)
    city = City.objects.all()
    # print('city', city)
    context = {'partners': partners, 'city': city}
    return render(request, 'zotravo/Home.html', context)


def confirmation(request):
    context = {}
    return render(request, 'zotravo/confirmation.html')


def detailPage(request):
    context = {}
    return render(request, 'zotravo/detailPage.html')


def orderPage(request):
    return render(request, 'zotravo/orderPage.html')


def loginPage(request):
    return render(request, 'zotravo/login.html')


def vendorloginPage(request):
    return render(request, 'zotravo/vendorlogin.html')
