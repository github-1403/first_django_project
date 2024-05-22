from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about_us.html')


def contact(request):
    return render(request, 'pages/contact_us.html')

