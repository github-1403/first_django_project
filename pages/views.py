from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'page_name': 'home'
    }
    return render(request, 'pages/home.html', context=context)


def about(request):
    context = {
        'page_name': 'about us'
    }
    return render(request, 'pages/about_us.html', context=context)


def contact(request):
    context = {
        'page_name': 'contact us'
    }
    return render(request, 'pages/contact_us.html', context=context)

