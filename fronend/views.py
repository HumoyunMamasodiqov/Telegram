from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def bars(request):
    return render(request, 'bars.html')