from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Task
def index(request):
    return render(request, 'renessans_tech/index.html', {'title' : 'Главная страница сайта'})

def about(request):
    return render(request, 'renessans_tech/about.html')


def phones(request):
    return render(request, 'renessans_tech/phones1.html')

def laptops(request):
    return render(request, 'renessans_tech/laptops.html')

def tv(request):
    return render(request, 'renessans_tech/tv.html')

def computers(request):
    return render(request, 'renessans_tech/computers.html')

def tablets(request):
    return render(request, 'renessans_tech/tablets.html')

def accessories(request):
    return render(request, 'renessans_tech/accessories.html')

def basket(request):
    return render(request, 'renessans_tech/basket.html')

def phone_page(request):
    return render(request, 'renessans_tech/phone_page1.html')

def laptop_page(request):
    return render(request, 'renessans_tech/laptop_page.html')

def tv_page(request):
    return render(request, 'renessans_tech/tv_page.html')


