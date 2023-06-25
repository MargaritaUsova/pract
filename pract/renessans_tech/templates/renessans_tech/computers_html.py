import json
from django.urls import reverse

with open('/Users/margaritausova/Documents/pract/computers_prices.json') as f1:
    prices = json.load(f1)

with open('computers.html', 'w') as f:
    f.write("""
    <!DOCTYPE html>
{% load static %}
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Компьютеры</title>
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
        <a style="color: #ff0078;"class="cathegory-items" href = 'computers'>
          Компьютеры
        </a>
        <a class="cathegory-items" href = 'tablets'>
          Планшеты
        </a>
        <a class="cathegory-items" href = 'accessories'>
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
    <a href="computers/{nameTranslit}">
        <img class="item-photo" src="{{% static 'pictures/computers/{image}.jpg' %}}">
      </a>
      <p class="cashback-text" data-tooltip="Купите этот товар с кэшбеком {cashback}">Кэшбек {cashback}</p>
    </div>
    <div class="item-info">
    <a href=computers/{nameTranslit}>
        <p class="item-name">
            {name}
        </p>
      </a>
      <ul>
        <li>Бренд: <span class="text-highligt">{brand}</span></li>
        <li>Диагональ/разрешение: <span class="text-highligt">{screen}"</span></li>
        <li>Тип процессора: <span class="text-highligt">{proc}</span></li>
        <li>Оперативная память (RAM): <span class="text-highligt">{ram}</span></li>
        <li>Графический контроллер: <span class="text-highligt">{controller}</span></li>

        <li>Объем SSD <span class="text-highligt">{ssd}</span></li>
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
                   screen=prices[i]['Диагональ/разрешение'],
                   brand=prices[i]['brand'],
                   proc=prices[i]['Тип процессора'],
                   controller = prices[i]['Графический контроллер'],
                   ram=prices[i]['Оперативная память (RAM)'],
                   cur_price=prices[i]['item_discount_price'],
                   previous_price=prices[i]['item_base_price'],
                   nameTranslit=prices[i]['nameTranslit'],
                   ssd = prices[i]['Объем SSD'],
                   image=i
                   ))
    f.write("""
    <footer class="footer">
      <div class="container">
        <div class="row">
          <div class="footer-col">
            <h4>Сервис</h4>
            <ul>
              <li><a href="about_us">О нас</a></li>
              <li><a href="https://rencredit.ru/about/">О банке</a></li>
              <li><a href="https://rencredit.ru/addresses/">Отделения и банкоматы</a></li>
              <li><a href="https://rencredit.ru/services/">Сервисы и услуги</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Помощь</h4>
            <ul>
              <li><a href="https://rencredit.ru/support/faq/">Поддержка клиентов</a></li>
              <li><a href="https://rencredit.ru/support/appeals/">Обратная связь</a></li>
              <li><a href="https://rencredit.ru/doc/support/forms/formy-tipovykh-spravok/">Форма справок и документов</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Услуги</h4>
            <ul>
              <li><a href="https://rencredit.ru/loans/">Кредиты</a></li>
              <li><a href="https://rencredit.ru/cards/">Карты</a></li>
              <li><a href="https://rencredit.ru/deposits/">Вклады</a></li>
              <li><a href="https://rencredit.ru/investments/">Инвестиции</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Контакты</h4>
            <div class="contact-info">
            <ul>
              <p style="color: #bbbbbb; font-size: 12px;">круглосуточно, бесплатно по России</p>
              <li><a href="#">8 800 200-0-981</a></li>
              <p style="color: #bbbbbb; font-size: 12px;">Номер может использоваться для исходящих вызовов</p>
              <li><a href="#">8 495 783-46-23</a></li>
            </ul>
            </div>
          </div>
        </div>
      </div>
   </footer>
    </body>
    </html>""")
