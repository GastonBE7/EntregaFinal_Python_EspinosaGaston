from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={})

def creator(request):
    return render(request, 'creator.html', context={})