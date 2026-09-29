#===============================================================================================
#@@ INHERITENCE @@##
#===============================================================================================
"""
###single Inheritance###
"""

"""1. Create a Person class with name and age. Create a Student class that inherits from 
Person and adds course. Display all details."""
from os import name
from typing import overload

from yaml import YAMLError


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class student(person):
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Coure:",self.course)

s1=student("Gnaneshwar",23,"DS")
s1.display()

"""output:--
Name: Gnaneshwar
Age: 23
Coure: DS
"""


"""2. Create an Employee class with name, salary, and department. Create a Manager class 
that inherits from Employee and adds team_size."""

class employee:
    def __init__(self,name, salary,department):
        self.name=name
        self.salary=salary
        self.department=department

class manager(employee):
    def __init__(self, name, salary, department,team_size):
        self.name=name
        self.salary=salary
        self.department=department
        self.team_size=team_size

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("Team Size:", self.team_size)

m1=manager("Gnaneshar",50000,"IT","10")
# m1.manager()
m1.display()

"""output:
Name: Gnaneshar
Salary: 50000
Department: IT
Team Size: 10
"""

"""3. Create a Vehicle class with brand and model. Create a Car class that inherits from Vehicle 
and adds fuel_type."""

class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class car(vehicle):
    def __init__(self, brand, model,fuel_type):
        self.brand=brand
        self.model=model
        self.fuel_type=fuel_type

    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Fuel_type:",self.fuel_type)

C1=car("Toyota", "Innova", "Diesel")
C1.display()

"""output:--
Brand: Toyota
Model: Innova
Fuel_type: Diesel
"""

"""4. Create a BankAccount class with account_number and balance. Create a SavingsAccount 
class that inherits from it and adds interest_rate."""

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance,interest_rate):
        self.account_number=account_number
        self.balance=balance
        self.interest_rate=interest_rate

    def display(self):
        print("Account Number:",self.account_number)
        print("Balance:",self.balance)
        print("Interst Rate:",self.interest_rate)

B1=SavingsAccount(963852741,50000,5.5)
B1.display()

"""
Account Number: 963852741
Balance: 50000
Interst Rate: 5.5
"""


"""5. Create a Product class with product_name and price. Create an ElectronicProduct class 
that inherits from it and adds warranty_years."""

class product:
    def __init__(self,product_name,price):
        self.product=product_name
        self.price=price

class ElectronicProduct(product):
    def __init__(self, product_name, price,warranty_years):
        self.product=product_name
        self.price=price
        self.warranty=warranty_years

    def display(self):
        print("Product Name:",self.product)
        print("Price:",self.price)
        print("Warranty Years:",self.warranty)

p1=ElectronicProduct("Laptop",55249,"5Y")
p1.display()
        
"""
Product Name: Laptop
Price: 55249
Warranty Years: 5Y
"""

"""6. Create an Animal class with name and age. Create a Dog class that inherits from it and 
adds breed.  
Constructor + super()"""

class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Dog(animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)
        self.breed=breed
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Breed:",self.breed)

a1=Dog("Tommy", 3, "Labrador")
a1.display()

"""
Name: Tommy
Age: 3
Breed: Labrador
"""


"""7. Create a Person class with a constructor accepting name and age. Create a Student class 
with course and marks. Use super()."""

class Person:
    def __init__(self,name,age):
        self.age=age
        self.name=name

class student(Person):
    def __init__(self, name, age,course,marks):
        self.name=name
        self.age=age
        self.course=course
        self.marks=marks

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)
        print("Marks:",self.marks)

s1=student("gnaneswar",23,"EEE",85)
s1.display()     

"""
Name: gnaneswar
Age: 23
Course: EEE
Marks: 85
"""


"""8. Create an Employee class with name and salary. Create a Developer class with language 
and experience. Initialize all values using super()."""

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class developer(Employee):
    def __init__(self, name, salary,language,experience):
        super().__init__(name, salary)
        self.language=language
        self.experience=experience

    def display(self):
        print("Emp Name:",self.name)
        print("Salary:",self.salary)
        print("language know:",self.language)
        print("Experience:",self.experience)

E2=developer("Gnaneshwar",55000,"Python","2Y")
E2.display()
        
"""output:
Emp Name: Gnaneshwar
Salary: 55000
language know: Python
Experience: 2Y
"""


"""9. Create a Vehicle class with brand and model. Create a Car class with fuel_type and price. 
Use super() to initialize parent attributes.""" 

class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class car(vehicle):
    def __init__(self, brand, model,fuel_type,price):
        super().__init__(brand, model)
        self.fuel_type=fuel_type
        self.price=price

    def display(self):
        print("Band:",self.brand)
        print("Model:",self.model)
        print("Fuel Type:",self.fuel_type)
        print("Price:",self.price)\

c1=car("Toyota",2025,"Innova", "Diesel")
c1.display()

"""
Band: Toyota
Model: 2025
Fuel Type: Innova
Price: Diesel
"""
        

"""10. Create a BankAccount class with holder_name and balance. Create a SavingsAccount 
class with interest_rate. Calculate the final balance."""

class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder = holder_name
        self.balance = balance

class SavingAccount(BankAccount):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.interest_rate = interest_rate

    def interest_(self):
        self.interest = (self.balance / 100) * self.interest_rate
        return self.interest

    def total(self):
        self.total_balance = self.balance + self.interest
        return self.total_balance

    def display(self):
        print("Acc Holder Name:", self.holder)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate)
        print("Interest Gained:", self.interest)
        print("Total Balance:", self.total_balance)

Acc = SavingAccount("Gnaneshwar", 50000, 5)
Acc.interest_()
Acc.total()
Acc.display()

"""output:---
Acc Holder Name: Gnaneshwar
Balance: 50000
Interest Rate: 5
Interest Gained: 2500.0
Total Balance: 52500.0
"""

"""11. Create a Company class with company_name. Create an Employee class with 
employee_name and salary. Use super().  
Multilevel Inheritance """

class Company:
    def __init__(self,company_name):
        self.company_name=company_name

class Employee(Company):
    def __init__(self, company_name,employee_name,salary):
        super().__init__(company_name)
        self.employee_name=employee_name
        self.salary=salary

    def display(self):
        print("Company Name:",self.company_name)
        print("Employee Name:",self.employee_name)
        print("Salary:",self.salary)

e1=Employee("Infosys","Gnaneshwar",50000)
e1.display()

"""output:---
Company Name: Infosys
Employee Name: Gnaneshwar
Salary: 50000
""" 


"""12. Create the following:  
Person 
↓ 
Employee 
↓ 
Manager 
Store appropriate information in each class and display all details."""

class Person:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age

class Employee(Person):
    def __init__(self,Name,Age,Employee_id,Salary):
        super().__init__(Name,Age)
        self.employee_id=Employee_id
        self.salary=Salary

class Manager(Employee):
    def __init__(self, Name, Age, Employee_id, Salary,Department):
        super().__init__(Name, Age, Employee_id, Salary)
        self.department=Department

    def display(self):
        print("Name:",self.Name)
        print("Age:",self.Age)
        print("Employee id:",self.employee_id)
        print("Salary:",self.salary)
        print("Department:",self.department)

m1=Manager("Gnaneshwar",25,101,45000,"IT")
m1.display()

"""output:---
Name: Gnaneshwar
Age: 25
Employee id: 101
Salary: 45000
Department: IT
"""

"""13. Create:  
Vehicle 
↓ 
Car 
↓ 
ElectricCar 
Add attributes at each level and display them."""

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class car(vehicle):
    def __init__(self, brand, model,fuel_type):
        super().__init__(brand, model)
        self.fuel_pytpe=fuel_type

class electrical(car):
    def __init__(self, brand, model, fuel_type,battery):
        super().__init__(brand, model, fuel_type)
        self.battery=battery

    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Fuel Type:",self.fuel_pytpe)
        print("Battery:",self.battery)

v1=electrical("tesla","model 3","electrical","75kWh")
v1.display()

"""output:---
Brand: tesla
Model: model 3
Fuel Type: electrical
Battery: 75kWh
"""

"""14. Create:  
Student 
↓ 
GraduateStudent 
↓ 
ResearchStudent 
Use constructors and super() at every level."""

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class GraduateStudent(student):
    def __init__(self, name, age,course):
        super().__init__(name, age)
        self.course=course

class ResearchStudent(GraduateStudent):
    def __init__(self, name, age, course,research_topic):
        super().__init__(name, age, course)
        self.research_topic=research_topic

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)

student = ResearchStudent("Gnaneshwar",2025,"M.Tech","Artificial Intelligence")
student.display()

"""output:---
Age: 2025
Course: M.Tech
Research Topic: Artificial Intelligence
"""


"""15. Create:  
Animal 
↓ 
Mammal 
↓ 
Dog 
Add suitable attributes and methods to each class.""" 

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Animal NAme:",self.name)
        print("Age:",self.age)

class Mammal(Animal):
    def __init__(self, name, age,Hair_colour):
        super().__init__(name, age)
        self.hair_colour=Hair_colour

    def display_mammal(self):
        print("Hair Color:", self.hair_colour)

class Dog(Mammal):
    def __init__(self, name, age, Hair_colour,breed):
        super().__init__(name, age, Hair_colour)
        self.breed=breed

    def display_Dog(self):
        print("Breed Name:",self.breed)

a1=Dog("Alpha",15,"Black","Army")
a1.display()
a1.display_mammal()
a1.display_Dog()

"""output:--
Animal NAme: Alpha
Age: 15
Hair Color: Black
Breed Name: Army
"""
 
"""Multiple Inheritance """
"""16. Create Father and Mother classes with different properties. Create a Child class that 
inherits from both. """

class father:
    def home(self):
        print("father have home")

class mother:
    def Gold(self):
        print("mother have 100 grams of Gold")

class child(father,mother):
    def bike(self):
        print("child have bike")

a=child()
a.home()
a.Gold()
a.bike()

"""output:---
father have home
mother have 100 grams of Gold
child have bike"""
 
"""17. Create Printer and Scanner classes. Create a Machine class that inherits from both. """

class Printer:
    def __init__(self, print_speed):
        self.print_speed = print_speed

    def display_printer(self):
        print("Print Speed:", self.print_speed)

    def print_document(self):
        print("Printing document...")

class Scanner:
    def __init__(self, scan_resolution):
        self.scan_resolution = scan_resolution

    def display_scanner(self):
        print("Scan Resolution:", self.scan_resolution)

    def scan_document(self):
        print("Scanning document...")

class Machine(Printer, Scanner):
    def __init__(self, print_speed, scan_resolution, brand):
        Printer.__init__(self, print_speed)
        Scanner.__init__(self, scan_resolution)
        self.brand = brand

    def display_machine(self):
        print("Brand:", self.brand)

m1 = Machine("30 pages/min", "1200 DPI", "HP")

m1.display_printer()
m1.print_document()

m1.display_scanner()
m1.scan_document()

m1.display_machine()

"""output:--
Print Speed: 30 pages/min
Printing document...
Scan Resolution: 1200 DPI
Scanning document...
Brand: HP
"""

"""18. Create Teacher and Researcher classes. Create a Professor class that inherits from both."""

class Teacher:
    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_id = teacher_id
        self.subject = subject

    def display_teacher(self):
        print(f"Teacher Name: {self.name}")
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Subject: {self.subject}")


class Researcher:
    def __init__(self, research_topic, experience):
        self.research_topic = research_topic
        self.experience = experience

    def display_researcher(self):
        print(f"Research Topic: {self.research_topic}")
        print(f"Experience: {self.experience} years")

class Professor(Teacher, Researcher):
    def __init__(self, name, teacher_id, subject,
                 research_topic, experience, department):

        Teacher.__init__(self, name, teacher_id, subject)
        Researcher.__init__(self, research_topic, experience)

        self.department = department

    def display_professor(self):
        print(f"Department: {self.department}")

p1=Professor("Ravi",101,"Python","Artificial Intelligence",5,"Computer Science")
p1.display_teacher()
p1.display_researcher()
p1.display_professor()

"""output:--
Teacher Name: Ravi
Teacher ID: 101
Subject: Python
Research Topic: Artificial Intelligence
Experience: 5 years
Department: Computer Science
"""


 
"""19. Create Developer and Designer classes. Create a UIDeveloper class that inherits from 
both. """ 

class Developer:
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def display_developer(self):
        print("Developer Name:", self.name)
        print("Programming Language:", self.language)

class Designer:
    def __init__(self, design_tool):
        self.design_tool = design_tool

    def display_designer(self):
        print("Design Tool:", self.design_tool)

class UIDeveloper(Developer, Designer):
    def __init__(self, name, language, design_tool, experience):
        Developer.__init__(self, name, language)
        Designer.__init__(self, design_tool)
        self.experience = experience

    def display_ui_developer(self):
        print("Experience:", self.experience, "years")

u1 = UIDeveloper("Ravi","Python","Figma",3)
u1.display_developer()
u1.display_designer()
u1.display_ui_developer()

"""output:--
Developer Name: Ravi
Programming Language: Python
Design Tool: Figma
Experience: 3 years
"""
 
"""Hierarchical Inheritance """
"""20. Create an Employee parent class and two child classes Developer and Tester. Add 
different properties to each child. """ 

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_developer(self):
        print("Programming Language:", self.programming_language)

class Tester(Employee):
    def __init__(self, name, salary, testing_tool):
        super().__init__(name, salary)
        self.testing_tool = testing_tool

    def display_tester(self):
        print("Testing Tool:", self.testing_tool)

d1 = Developer("Ravi", 50000, "Python")
t1 = Tester("Kiran", 45000, "Selenium")

d1.display_employee()
d1.display_developer()
print()
t1.display_employee()
t1.display_tester()

"""output:--
Employee Name: Ravi
Salary: 50000
Programming Language: Python

Employee Name: Kiran
Salary: 45000
Testing Tool: Selenium
"""

"""
21. Create an Animal parent class and child classes Dog, Cat, and Cow. Add different 
attributes and methods to each child."""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print("Dog is barking")

    def display_dog(self):
        self.display()
        print("Breed:", self.breed)
        self.bark()

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print("Cat is meowing")

    def display_cat(self):
        self.display()
        print("Color:", self.color)
        self.meow()

class Cow(Animal):
    def __init__(self, name, age, milk):
        super().__init__(name, age)
        self.milk = milk

    def eat_grass(self):
        print("Cow is eating grass")

    def display_cow(self):
        self.display()
        print("Milk:", self.milk, "litres")
        self.eat_grass()

dog = Dog("Tommy", 3, "Labrador")
cat = Cat("Kitty", 2, "White")
cow = Cow("Ganga", 5, 10)

print("----- Dog Details -----")
dog.display_dog()

print("\n----- Cat Details -----")
cat.display_cat()

print("\n----- Cow Details -----")
cow.display_cow()


"""output:---
----- Dog Details -----
Name: Tommy
Age: 3
Breed: Labrador
Dog is barking

----- Cat Details -----
Name: Kitty
Age: 2
Color: White
Cat is meowing

----- Cow Details -----
Name: Ganga
Age: 5
Milk: 10 litres
Cow is eating grass
"""

"""
22. Create a Vehicle parent class and child classes Car, Bike, and Bus. Display their specific 
information.""" 

class Vehicle:
    def __init__(self,brand,Year,model):
        self.brand=brand
        self.year=Year
        self.model=model

    def display(self):
        print("Brand:",self.brand)
        print("Year:",self.year)
        print("Model:",self.model)

class car(Vehicle):
    def __init__(self, brand, Year, model,fuel_type):
        super().__init__(brand, Year, model)
        self.fuel_type=fuel_type

    def display_car(self):
        print(super().display())
        print("Fuel Type:",self.fuel_type)

class bike(Vehicle):
    def __init__(self, brand, Year, model,engine):
        super().__init__(brand, Year, model)
        self.engine=engine

    def display_bike(self):
        print(super().display())
        print("Engine Range:",self.engine)

class bus(Vehicle):
    def __init__(self, brand, Year, model,seats):
        super().__init__(brand, Year, model)
        self.seats=seats

    def dispaly_bus(self):
        print(super().display())
        print("seating capacity:",self.seats)

car = car("Toyota",2024, "Innova", "Petrol")
bike = bike("Honda",2026, "Activa", "125cc")
bus = bus("Volvo",2024, "B9R",50)

print("-----car details-----")
car.display_car()
print()
print("-----bike details-----")
bike.display_bike()
print()
print("-----bus details-----")
bus.dispaly_bus()

"""output:---
-----car details-----
Brand: Toyota
Year: 2024
Model: Innova
None
Fuel Type: Petrol

-----bike details-----
Brand: Honda
Year: 2026
Model: Activa
None
Engine Range: 125cc

-----bus details-----
Brand: Volvo
Year: 2024
Model: B9R
None
seating capacity: 50"""


"""Hybrid Inheritance """
"""23. Create this structure:  
             Employee 
             /      \ 
       Developer    Tester 
             \      / 
              TeamLead 
Implement the classes and display all inherited properties and methods."""
class Employee:
    def __init__(self, Employee_name, employee_id):
        self.emp_name = Employee_name
        self.emp_id = employee_id

    def display(self):
        print("Employee name:", self.emp_name)
        print("Employee ID:", self.emp_id)

class Developer(Employee):
    def __init__(self, Employee_name, employee_id, programming_language):
        super().__init__(Employee_name, employee_id)
        self.programming_language = programming_language

    def display_dev(self):
        super().display()
        print("Programming Language:", self.programming_language)

class Tester(Employee):
    def __init__(self, Employee_name, employee_id, testing_tool):
        super().__init__(Employee_name, employee_id)
        self.tool = testing_tool

    def display_test(self):
        super().display()
        print("Tool used for testing:", self.tool)

class TeamLead(Developer, Tester):
    def __init__(self, Employee_name, employee_id,
                 programming_language, testing_tool, team_size):

        Employee.__init__(self, Employee_name, employee_id)

        self.programming_language = programming_language
        self.tool = testing_tool
        self.team_size = team_size

    def display_teamlead(self):
        self.display()
        print("Programming Language:", self.programming_language)
        print("Testing Tool:", self.tool)
        print("Team Size:", self.team_size)

d1 = Developer("Gnaneshwar", 101, "Python")

d1.display_dev()
print("------------------------")

t1 = Tester("Ravi", 102, "Selenium")

t1.display_test()
print("------------------------")

tl = TeamLead("Suresh", 103, "Java", "Selenium", 10)

tl.display_teamlead()

# """output:---
# Employee name: Suresh
# Employee ID: 103
# Programming Language: Java
# Testing Tool: Selenium
# Team Size: 10"""

"""24. Create:  
              Device 
              /    \ 
           Phone   Camera 
              \    / 
           Smartphone 
Implement suitable attributes and methods"""

class Device:
    def __init__(self, brand):
        self.brand = brand

    def display_device(self):
        print("Brand:", self.brand)


class Phone(Device):
    def __init__(self, brand, phone_number):
        super().__init__(brand)
        self.phone_number = phone_number

    def display_phone(self):
        print("Phone Number:", self.phone_number)

class Camera(Device):
    def __init__(self, brand, megapixel):
        super().__init__(brand)
        self.megapixel = megapixel

    def display_camera(self):
        print("Megapixel:", self.megapixel)

class Smartphone(Phone, Camera):
    def __init__(self, brand, phone_number, megapixel, model):
        Device.__init__(self, brand)
        self.phone_number = phone_number
        self.megapixel = megapixel
        self.model = model

    def display(self):
        self.display_device()
        self.display_phone()
        self.display_camera()
        print("Model:", self.model)

s = Smartphone("Samsung", "9876543210", 108, "S25")
s.display()

"""output:---
Brand: Samsung
Phone Number: 9876543210
Megapixel: 108
Model: S25"""

"""25. Create:  
              Person 
              /    \ 
          Student  Employee 
              \    / 
             Intern 
Implement this hybrid inheritance structure using constructors."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

class Intern(Student, Employee):
    def __init__(self, name, age, course, company, duration):
        Person.__init__(self, name, age)
        self.course = course
        self.company = company
        self.duration = duration

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Company:", self.company)
        print("Internship Duration:", self.duration)

obj = Intern("Gnaneshwar", 22, "Python", "ABC Technologies", "6 Months")

obj.display()

"""output:--
Name: Gnaneshwar
Age: 22
Course: Python
Company: ABC Technologies
Internship Duration: 6 Months"""


""" Challenge Problems """
"""26. Create a Library Management System using inheritance:  
Library 
   ↓ 
Book 
   ↓ 
EBook 
Store book details, author, price, and file size. """

class Library:
    def __init__(self, library_name):
        self.library_name = library_name

    def display_library(self):
        print("Library Name:", self.library_name)

class Book(Library):
    def __init__(self, library_name, book_name, author, price):
        super().__init__(library_name)
        self.book_name = book_name
        self.author = author
        self.price = price

    def display_book(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Price:", self.price)

class EBook(Book):
    def __init__(self, library_name, book_name, author, price, file_size):
        super().__init__(library_name, book_name, author, price)
        self.file_size = file_size

    def display_ebook(self):
        self.display_library()
        self.display_book()
        print("File Size:", self.file_size, "MB")

ebook = EBook("City Library", "Python Basics", "John Smith", 500, 25)

ebook.display_ebook()

"""Library Name: City Library
Book Name: Python Basics
Author: John Smith
Price: 500
File Size: 25 MB"""

"""27. Create an E-commerce system:  
User 
 /  \ 
Customer Seller 
 \     / 
Marketplace 
Store appropriate details using inheritance."""

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_user(self):
        print("Name:", self.name)
        print("Email:", self.email)

class Customer(User):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.customer_id = customer_id

    def display_customer(self):
        print("Customer ID:", self.customer_id)

class Seller(User):
    def __init__(self, name, email, seller_id):
        super().__init__(name, email)
        self.seller_id = seller_id

    def display_seller(self):
        print("Seller ID:", self.seller_id)

class Marketplace(Customer, Seller):
    def __init__(self, name, email, customer_id, seller_id, product):
        User.__init__(self, name, email)
        self.customer_id = customer_id
        self.seller_id = seller_id
        self.product = product

    def display_marketplace(self):
        self.display_user()
        print("Customer ID:", self.customer_id)
        print("Seller ID:", self.seller_id)
        print("Product:", self.product)

marketplace = Marketplace("Gnaneshwar","gnaneshwar@gmail.com",101,501,"Laptop")
marketplace.display_marketplace()

"""output:--
Name: Gnaneshwar
Email: gnaneshwar@gmail.com
Customer ID: 101
Seller ID: 501
Product: Laptop"""



"""28. Create a College Management System:  
Person 
/   \ 
Student Teacher 
\   / 
Assistant 
Use super() wherever required."""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student(self):
        print("Student ID:", self.student_id)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        print("Subject:", self.subject)

class Assistant(Student, Teacher):
    def __init__(self, name, age, student_id, subject, assistant_role):
        Person.__init__(self, name, age)
        self.student_id = student_id
        self.subject = subject
        self.assistant_role = assistant_role

    def display_assistant(self):
        self.display_person()
        print("Student ID:", self.student_id)
        print("Subject:", self.subject)
        print("Assistant Role:", self.assistant_role)

assistant = Assistant("Rahul",22,101,"Python","Teaching Assistant")
assistant.display_assistant()

"""output:---
Name: Rahul
Age: 22
Student ID: 101
Subject: Python
Assistant Role: Teaching Assistant"""



"""29. Create a Banking System:  
Account 
/    \ 
Savings Current 
Implement account holder, account number, balance, deposit, and withdrawal."""

class Account:
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Holder:", self.holder_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)

class Savings(Account):
    def __init__(self, holder_name, account_number, balance, interest_rate):
        super().__init__(holder_name, account_number, balance)
        self.interest_rate = interest_rate

    def display_savings(self):
        self.display()
        print("Interest Rate:", self.interest_rate, "%")

class Current(Account):
    def __init__(self, holder_name, account_number, balance, overdraft_limit):
        super().__init__(holder_name, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def display_current(self):
        self.display()
        print("Overdraft Limit:", self.overdraft_limit)

savings = Savings("Gnaneshwar", 1001, 10000, 6.5)
savings.deposit(2000)
savings.withdraw(3000)
savings.display_savings()

"""output:---
Deposited: 2000
Withdrawn: 3000
Account Holder: Gnaneshwar
Account Number: 1001
Balance: 9000
Interest Rate: 6.5 %
"""


"""30. Create a Company Management System:  
Employee 
/     \ 
Developer Tester 
\   / 
TeamLead 
Implement this as a hybrid inheritance problem. """

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_employee(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)

class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def display_developer(self):
        print("Programming Language:", self.programming_language)

class Tester(Employee):
    def __init__(self, name, employee_id, testing_tool):
        super().__init__(name, employee_id)
        self.testing_tool = testing_tool

    def display_tester(self):
        print("Testing Tool:", self.testing_tool)

class TeamLead(Developer, Tester):
    def __init__(
        self,name,employee_id,programming_language,testing_tool,team_size):
        Employee.__init__(self, name, employee_id)
        self.programming_language = programming_language
        self.testing_tool = testing_tool
        self.team_size = team_size

    def display_teamlead(self):
        self.display_employee()
        print("Programming Language:", self.programming_language)
        print("Testing Tool:", self.testing_tool)
        print("Team Size:", self.team_size)

teamlead = TeamLead("Gnaneshwar",101,"Python","Selenium",8)
teamlead.display_teamlead()

"""output:--
Employee Name: Gnaneshwar
Employee ID: 101
Programming Language: Python
Testing Tool: Selenium
Team Size: 8"""
#===============================================================================================