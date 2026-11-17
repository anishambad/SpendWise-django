from django.http import HttpResponse 
from django.shortcuts import render


def home(request):
    context={
    'app_name' : 'SpendWise',
    'tagline' : 'Track every rupee , see where it goes. ',
    'year' : 2026,  
    }
    
    return render(request , 'core/home.html' , context)

def about(request) :
    return render(request , 'core/about.html')