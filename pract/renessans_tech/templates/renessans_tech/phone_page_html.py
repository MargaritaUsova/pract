import json
import math
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
  <title>Смартфоны</title>
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
            <img id="item-photo-1" class="item-photo" src="{% static 'pictures/test-1.avif' %}" style="width:100%">
          </div>

          <div class="mySlides fade">
            <img id="item-photo-2" class="item-photo " src="{% static 'pictures/test-2.avif' %}" style="width:100%">
          </div>

          <div class="mySlides fade">
            <img id="item-photo-3" class="item-photo " src="{% static 'pictures/test-3.avif' %}" style="width:100%">
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

          function plusSlides(n) {
            showSlides(slideIndex += n);
          }

          function currentSlide(n) {
            showSlides(slideIndex = n);
          }

          function showSlides(n) {
            var i;
            var slides = document.getElementsByClassName("mySlides");
            var dots = document.getElementsByClassName("dot");
            if (n > slides.length) {slideIndex = 1}
            if (n < 1) {slideIndex = slides.length}
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            for (i = 0; i < dots.length; i++) {
                dots[i].className = dots[i].className.replace(" active", "");
            }
            slides[slideIndex-1].style.display = "block";
            dots[slideIndex-1].className += " active";
          }
          </script>
        <p id = "cashback_calculate" class="cashback-text" data-tooltip="Купите этот товар с кэшбеком {calculate}">Кэшбек 10%</p>
      </div>
      <div class="item-info">
        <p id="item-name" class="item-name">
          Смартфон Apple iPhone 14 Pro Max 128GB nanoSim/eSim Deep Purple
        </p>
        <p style="font-weight: bold;">
          Характеристики:
        </p>
        <ul>
          <li class="feature-1">Экран: <span id="feature-info-1" class="text-highligt">6.1"/2556x1179 Пикс</span></li>
          <li class="feature-2">Технология экрана: <span id="feature-info-2" class="text-highligt">OLED</span></li>
          <li class="feature-3">Тип процессора: <span id="feature-info-3" class="text-highligt">A16 Bionic</span></li>
          <li class="feature-4">Встроенная память (ROM) <span id="feature-info-4" class="text-highligt">128 ГБ</span></li>
          <li class="feature-5">Основная камера: МПикс <span id="feature-info-5" class="text-highligt">48/12/12</span></li>
          <li class="feature-6">Фронтальная камера МПикс: <span id="feature-info-6" class="text-highligt">лялллляя</span></li>
          <li class="feature-7">Оперативная память (RAM): <span id="feature-info-7" class="text-highligt">128 ГБ</span></li>
          <li class="feature-8">Процессор: <span id="feature-info-8" class="text-highligt">48/12/12</span></li>
        </ul>
        <a style="color:#ff0078;" href = "https://www.mvideo.ru/products/smartfon-apple-iphone-14-pro-max-128gb-nanosim-esim-deep-purple-30064939">
          Подробнее на сайте М.Видео
        </a>
      </div>
      <div class="item-price-container">
        <p id="item-current-price" class="item-current-price">
          103 999 ₽
        </p>
        <p id="item-previous-price" class="item-previous-price">
          119 999
        </p>
        <button class="add-to-cart" onclick="this.className='in-cart-btn'"></button> <br>
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
      document.getElementById("feature-info-1").innerHTML = "{screen}";
      document.getElementById("item-current-price").innerHTML = "{price}";
      document.getElementById("item-previous-price").innerHTML = "{old_price}";
      document.getElementById("feature-info-2").innerHTML = "{techn_screen}";
      document.getElementById("feature-info-3").innerHTML = "{proc_type}";
      document.getElementById("feature-info-4").innerHTML = "{rom}";
      document.getElementById("feature-info-5").innerHTML = "{osn_cam}";
      document.getElementById("feature-info-6").innerHTML = "{front_cam}";
      document.getElementById("feature-info-7").innerHTML = "{ram}";
      document.getElementById("feature-info-8").innerHTML = "{proc}";
      document.getElementById("item-photo-1").src = "{{% static '{photo1}' %}}";
      document.getElementById("item-photo-2").src = "{{% static '{photo2}' %}}";
      document.getElementById("item-photo-3").src = "{{% static '{photo3}' %}}";
      document.getElementById("cashback_calculate").setAttribute('data-tooltip', '{calculate}');
      
      }}
            """.format(link=prices[i]['nameTranslit'],
                        name = prices[i]['item_name'],
                       screen = prices[i]['Экран'],
                        price = str(prices[i]['item_discount_price']) + ' ₽',
                        old_price = str(prices[i]['item_base_price']) + ' ₽',
                       techn_screen = prices[i]['Технология экрана'],
                       proc_type = prices[i]['Тип процессора'],
                       rom = prices[i]['Встроенная память (ROM)'],
                       osn_cam = prices[i]['Основная камера МПикс'],
                       front_cam = prices[i]['Фронтальная камера МПик'],
                       ram = prices[i]['Оперативная память (RAM)'],
                       proc = prices[i]['Процессор'],
                       photo1 = f'pictures/phones/img1/{i}.AVIF',
                       photo2 = f'pictures/phones/img2/{i}.AVIF',
                       photo3 = f'pictures/phones/img3/{i}.AVIF',
                       calculate = 'Купите этот товар и получите кэшбек ' + str(math.floor(int(prices[i]['item_cashback'][:-1])
                                                                                           * prices[i]['item_discount_price'] / 100)) + ' ₽'

                       ))
    f.write("""
    </script>
<footer class="footer">
      <div class="container">
        <div class="row">
          <div class="footer-col">
            <h4>Сервис</h4>
            <ul>
              <li><a href="/about_us">О нас</a></li>
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
  </html>
    """
    )