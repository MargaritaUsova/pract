import json

with open('/Users/margaritausova/Documents/pract/phone_prices.json') as f1:
    prices = json.load(f1)


with open('phones.html', 'a') as f:
    #print(prices['30067439']['item_base_price'])
    for i in prices:
        f.write("""    <h1>{price}</h1> <h2>{name}</h2><h3> )</h3>
        """.format(price=prices[i]['item_discount_price'],
                   name = prices[i]['item_name']))
    f.write("""</body>
    </html>""")





