from django.shortcuts import render
from .models import Odam

def index(request):
    odam = Odam.objects.all() 
    return render(request, 'index.html', {"odam": odam})

def bars(request):
    odam = Odam.objects.all() 

    return render(request, "bars.html", {"odam": odam})

def user(request):
    return render(request, 'user.html')
