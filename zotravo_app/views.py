from django.shortcuts import render

# Create your views here.

def home(request):
   context = {}
   return render (request, 'zotravo/Home.html')

def confirmation(request):
   context = {}
   return render (request, 'zotravo/confirmation.html')

def detailPage(request):
   context = {}
   return render (request, 'zotravo/detailPage.html')

def orderPage(request):
   context = {}
   return render (request, 'zotravo/orderPage.html') 
   
def loginPage(request):
   context = {}
   return render (request, 'zotravo/login.html') 

