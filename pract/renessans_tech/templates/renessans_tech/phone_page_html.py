import json
from django.urls import reverse
from django import template
from django.urls import reverse

register = template.Library()
@register.filter
def is_current_page(request, param):
    return reverse(request.path).view_name == param

with open('/Users/margaritausova/Documents/pract/phone_prices.json') as f1:
    prices = json.load(f1)

with open('phone_page1.html', 'w') as f:
    f.write("""
    <!DOCTYPE html>
{% load static %}
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title></title>
  <link rel="stylesheet" href="{% static 'css/phone_page.css' %}">
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
        <a style="color: #ff0078;" class="cathegory-items" href = '/phones'>
          Смартфоны
        </a>
        <a class="cathegory-items" href = '/laptops'>
          Ноутбуки
        </a>
        <a class="cathegory-items" href="/tv">
          Телевизоры
        </a>
        <a class="cathegory-items" href = '/computers'>
          Компьютеры
        </a>
        <a class="cathegory-items" href = '/tablets'>
          Планшеты
        </a>
        <a class="cathegory-items" href = '/accessories'>
          Аксессуары
        </a>
        <a class="cathegory-items">
          Поиск
        </a>
        <a class="shopping-cart" href = '/basket'>
          Корзина
        </a>
      </div>

    </header> <br>
    <div class="item-box">
      <div class="item-photo-container">
        <div class="slideshow-container">

          <div class="mySlides fade">
            <img class="item-photo" src="{% static 'pictures/test-1.avif' %}" style="width:100%">
          </div>

          <div class="mySlides fade">
            <img class="item-photo " src="{% static 'pictures/test-2.avif' %}" style="width:100%">
          </div>

          <div class="mySlides fade">
            <img class="item-photo " src="{% static 'pictures/test-3.avif' %}" style="width:100%">
          </div>

          <a class="prev" onclick="plusSlides(-1)">❮</a>
          <a class="next" onclick="plusSlides(1)">❯</a>

        </div>
          <br>

          <div style="text-align:center">
            <span class="dot" onclick="currentSlide(1)"></span>
            <span class="dot" onclick="currentSlide(2)"></span>
            <span class="dot" onclick="currentSlide(3)"></span>
          </div>

          <script>
          var slideIndex = 1;
          showSlides(slideIndex);

          function plusSlides(n) {{
            showSlides(slideIndex += n);
          }}

          function currentSlide(n) {{
            showSlides(slideIndex = n);
          }}

          function showSlides(n) {{
            var i;
            var slides = document.getElementsByClassName("mySlides");
            var dots = document.getElementsByClassName("dot");
            if (n > slides.length) {slideIndex = 1}}
            if (n < 1) {slideIndex = slides.length}}
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";
            }}
            for (i = 0; i < dots.length; i++) {{
                dots[i].className = dots[i].className.replace(" active", "");
            }}
            slides[slideIndex-1].style.display = "block";
            dots[slideIndex-1].className += " active";
          }}
          </script>
        <p class="cashback-text" data-tooltip="Купите этот товар с кэшбэком 10%">Кэшбек 10%</p>
      </div>
      <div class="item-info">
        <p id="item-name" class="item-name">
          Смартфон Apple iPhone 14 Pro Max 128GB nanoSim/eSim Deep Purple
        </p>
        <p style="font-weight: bold;">
          Характеристики:
        </p>
        <ul>
          <li id="feature-1" class="feature-1">Экран: <p id="feature-1" class="text-highligt">6.1"/2556x1179 Пикс</p></li>
          <li class="feature-2">Технология экрана: <span class="text-highligt">OLED</span></li>
          <li class="feature-3">Тип процессора: <span class="text-highligt">A16 Bionic</span></li>
          <li class="feature-4">Встроенная память (ROM) <span class="text-highligt">128 ГБ</span></li>
          <li class="feature-5">Основная камера МПикс <span class="text-highligt">48/12/12</span></li>
        </ul>
        <a style="color:#ff0078;" href = "https://www.mvideo.ru/products/smartfon-apple-iphone-14-pro-max-128gb-nanosim-esim-deep-purple-30064939">
          Подробнее на сайте М.Видео
        </a>
      </div>
      <div class="item-price-container">
        <p class="item-current-price">
          103 999 ₽
        </p>
        <p class="item-previous-price">
          119 999
        </p>
        <button class="add-to-cart">В корзину</button> <br>
        <a href = 'https://anketa.rencredit.ru/app/credit/site/#anketa'>
          <button class="credit-btn">Купить в кредит</button>
        </a>
      </div>
    </div>

  <script>
    const currentUrl = window.location.href;
    """
    )
    for i in prices:
        f.write("""
    if (currentUrl == "http://127.0.0.1:8000/phones/{link}"){{
      document.getElementById("item-name").innerHTML = "{name}";
      document.getElementById("feature-1").innerHTML = "{screen}";
      
      }}
      
    
            """.format(link=prices[i]['nameTranslit'],
                        name = prices[i]['item_name'],
                       screen = prices[i]['Экран']
                       ))
    f.write("""
    </script>

  </body>
  </html>
    """
    )