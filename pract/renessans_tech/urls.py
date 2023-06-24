from django.urls import path
from . import views
import json

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

]

with open('/Users/margaritausova/Documents/pract/phone_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'phones/{prices[i]["nameTranslit"]}', views.phone_page),)


with open('/Users/margaritausova/Documents/pract/laptop_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'laptops/{prices[i]["nameTranslit"]}', views.laptop_page),)

with open('/Users/margaritausova/Documents/pract/tv_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'tv/{prices[i]["nameTranslit"]}', views.tv_page),)

with open('/Users/margaritausova/Documents/pract/computers_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'computers/{prices[i]["nameTranslit"]}', views.computer_page),)

with open('/Users/margaritausova/Documents/pract/tablets_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'tablets/{prices[i]["nameTranslit"]}', views.tablet_page),)

with open('/Users/margaritausova/Documents/pract/accessories_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'accessories/{prices[i]["nameTranslit"]}', views.accessories_page),)


