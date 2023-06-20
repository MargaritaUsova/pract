import json

with open('C:/Users/Пользователь/PycharmProjects/pract/phones_data.json') as f:
    templates = json.load(f)

with open('phones.html', 'a') as f:

    for i in templates:
        f.write("""    <div class="item-box">
    <div class="item-photo-container">
      <img class="item-photo" src="{% static 'pictures/test-img.jpg' %}">
      <p class="cashback-text" data-tooltip="Купите этот товар с кэшбэком 15%">Кэшбек 15%</p>
    </div>
    <div class="item-info">
      <p class="item-name">
        {name}}
      </p>
      <ul>
        <li>Экран: <span class="text-highligt">6.1"/2556x1179 Пикс</span></li>
        <li>Технология экрана: <span class="text-highligt">OLED</span></li>
        <li>Тип процессора: <span class="text-highligt">A16 Bionic</span></li>
        <li>Встроенная память (ROM) <span class="text-highligt">128 ГБ</span></li>
        <li>Основная камера МПикс <span class="text-highligt">48/12/12</span></li>
      </ul>
    </div>
    <div class="item-price-container">
      <p class="item-current-price">
        103 999 ₽
      </p>
      <p class="item-previous-price">
        119 999
      </p>
      <button class="add-to-cart">В корзину</button> <br>
      <button class="credit-btn">Купить в кредит</button>
    </div>
  </div>
        """.format(name=templates[i]['item_name']))
    f.write("""</body>
    </html>""")




