from django.urls import path
from . import views
import json
from django.conf import settings
from django.conf.urls.static import static
from cart.views import cart_add, cart, checkout

urlpatterns = [
    path('', views.index, name = 'index'),
    path('phones', views.phones),
    path('laptops', views.laptops),
    path('tv', views.tv),
    path('computers', views.computers),
    path('tablets', views.tablets),
    path('accessories', views.accessories),
    path('basket', views.basket),
    path('about_us', views.about_us),
    path('popular_items', views.popular_items),
    path('cart_add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/', cart, name='cart'),
    path('cart/checkout', checkout),
]

with open('/Users/margaritausova/Documents/6сем/pract/phone_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'phones/{prices[i]["nameTranslit"]}', views.phone_page),)


with open('/Users/margaritausova/Documents/6сем/pract/laptop_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'laptops/{prices[i]["nameTranslit"]}', views.laptop_page),)

with open('/Users/margaritausova/Documents/6сем/pract/tv_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'tv/{prices[i]["nameTranslit"]}', views.tv_page),)

with open('/Users/margaritausova/Documents/6сем/pract/computers_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'computers/{prices[i]["nameTranslit"]}', views.computer_page),)

with open('/Users/margaritausova/Documents/6сем/pract/tablets_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'tablets/{prices[i]["nameTranslit"]}', views.tablet_page),)

with open('/Users/margaritausova/Documents/6сем/pract/accessories_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'accessories/{prices[i]["nameTranslit"]}', views.accessories_page),)


