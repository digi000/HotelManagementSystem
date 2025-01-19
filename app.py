from flask import Flask
app = Flask(__name__)

class Id:
    name = ""
    email = ""
    pin = ""
    roomNo = 0
    roomType = ""
    expenditures = 0
    myOrderedFoods = []

    def __init__(self, nameR, emailR, pinR, no, typeRoom, expen):
        self.name = nameR
        self.email = emailR
        self.pin = pinR
        self.roomNo = no
        self.roomType = typeRoom
        self.expenditures = expen
        self.myOrderedFoods = []

    def addOrderedFood(self, name, quantity, price):
        orderfood = OrderedFoods(name, int(quantity), int(price))
        self.myOrderedFoods.append(orderfood)

class OrderedFoods:
    namefood = ""
    quantity = 0
    price = 0

    def __init__(self, name, quantity, price):
        self.namefood = name
        self.quantity = quantity
        self.price = price
        
@app.route("/")