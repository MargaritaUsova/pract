import json
from django.urls import reverse

with open('/Users/margaritausova/Documents/pract/accessories_prices.json') as f1:
    prices = json.load(f1)

with open('accessories.html', 'w') as f:
    f.write("""
    <!DOCTYPE html>
{% load static %}
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Аксессуары</title>
  <link rel="stylesheet" href="{% static 'css/phones.css' %}">
  <link rel="stylesheet" href="{% static 'css/header-footer.css' %}">
</head>
<body>
<header class="site-header">
      <div class="site-header-top">
        <div class="site-header-top-left">
          <img src="{% static 'pictures/city.svg' %}">
          <a>Москва</a>
        </div>
        <div class="site-header-top-middle">
          <a href="https://rencredit.ru/">Для жизни</a>
          <a href="https://rencredit.ru/sme/">Для бизнеса</a>
          <a href="https://rencredit.ru/about/">О банке</a>
          <a href="https://rencredit.ru/addresses/">Отделения и банкоматы</a>
        </div>
        <div class="site-header-top-right">
          <img src="{% static 'pictures/mobile-bank.svg' %}">
          <a href="https://rencredit.ru/services/mobile-bank/" style="padding-right: 15px;">Мобильный банк</a>
          <img src="{% static 'pictures/internet-bank.svg' %}">
          <a href="https://ib.rencredit.ru/#/login">Интернет-банк</a>
        </div>
      </div>

      <div class="site-header-bottom">
        <a href='/'>
          <img class="logo" src="{% static 'pictures/new_logo.svg' %}">
        </a>
        <a class="cathegory-items" href = 'phones'>
          Смартфоны
        </a>
        <a class="cathegory-items" href = 'laptops'>
          Ноутбуки
        </a>
        <a class="cathegory-items" href="tv">
          Телевизоры
        </a>
        <a class="cathegory-items" href = 'computers'>
          Компьютеры
        </a>
        <a class="cathegory-items" href = 'tablets'>
          Планшеты
        </a>
        <a style="color: #ff0078;"class="cathegory-items" href = 'accessories'>
          Аксессуары
        </a>
        <a class="cathegory-items">
          Поиск
        </a>
        <a class="shopping-cart" href = 'basket'>
          Корзина
        </a>
      </div>

    </header> <br>

    """)

    for i in prices:
        f.write("""     <div class="item-box">
    <div class="item-photo-container">
    <a href="accessories/{nameTranslit}">
        <img class="item-photo" src="{{% static 'pictures/accessories/{image}.jpg' %}}">
      </a>
      <p class="cashback-text" data-tooltip="Купите этот товар с кэшбэком {cashback}">Кэшбек {cashback}</p>
    </div>
    <div class="item-info">
    <a href=accessories/{nameTranslit}>
        <p class="item-name">
            {name}
        </p>
      </a>
      <ul>
        <li>Бренд: <span class="text-highligt">{brand}</span></li>
        <li>Подходит для: <span class="text-highligt">{suits}"</span></li>
        <li>Для моделей с диагональю экрана: <span class="text-highligt">{models}</span></li>
        <li>Тип корпуса: <span class="text-highligt">{type}</span></li>
        <li>Материал чехла: <span class="text-highligt">{material}</span></li>

      </ul>
    </div>
    <div class="item-price-container">
      <p class="item-current-price">
        {cur_price} ₽
      </p>
      <p class="item-previous-price">
        {previous_price}
      </p>
      <button class="add-to-cart">В корзину</button> <br>
      <a href = 'https://anketa.rencredit.ru/app/credit/site/#anketa'>
        <button class="credit-btn">Купить в кредит</button>
      </a>
    </div>
  </div>
        """.format(price=prices[i]['item_discount_price'],
                   name=prices[i]['item_name'],
                   cashback=prices[i]['item_cashback'],
                   suits=prices[i]['Подходит для'],
                   brand=prices[i]['brand'],
                   models=prices[i]['Для моделей с диагональю экрана'],
                   material = prices[i]['Материал чехла'],
                   type=prices[i]['Тип корпуса'],
                   cur_price=prices[i]['item_discount_price'],
                   previous_price=prices[i]['item_base_price'],
                   nameTranslit=prices[i]['nameTranslit'],
                   image=i
                   ))
    f.write("""</body>
    </html>""")
