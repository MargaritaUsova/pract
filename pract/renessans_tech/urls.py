from django.urls import path
from . import views
import json

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about-us', views.about, name = 'about'),
    path('phones', views.phones),
    path('laptops', views.laptops),
    path('appliances', views.byt_techn),
    path('computers', views.computers),
    path('tablets', views.tablets),
    path('accessories', views.accessories),
    path('basket', views.basket),

]

with open('/Users/margaritausova/Documents/pract/phone_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'phones/{prices[i]["nameTranslit"]}', views.phone_page),)


with open('/Users/margaritausova/Documents/pract/laptop_prices.json') as f1:
    prices = json.load(f1)
    for i in prices:
        urlpatterns.append(path(f'laptops/{prices[i]["nameTranslit"]}', views.laptop_page),)