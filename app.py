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

class workers:
    name = ""
    job = ""
    salary = ""

    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

class Foods:
    name = ""
    price = 0
    quantity = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = int(price)
        self.quantity = int(quantity)

class Rooms:
    typeRoom = ""
    priceRoom = 0
    totalRooms = 0
    bookRooms = 0
    startingRoom = 0

    def __init__(self, typeR, priceR, totalR, book, sRoom):
        self.typeRoom = typeR
        self.priceRoom = priceR
        self.totalRooms = totalR
        self.bookRooms = book+sRoom
        self.startingRoom = sRoom

id_list = []
worker_List = []
sms_List = []
complains = []
food_List = []
room_List = []
MyEmail = ""
MyPin = ""
MyName = ""
MyObject = ""
managerEmail = ""
managerName = ""
managerPin = ""
ownerEmail = ""
ownerName = ""
ownerPin = ""

# Save Data of All Residents

def saveData():
    global id_list
    file_path = path+'/data/data.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for id in id_list:
        record = id.name+","+id.email+","+id.pin+"," + \
            str(id.roomNo)+","+id.roomType+","+str(id.expenditures)
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Save Data of Manager


def saveDataManager():
    global managerEmail
    global managerName
    global managerPin
    file_path = path+'/data/dataManager.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    record = managerName+","+managerEmail+","+managerPin
    myfile = open(file_path, 'a')
    print(record, file=myfile, sep="\n")
    myfile.close()

# Save Data of Owner


def saveDataOwner():
    global ownerEmail
    global ownerName
    global ownerPin
    file_path = path+'/data/dataOwner.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    record = ownerName+","+ownerEmail+","+ownerPin
    myfile = open(file_path, 'a')
    print(record, file=myfile, sep="\n")
    myfile.close()

# Save Messages


def saveSms():
    global sms_List
    file_path = path+'/data/messages.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for sms in sms_List:
        record = sms
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Save Complains


def saveComplains():
    global complains
    file_path = path+'/data/complains.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for complain in complains:
        record = complain
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Save Worker Data


def saveWorkerData():
    global worker_List
    file_path = path+'/data/workers.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for worker in worker_List:
        record = worker.name+","+worker.job+","+worker.salary
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Save Data of All Foods


def saveDataFood():
    global food_List
    file_path = path+'/data/foods.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for food in food_List:
        record = food.name+","+str(food.price)+","+str(food.quantity)
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Save Data of All Rooms


def saveDataRooms():
    global room_List
    file_path = path+'/data/rooms.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for room in room_List:
        record = room.typeRoom+","+str(room.priceRoom)+","+str(
            room.totalRooms)+","+str(room.bookRooms)+","+str(room.startingRoom)
        myfile = open(file_path, 'a')
        print(record, file=myfile, sep="\n")
    myfile.close()

# Save Data of All Ordered Foods


def saveOrerdedFoods():
    global id_list
    file_path = path+'/data/orderedProducts.txt'
    myfile = open(file_path, 'w')
    myfile.close()
    for myid in id_list:
        orderlistfoods = []
        orderlistfoods = myid.myOrderedFoods
        for myfood in orderlistfoods:
            record = myfood.namefood+"," + \
                str(myfood.quantity)+","+str(myfood.price) + \
                ","+myid.name+","+str(myid.pin)
            myfile = open(file_path, 'a')
            print(record, file=myfile, sep="\n")
    myfile.close()

@app.route("/")