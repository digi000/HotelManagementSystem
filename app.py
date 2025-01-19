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

# Load Data of All Residents


def loaddata():
    file_path = path+'/data/data.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        name = ""
        email = ""
        password = ""
        roomno = ""
        roomtype = ""
        expen = ""
        i = 0
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            email = email + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            password = password + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            roomno = roomno + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            roomtype = roomtype + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            expen = expen + record[x]
        person = Id(name, email, password, int(roomno), roomtype, int(expen))
        id_list.append(person)

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

# Load Data of Manager


def loaddataManager():
    global managerName
    global managerEmail
    global managerPin
    file_path = path+'/data/dataManager.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    name = ""
    email = ""
    password = ""
    i = 0
    for record in records:
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            email = email + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            password = password + record[x]
    managerName = name
    managerEmail = email
    managerPin = password


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

# Load Data of Owner


def loaddataOwner():
    global ownerName
    global ownerEmail
    global ownerPin
    file_path = path+'/data/dataOwner.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    name = ""
    email = ""
    password = ""
    i = 0
    for record in records:
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            email = email + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            password = password + record[x]
    ownerName = name
    ownerEmail = email
    ownerPin = password

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

def loadSms():
    file_path = path+'/data/messages.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        if record != "":
            sms_List.append(record)

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

def loadComplains():
    file_path = path+'/data/complains.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        if record != "":
            complains.append(record)

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

def loadWokerData():
    global worker_List
    file_path = path+'/data/workers.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        name = ""
        job = ""
        salary = ""
        i = 0
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            job = job + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            salary = salary + record[x]
        worker = workers(name, job, salary)
        worker_List.append(worker)

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

# Load Data of All Foods


def loadfoodData():
    file_path = path+'/data/foods.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        name = ""
        price = ""
        quantity = ""
        i = 0
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            price = price + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            quantity = quantity + record[x]
        food = Foods(name, price, quantity)
        food_List.append(food)

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

# Load Data of All Rooms


def loaddataRooms():
    file_path = path+'/data/rooms.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        typeR = ""
        priceR = ""
        totalR = ""
        bookR = ""
        startingR = ""
        i = 0
        while(record[i] != ","):
            typeR = typeR + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            priceR = priceR + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            totalR = totalR + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            bookR = bookR + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            startingR = startingR + record[x]
        room = Rooms(typeR, int(priceR), int(
            totalR), int(bookR), int(startingR))
        room_List.append(room)

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

# Load Data of All Ordered Foods


def loadOrderedFoods():
    global id_list
    file_path = path+'/data/orderedProducts.txt'
    myfile = open(file_path, 'r')
    records = myfile.read().splitlines()
    for record in records:
        namef = ""
        quantityf = ""
        pricef = ""
        name = ""
        pin = ""
        i = 0
        while(record[i] != ","):
            namef = namef + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            quantityf = quantityf + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            pricef = pricef + record[i]
            i = i+1
        i = i+1
        while(record[i] != ","):
            name = name + record[i]
            i = i+1
        i = i+1
        for x in range(i, len(record)):
            pin = pin + record[x]
        for myid in id_list:
            if(myid.name == name and myid.pin == pin):
                myid.addOrderedFood(namef, quantityf, pricef)


@app.route("/")
def Page():
    return render_template("mainLoginPage.html")

# Owner Pages

@app.route("/loginowner")
def login1():
    return render_template("Owner/loginOwner.html")

@app.route("/ownerhome")
def owner():
    return render_template("Owner/owner.html", variable=ownerEmail, residents=len(id_list), workers=len(worker_List), totalincome=totalexpenditures(), totalsalary=totalsalaries())

@app.route("/sendMessage")
def sendMessageManager():
    global ownerEmail
    return render_template("Owner/sendMessageToManager.html", variable=ownerEmail)


@app.route("/recieveMessage")
def recieveMessageManager():
    global sms_List
    return render_template("Owner/recieveMessageOwner.html", variable=ownerEmail, smsList=sms_List)


@app.route("/profileowner")
def profile1():
    return render_template("Owner/profileOwner.html", email=ownerEmail, name=ownerName, pin=ownerPin)

@app.route("/profilemanager")
def profile2():
    return render_template("Manager/profileManager.html", email=managerEmail, name=managerName, pin=managerPin)

@app.route("/loginmanager")
def login2():
    return render_template("Manager/loginManager.html")

@app.route("/managerhome")
def manager():
    return render_template("Manager/manager.html", variable=managerEmail,totalresidents=len(id_list),totalworkers=len(worker_List),totalfoods=len(food_List),types=len(room_List))

@app.route("/sendMessageManager")
def sendMessageOwner():
    return render_template("Manager/sendMessageToOwner.html", variable=managerEmail)

@app.route("/recieveMessageManager")
def recieveMessageMYManager():
    return render_template("Manager/recieveMessageManager.html", variable=managerEmail, smsList=sms_List)


@app.route("/createAccountresident")
def Account():
    return render_template("Manager/registerResident.html")


@app.route("/registerResident", methods=['POST', 'GET'])
def createAcoount():
    name = request.form['name1']+" "+request.form['name2']
    email = request.form['email']
    pin = request.form['password']
    person = Id(name, email, pin, 0, "None", 0)
    id_list.append(person)
    saveData()
    return render_template("Manager/manager.html", variable=managerEmail,totalresidents=len(id_list),totalworkers=len(worker_List),totalfoods=len(food_List),types=len(room_List))


@app.route("/login")
def residentLogin():
    return render_template("Resident/loginResident.html")

@app.route("/profileresident")
def profile3():
    return render_template("Resident/profileResident.html", email=MyEmail, name=MyName, pin=MyPin)

@app.route("/resident")
def resident():
    global MyObject
    yourcomplains = calculatecomplains()
    return render_template("Resident/resident.html", variable=MyEmail, roomtype=MyObject.roomType, roomno=MyObject.roomNo, expen=MyObject.expenditures, yourcomplains=yourcomplains)

@app.route("/deleteResident",methods=['POST','GET'])
def delete1():
    if request.method=="POST":
        index=request.form['myindex']
        index=int(index)-1
        id_list.pop(index)
        saveData()
    return render_template("Manager/residentDetail.html", variable=managerEmail, My_List=id_list)
