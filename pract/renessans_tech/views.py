from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Task

from cart.forms  import CartAddProductForm


def product_detail(request, id, slug):
    product = get_object_or_404(Task,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'pract/renessans_tech/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
def index(request):
    return render(request, 'renessans_tech/index.html', {'title' : 'Главная страница сайта'})

def phones(request):
    return render(request, 'renessans_tech/phones1.html')

def basket(request):
    return render(request, 'renessans_tech/basket.html')

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

def computer_page(request):
    return render(request, 'renessans_tech/computer_page.html')
def tablet_page(request):
    return render(request, 'renessans_tech/tablet_page.html')

def accessories_page(request):
    return render(request, 'renessans_tech/accessories_page.html')

def about_us(request):
    return render(request, 'renessans_tech/about_us.html')

def popular_items(request):
    return render(request, 'renessans_tech/popular_items.html')


