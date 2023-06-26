import json

def toCart(name):
    pass

def deleteFromCart(name):
    pass

def showCart():
    with open("/Users/margaritausova/Documents/pract/items_in_cart.json") as file:
        items = json.load(file)
        for i in items:
            return i
