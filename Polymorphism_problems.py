"""Level 1: Basic Polymorphism """
"""Beginner """
"""Q1. Animal Sound (Method Overriding) 
Create a parent class Animal with a method sound(). Create child classes Dog, Cat, and Cow that 
override the sound() method. 
Expected output: 
Dog barks 
Cat meows 
Cow moos """

from email.mime import audio


class animal:
    def sound(self):
        print("Animals makes a sound")
class Dog(animal):
    def sound(self):
        print("Dog barks")
class Cat(animal):
    def sound(self):
        print("Cat meows")
class Cow(animal):
    def sound(self):
        print("Cow moos")

Animal=animal()
Animal.sound()
dog=Dog()
dog.sound()
cat=Cat()
cat.sound()
cow=Cow()
cow.sound()

"""output:---
Animals makes a sound
Dog barks
Cat meows
Cow moos
"""

"""Q2. Payment System 
Create a parent class Payment with a method pay(). Create child classes UPI, CreditCard, and 
Cash. Each class should implement its own pay() method. 
Expected output: 
Payment through UPI 
Payment through Credit Card 
Payment through Cash """

class payment:
    def pay(self):
        print("Make diferent payment methods")
class UPI(payment):
    def pay(self):
        print("Payment through UPI")
class Credit_card(payment):
    def pay(self):
        print("Payment through Credit Card")
class Cash(payment):
    def pay(self):
        print("Payment through Cash")

p1=payment()
p1.pay()
p2=UPI()
p2.pay()
p3=Credit_card()
p3.pay()
p4=Cash()
p4.pay()

"""output:--
Make diferent payment methods
Payment through UPI
Payment through Credit Card
Payment through Cash
"""

"""Q3. Employee Salary 
Create a parent class Employee with a method calculate_salary(). Create child classes 
FullTimeEmployee and PartTimeEmployee. 
• Full-time salary = monthly salary 
• Part-time salary = working hours × hourly rate 
Display the salary for each employee. """

class Employee:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Employee Name:",self.name)
class FullTimeEmployee(Employee):
    def __init__(self, name,monthly_salary):
        super().__init__(name)
        self.monthly_salary=monthly_salary

    def calculate_salary(self):
        self.display()
        print("Full-time salary:",self.monthly_salary)

class PartTimeEmployee(Employee):
    def __init__(self, name,working_hours,salary_per_hour):
        super().__init__(name)
        self.working_hours=working_hours
        self.salary_for_hour=salary_per_hour

    def calculate_salary(self):
        self.display()
        print("Part-time salary:",self.working_hours*self.salary_for_hour)

employ=[FullTimeEmployee("Gnaneshwar",50000),PartTimeEmployee("rajeshwari",200,5)]
for salary in employ:
    salary.calculate_salary()     

"""Output:-----
Employee Name: Gnaneshwar
Full-time salary: 50000
Employee Name: rajeshwari
Part-time salary: 1000
"""

"""Q4. Shape Area 
Create a parent class Shape with an area() method. Create child classes Circle, Rectangle, and 
Square. 
Calculate and display the area of each shape using method overriding. """

class shape:
    def area(self):
        print("Area of Shape")

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_circle = 3.14 * (self.radius ** 2)
        print("Area of Circle:", area_circle)

class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area_rectangle = self.length * self.width
        print("Area of Rectangle:", area_rectangle)

class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        area_square = self.side * self.side
        print("Area of Square:", area_square)

Area = [circle(10),Rectangle(10, 15),square(50)]

for area in Area:
    area.area()

"""output:---
Area of Circle: 314.0
Area of Rectangle: 150
Area of Square: 2500
"""


"""Q5. Vehicle Information 
Create a parent class Vehicle with a method start(). Create child classes Car, Bike, and Bus, each 
with a different implementation of start(). 
Use a loop to call the method for all objects. """

class Vehicle:
    def start(self):
        print("Vehicle will be start")

class Car(Vehicle):
    def start(self):
        print("Car start with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with a key")

Vehicles=[Car(),Bike(),Bus()]
for vehicle in Vehicles:
    vehicle.start()

"""output:---
Car start with key
Bike starts with a self-start button
Bus starts with a key
"""


"""Level 2: Intermediate Polymorphism Intermediate """

"""Q6. Method Overloading Using Default Arguments 
Create a class Calculator with a method add() that accepts two or three numbers and returns 
their sum. 
Expected output: 
15 
30 
60 """

class Calculator:
    def add(self,a,b,c=0):
        print("Total:",a+b+c)

Calculator=Calculator()
Calculator.add(10,20)
Calculator.add(41,89)
Calculator.add(78,96)

"""output:---
Total: 30
Total: 130
Total: 174
"""


"""Q7. Duck Typing – Notification System 
Create three unrelated classes: EmailNotification, SMSNotification, and WhatsAppNotification. 
Each class should have a send() method. 
Create a function notify_user() that accepts any object and calls its send() method."""

class notification:
    def send(self):
        print("Notification")

class EmailNotification(notification):
    def send(self):
        print("EmailNotification")

class SMSNotification(notification):
    def send(self):
        print("SMSNotification")

class WhatsAppNotification(notification):
    def send(self):
        print("WhatsAppNotification")

def notify_user():
    notify_user.send()

a=EmailNotification()
b=SMSNotification()
c=WhatsAppNotification()
a.send()
b.send()
c.send()

"""EmailNotification
SMSNotification
WhatsAppNotification
"""


"""Q8. Banking System 
Create a parent class Bank with a method interest_rate(). Create child classes SBI, HDFC, and 
ICICI, each returning a different interest rate. 
Display the interest rate using a common function."""

class bank_interest:
    def interest(self):
        print("5% of interest")

class SBI(bank_interest):
    def interest(self):
        print("2% of interest")

class ICICI(bank_interest):
    def interest(self):
        print("2.5% of interest")

def interest_process(abc):
    abc.interest()

a=bank_interest()
b=SBI()
c=ICICI()
interest_process(a)
interest_process(b)
interest_process(c)

"""list=[bank_interest(),SBI(),ICICI()]
for i in list:
    i.interest()"""


"""Q9. Polymorphism with Built-in Functions"""
"""Create a list, tuple, string, and dictionary.
Use the same built-in functions len() and type() on all four objects. 
Explain how the same function works with different object types."""

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_string = "Gnaneshwar"
my_dict = {"name": "Gnani", "id": 101}

print(len(my_list))
print(len(my_tuple))
print(len(my_string))
print(len(my_dict))

print("---")

print(type(my_list))
print(type(my_tuple))
print(type(my_string))
print(type(my_dict))

"""3
3
10
2
---
<class 'list'>
<class 'tuple'>
<class 'str'>
<class 'dict'>"""


"""Q10. Food Ordering System 
Create a parent class Food with a method prepare(). Create child classes Pizza, Burger, and 
Biryani. 
Each class should provide its own preparation process. Call prepare() using a common function 
that accepts different food objects."""

class Food:
    def prepare(self):
        print("Preparing food")

class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza with cheese and toppings")

class Burger(Food):
    def prepare(self):
        print("Preparing Burger with bun, patty and vegetables")

class Biryani(Food):
    def prepare(self):
        print("Preparing Biryani with rice, spices and chicken")

def prepare_food(food):
    food.prepare()

pizza = Pizza()
burger = Burger()
biryani = Biryani()
prepare_food(pizza)
prepare_food(burger)
prepare_food(biryani)


"""Level 3: Advanced Problem-Solving 
Advanced """

"""Q11. Operator Overloading – Addition 
Create a class Book with attributes pages. Overload the + operator using __add__() to add the 
pages of two books. 
Expected output: 
Book 1 pages: 150 
Book 2 pages: 200 
Total pages: 350 """

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
b1=Book(150)
b2=Book(200)
print("book 1 pages:",b1.pages)
print("book 2 pages:",b2.pages)
print("Total pages:",b1+b2)

"""book 1 pages: 150
book 2 pages: 200
Total pages: 350"""

"""Q12. Operator Overloading – Comparison 
Create a class Product with an attribute price. Overload the > operator using __gt__() to 
compare the prices of two products. 
Display which product has the higher price."""

class product:
    def __init__(self,name,price):
        self.price=price
        self.name=name
    def __gt__(self, other):
        return self.price>other.price
p1=product("laptop",50000)
p2=product("mobile",25000)

print("Product 1:",p1.name)
print("price:",p1.price)

print("Product 2:",p2.name)
print("price:",p2.price)

if p1>p2:
    print(p1.name,"has higher price")
else:
    print(p2.name,"has higher price")

"""Product 1: laptop
price: 50000
Product 2: mobile
price: 25000
laptop has higher price"""


"""Q13. Duck Typing – Media Player 
Create three classes: Audio, Video, and Podcast. Each class should have a play() method. 
Create a function play_media() that accepts any object and calls its play() method without 
checking its class."""

class Audio:
    def play(self):
        print("playing audio")

class Video:
    def play(self):
        print("playing video")

class Podcast:
    def play(self):
        print("playing Podcast")

def play_media(media):
    media.play()

audio = Audio()
video = Video()
podcast = Podcast()

play_media(audio)
play_media(video)
play_media(podcast)

"""playing audio
playing video
playing Podcast"""

"""Q14. Polymorphism with Class Methods 
Create a parent class Employee with a class method company_info(). Create child classes 
Developer and DataAnalyst that override the class method. 
Call the method using both child classes and explain the output."""

class Employee:
    @classmethod
    def company_info(cls):
        print("Employee works in ABC Company")
class Developer(Employee):
    @classmethod 
    def company_info(cls): 
        print("Developer works in ABC Company") 
class DataAnalyst(Employee):
    @classmethod 
    def company_info(cls):
        print("Data Analyst works in ABC Company")
Developer.company_info() 
DataAnalyst.company_info()

"""Developer works in ABC Company
Data Analyst works in ABC Company"""


"""Q15. Shopping Cart 
Create classes Electronics, Clothing, and Grocery. Each class should have a method 
calculate_discount() with a different discount calculation. 
Create a common function to calculate and display the final price for different products."""

class Electronics:
    def __init__(self, price):
        self.price = price
    def calculate_discount(self):
        return self.price * 10 / 100
class Clothing:
    def __init__(self, price):
        self.price = price
    def calculate_discount(self):
        return self.price * 20 / 100
class Grocery:
    def __init__(self, price):
        self.price = price
    def calculate_discount(self):
        return self.price * 5 / 100
def calculate_final_price(product):
    discount = product.calculate_discount()
    final_price = product.price - discount

    print("Original Price:", product.price)
    print("Discount:", discount)
    print("Final Price:", final_price)
    print("------------------------")
electronics = Electronics(50000)
clothing = Clothing(2000)
grocery = Grocery(1000)

calculate_final_price(electronics)
calculate_final_price(clothing)
calculate_final_price(grocery)

"""Original Price: 50000
Discount: 5000.0
Final Price: 45000.0
------------------------
Original Price: 2000
Discount: 400.0
Final Price: 1600.0
------------------------
Original Price: 1000
Discount: 50.0
Final Price: 950.0
------------------------"""

     
"""Level 4: Real-Time Interview Challenges 
Interview Practice """

"""Q16. Ride Booking Application 
Create a parent class Ride with a method calculate_fare(). Create child classes BikeRide, 
CarRide, and AutoRide. 
Each ride should calculate its fare based on distance and its own rate per kilometer. Display the 
fare using a common function. """

class ride:
    def calculate_fare(self,distance,price):
            self.distance=distance
            self.price=price
    def fare(self):
        self.fare=self.distance*self.price
        print("fare for your ride:",self.fare)

class BikeRide(ride):
    pass
class CarRide(ride):
    pass
class AutoRide(ride):
    pass

a1=AutoRide()
a1.calculate_fare(10,17)
a1.fare()

b1=BikeRide()
b1.calculate_fare(10,9.5)
b1.fare()

c1=CarRide()
c1.calculate_fare(10,25)
c1.fare()

"""fare for your ride: 170
fare for your ride: 95.0
fare for your ride: 250"""

"""Q17. Hospital Management System 
Create a parent class Doctor with a method treat_patient(). Create child classes Cardiologist, 
Dentist, and Neurologist. 
Each doctor should provide a different treatment description. Use polymorphism to call the 
methods. """

class Doctor:
    def treat_patient(self):
        print("Doctor is treating the patient")
class Cardiologist(Doctor):
    def treat_patient(self):
        print("Cardiologist is treating heart problems")
class Dentist(Doctor):
    def treat_patient(self):
        print("Dentist is treating teeth problems")
class Neurologist(Doctor):
    def treat_patient(self):
        print("Neurologist is treating nervous system problems")
def treat(doctor):
    doctor.treat_patient()

cardiologist = Cardiologist()
dentist = Dentist()
neurologist = Neurologist()

treat(cardiologist)
treat(dentist)
treat(neurologist)

"""Cardiologist is treating heart problems
Dentist is treating teeth problems
Neurologist is treating nervous system problems"""


"""Q18. File Processing System 
Create classes CSVFile, JSONFile, and TextFile. Each class should have a read_file() method. 
Create a common function process_file() that accepts different file objects and calls the 
appropriate method."""

class CSVFile:
    def read_file(self):
        print("Reading CSV file")

class JSONFile:
    def read_file(self):
        print("Reading JSON file")

class TextFile:
    def read_file(self):
        print("Reading Text file")

def process_file(file):
    file.read_file()

csv = CSVFile()
json = JSONFile()
text = TextFile()

process_file(csv)
process_file(json)
process_file(text)

"""Reading CSV file
Reading JSON file
Reading Text file"""


"""Q19. Custom Data Types 
Create a class Distance with attributes km and meters. Overload the + operator to add two 
distance objects and return the total distance in normalized kilometers and meters. 
Example: 
Distance 1: 2 km 500 meters 
Distance 2: 3 km 800 meters 
Total: 6 km 300 meters"""

class Distance:
    def __init__(self, km, meters):
        self.km = km
        self.meters = meters

    def __add__(self, other):
        total_km = self.km + other.km
        total_meters = self.meters + other.meters

        if total_meters >= 1000:
            total_km = total_km + total_meters // 1000
            total_meters = total_meters % 1000

        return Distance(total_km, total_meters)
    
    def display(self):
        print("Total:", self.km, "km", self.meters, "meters")

d1 = Distance(2, 500)
d2 = Distance(3, 800)
d3 = d1 + d2
d3.display()

"""Total: 6 km 300 meters"""

"""Q20. Complete Polymorphism Challenge 
Create a class Employee and child classes Manager, Developer, and Tester. 
Each employee should have: 
• A work() method with a different implementation. 
• A calculate_bonus() method with a different implementation. 
• A display_details() method to display employee information. 
Store all employee objects in a list and use a loop to call the methods without checking the 
object type."""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print("Employee is working")

    def calculate_bonus(self):
        return self.salary * 5 / 100

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def work(self):
        print("Manager is managing the team")

    def calculate_bonus(self):
        return self.salary * 20 / 100

class Developer(Employee):
    def work(self):
        print("Developer is writing code")

    def calculate_bonus(self):
        return self.salary * 15 / 100

class Tester(Employee):
    def work(self):
        print("Tester is testing the application")

    def calculate_bonus(self):
        return self.salary * 10 / 100

manager = Manager("Gnaneshwar", 60000)
developer = Developer("Rajesh", 50000)
tester = Tester("Suresh", 40000)

employees = [manager, developer, tester]

for employee in employees:
    employee.display_details()
    employee.work()
    bonus = employee.calculate_bonus()

    print("Bonus:", bonus)
    print("--------------------")

"""Name: Gnaneshwar
Salary: 60000
Manager is managing the team
Bonus: 12000.0
--------------------
Name: Rajesh
Salary: 50000
Developer is writing code
Bonus: 7500.0
--------------------
Name: Suresh
Salary: 40000
Tester is testing the application
Bonus: 4000.0
--------------------"""




