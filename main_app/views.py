from datetime import datetime

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def services(request):
    our_services = ["Bush Camps", "Hikes", "Swimming"]
    price = 1000
    date  = '6-11-2024'
    return render(request, 'services.html',
       {"services":services, 'price':price, 'date':date})


def about(request):
    return render(request,'about.html')