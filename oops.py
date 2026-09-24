

#=======================================================================================================================================================================================================##################
## OOPS BASIC PROBLEMS:  20 QUESTIONS
#=======================================================================================================================================================================================================##################


"""Level 1 – Basic """


"""1. Student Details
Create a class Student
with:
• Variables: name, age, course  
• Constructor to initialize the variables  
• Method display() to print student details.  
Expected concept: Constructor + instance variables + method """


class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course


    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("course:",self.course)
       
s1=student("gnaneshwar",23,"EEE")
s1.display()


"""output:-
name: gnaneshwar
age: 23
course: EEE"""


#==========================================================================================


"""2. Employee Salary
Create a class Employee
with:
• name , basic_salary  
Create a method display_salary() that prints the employee's salary.
Example: Name: Aparna Salary: 30000 """


class employee:
    def __init__(self,name,basic_salary):
        self.name=name
        self.basic_salary=basic_salary


    def display(self):
        print("name:",self.name)
        print("salary:",self.basic_salary)
       


e1=employee("aparna",30000)
e1.display()


"""output:-
name: aparna
salary: 30000"""




#==========================================================================================




"""3. Bank Account
Create a class BankAccount
with
• account_holder  
• balance  
Create methods:
• deposit(amount)  
• withdraw(amount)  
• display_balance()  
If the withdrawal amount is greater than the balance,display "Insufficient Balance". """


class bank():
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance


    def display_details(self):
        print("acc holder name:",self.account_holder)
        print("Bank balance:",self.balance)
       


    def deposit(self,amount):
        self.balance+=amount
        print("diposite amount:",amount)
       


    def withdrawl(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("withdrawl amount:",amount)
            print("available balance:",self.balance)
        else:
            print("Insufficient Balance:" "ERROR")
           


    def display_balance(self):
        print("Balance:",self.balance)
       


b1=bank("Gnaneshwar",500000)
b1.display_details()
b1.deposit(5000)
b1.withdrawl(600000)
b1.display_balance()


"""output:-
acc holder name: Gnaneshwar
Bank balance: 500000
diposite amount: 5000
Insufficient Balance:ERROR
Balance: 505000"""




#==========================================================================================




"""4. Mobile Phone
Create a class Mobile
with:
• brand  
• model  
• price  
Create a method
display()
to display all details.
Create objects for 3 different mobiles."""


class mobile:
    def __init__(self,brand,model,price ):
        self.brand=brand
        self.model=model
        self.price=price


    def display(self):
        print("Mobile Brand:",self.brand)
        print("Mobile Model:",self.model)
        print("Mobile Price:",self.price)
       


m1=mobile("samsung","S 25 ULTRA",155000)
m2 = mobile("Apple", "iPhone 17", 120000)
m3 = mobile("OnePlus", "13", 70000)


m1.display()
m2.display()
m3.display()




"""outputs:=
Mobile Brand: samsung
Mobile Model: S 25 ULTRA
Mobile Price: 155000


Mobile Brand: Apple
Mobile Model: iPhone 17
Mobile Price: 120000


Mobile Brand: OnePlus
Mobile Model: 13
Mobile Price: 70000"""




#==========================================================================================




"""5. Rectangle Calculation
Create a class Rectangle
with:
• length  
• breadth  
Create methods:
• area()
• perimeter()  
Use the constructor to initialize length and breadth."""




class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


    def area(self):
        a = self.length * self.breadth
        print("Area:", a)
       


    def perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        print("Perimeter:", perimeter)
       


r1 = Rectangle(10, 8)
r1.area()
r1.perimeter()


"""o/p:
Area: 80
Perimeter: 36"""


#==========================================================================================
"""Level 2 – Logic-Based Problems"""


"""6. Student Marks
Create a class Student
with:
• name
• marks  
Create methods:
• display_marks()  
• check_result()  
Rules:
marks >= 40 → Pass
marks < 40  → Fail
Create objects for 5 students. """


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


    def display_marks(self):
        print("Student Name:",self.name)
        print("MARKS:",self.marks)
       


    def check_result(self):
        if self.marks>= 40:
            result="PASS"
        else:
            result="FAIL"
        print(result)
       


s1 = Student("Rahul", 49)
s2 = Student("Sneha", 39)
s3 = Student("Kiran", 75)
s4 = Student("Priya", 35)
s5 = Student("Arjun", 50)


s1.display_marks()
s1.check_result()


s2.display_marks()
s2.check_result()


s3.display_marks()
s3.check_result()


s4.display_marks()
s4.check_result()


s5.display_marks()
s5.check_result()


"""output:--
Student Name: Rahul
MARKS: 49
PASS


Student Name: Sneha
MARKS: 39
FAIL


Student Name: Kiran
MARKS: 75
PASS


Student Name: Priya
MARKS: 35
FAIL


Student Name: Arjun
MARKS: 50
PASS"""


#==========================================================================================


"""7. Employee Bonus
Create a class Employee
with:
• name
• salary
Create a method
calculate_bonus().
Rules:
salary >= 50000 → 10% bonus
salary < 50000  → 5% bonus
Display: Employee Name Salary Bonus Total Salary """


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


        print("Employee name:",self.name)
        print("Salary:",self.salary)
       


    def calculate_bonus(self):
        if self.salary>= 50000:
            bonus=self.salary*0.10
        else:
            bonus=self.salary*0.05
        Total_Salary=self.salary+bonus


        print("Bonus:",bonus)
        print("Total Salary:",Total_Salary)
       


e1=Employee("Gnaneswhar",55000)
e1.calculate_bonus()


"""output:--
Employee name: Gnaneswhar
Salary: 55000
Bonus: 5500.0
Total Salary: 60500.0"""


#==========================================================================================


"""8. Product Discount
Create a class Product
with:
• product_name
• price  
Create a method
calculate_discount().
Rules:
price >= 5000 → 20% discount
price >= 2000 → 10% discount
otherwise → 5% discount
Display the final price. """


class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price


    def calculate_discount(self):
        if self.price >= 5000:
            discount=self.price*0.20
        elif self.price>= 2000:
            discount=self.price*0.10
        else:
            discount=self.price*0.05
        total = self.price - discount
        print("Product:",self.product_name)
        print("Final price:",total)
       


p1 = Product("Headphones", 3000)
p2 = Product("Keyboard", 1500)


p1.calculate_discount()
p2.calculate_discount()


"""output:--
Product: Headphones
Final price: 2700.0


Product: Keyboard
Final price: 1425.0"""


#==========================================================================================


"""9. ATM Transaction
Create a class ATM
with:
• account_number
• balance  
Create methods:
• deposit()
• withdraw()
• check_balance()  
The object should maintain the updated balance after every transaction."""


class ATM:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print("Balance:", self.balance)
       


    def deposit(self, amount):
        self.balance += amount
        print("Deposit Amount:", amount)
        print("Balance:", self.balance)
       


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdraw:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient Balance")
           


    def check_balance(self):
        print("Updated Balance:", self.balance)
       


a1 = ATM(963852741, 15000)
a1.deposit(5000)
a1.withdraw(2000)
a1.check_balance()  


"""output:--
Balance: 15000
Deposit Amount: 5000
Balance: 20000
Withdraw: 2000
Balance: 18000
Updated Balance: 18000"""


#==========================================================================================


"""10. Car Information
Create a class Car
with:
• brand
• model
• price
• fuel_type
Create methods:
• display()
• check_price()  
If price is greater than ₹10,00,000, display "Premium Car",
otherwise "Normal Car"."""


class car:
    def __init__(self,brand,model,price,fuel_type):
        self.brand=brand
        self.model=model
        self.price=price
        self.fuel_type=fuel_type


    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Fuel Type:", self.fuel_type)
       


    def check_price(self):
        if self.price>1000000:
            print("car range:","Premium Car")
        else:
            print("car range:","Normal Car")
           




c1 = car("Toyota", "Fortuner", 4500000, "Diesel")
c1.display()
c1.check_price()


c2 = car("Hyundai", "Creta", 900000, "Petrol")
c2.display()
c2.check_price()




"""output:--
Brand: Toyota
Model: Fortuner
Price: 4500000
Fuel Type: Diesel
car range: Premium Car
Brand: Hyundai
Model: Creta
Price: 900000
Fuel Type: Petrol
car range: Normal Car"""




#==========================================================================================
"""Level 3 – Multiple Methods """


"""11. Electricity Bill
Create a class ElectricityBill with:
• customer_name  
• units  
Create a method calculate_bill().
Use:
Units <= 100 → ₹2/unit  
101–200  → ₹3/unit        
201–300  → ₹5/unit    
Above 300  → ₹7/unit      
Create another method display_bill()."""


class ElectricityBill:
    def __init__(self,customer_name,units):
        self.customer_name=customer_name
        self.units=units


    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 2
        elif self.units <= 200:
            bill = self.units * 3
        elif self.units <= 300:
            bill = self.units * 5
        else:
            bill = self.units * 7
        print("total_bill:",bill)
       


    def display(self):
        print("customer name:",self.customer_name)
        print("Total units:",self.units)
       




e1=ElectricityBill("ramu",90)
e1.display()
e1.calculate_bill()


"""o/p:--
customer name: ramu
Total units: 90
total_bill: 180"""




#==========================================================================================


"""12. Library Book
Create a class Book with:
• title  
• author  
• price  
• available  
Create methods:
• display_book()  
• borrow_book()  
• return_book()  
When a book is borrowed, change availability to False."""


class Book:
    def __init__(self,title,author,price,available):
        self.title=title
        self.author=author
        self.price=price
        self.available=available


    def display_book(self):
        print("Book Title:",self.title)
        print("Auther Name:",self.author)
        print("Price:",self.price)
        print("availability:",self.available)
       


    def borrow_book(self):
        if self.available==True:
            self.available=False
            print("book was soldout")
        else:
            print("book is not avalable",self.title)
           


    def return_book(self):
        if self.available == False:
            self.available = True
            print("Book returned successfully")
        else:
            print("Book is already available")
           




book1=Book("Python Basics", "Guido", 500, True)
book1.display_book()
"""
Book Title: Python Basics
Auther Name: Guido
Price: 500
availability: True"""
book1.borrow_book()
"""book was soldout"""


book1.display_book()
"""Book Title: Python Basics
Auther Name: Guido
Price: 500
availability: False"""


book1.return_book()
"""Book returned successfully
"""
book1.display_book()
"""Book Title: Python Basics
Auther Name: Guido
Price: 500
availability: True"""




#==========================================================================================
"""
13. Shopping Cart
Create a class Product with:
• name  
• price  
• quantity  
Create methods:
• calculate_total()  
• display_product()  
Create 3 product objects and calculate the total shopping amount. """


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total(self):
        return self.price * self.quantity


    def display_product(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total:", self.calculate_total())
        print()


p1 = Product("Laptop", 50000, 1)
p2 = Product("Mouse", 500, 2)
p3 = Product("Keyboard", 1000, 1)


p1.display_product()
p2.display_product()
p3.display_product()
total_amount = (p1.calculate_total()+ p2.calculate_total()+ p3.calculate_total())
print("Total Shopping Amount:", total_amount)


"""o/p:
Product Name: Laptop
Price: 50000
Quantity: 1
Total: 50000


Product Name: Mouse
Price: 500
Quantity: 2
Total: 1000


Product Name: Keyboard
Price: 1000
Quantity: 1
Total: 1000


Total Shopping Amount: 52000"""


#==========================================================================================
"""14. Employee Performance
Create a class Employee with:
• name  
• salary  
• rating  
Create methods:
• display()  
• calculate_increment()
Rules:
rating >= 4.5 → 20% increment
rating >= 3.5 → 10% increment
rating < 3.5  → 5% increment """


class Employee:
    def __init__(self,name,salary,rating):
        self.name=name
        self.salary=salary
        self.rating=rating


    def display(self):
        print("NAME:",self.name)
        print("SALARY:",self.salary)
        print("RATING:",self.rating)
        print()


    def calculate_increment(self):
        if self.rating>= 4.5:
            increment = self.salary*20/100
        elif self.rating>= 3.5:
            increment = self.salary*10/100
        else:
            increment = self.salary*5/100


        print("increment:",increment)
        print("New_salary:",self.salary+increment)


e1 = Employee("Gnaneshwar", 50000, 4.7)
e1.display()
e1.calculate_increment()


"""NAME: Gnaneshwar
SALARY: 50000
RATING: 4.7


increment: 10000.0
New_salary: 60000.0"""
   


#==========================================================================================
"""15. Bank Account Validation
Create a class BankAccount with:
• account_holder  
• balance  
Create methods:
• deposit(amount)  
• withdraw(amount)  
• check_balance()  
Additional rule:
Minimum balance = ₹1000
A withdrawal should not be allowed if the remaining balance becomes less than ₹1000."""


class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance


    def deposite(self,amount):
        self.balance+=amount
        print("diposited amount:",amount)


    def withdraw(self,amount):
        if self.balance-amount>=1000:
            self.balance-=amount
            print("debited amount:",amount)
        else:
            print("transaction declined insufficient balance")
            print("maitain minimum balance ₹1000")


    def check_balance(self):
        print("Availble Balance:",self.balance)


account = BankAccount("Gnaneshwar", 5000)


account.check_balance()


account.deposite(2000)
account.check_balance()


account.withdraw(3000)
account.check_balance()


account.withdraw(4000)
account.check_balance()


"""output:
Availble Balance: 5000
diposited amount: 2000
Availble Balance: 7000
debited amount: 3000
Availble Balance: 4000
transaction declined insufficient balance
maitain minimum balance ₹1000
Availble Balance: 4000
"""


#==========================================================================================
"""Level 4 – Challenge Problems"""


""" 16. Online Food Order
Create a class FoodOrder with:
• customer_name  
• food_name  
• price  
• quantity  
Methods:
• calculate_total()  
• apply_discount()  
• display_order()  
Rules:
Total >= ₹2000 → 20% discount
Total >= ₹1000 → 10% discount
Otherwise      → No discount """


class FoodOrder:
    def __init__(self,customer_name,food_name,price,quantity):
        self.customer_name=customer_name
        self.food_name=food_name
        self.price=price
        self.quantity=quantity


    def calculate_total(self):
        self.total=self.price*self.quantity
        return self.total


    def apply_discount(self):
        if self.total<=2000:
            self.discount=self.total*0.20
        elif self.total>=1000:
            self.discount=self.total*0.10
        else:
            self.discount=0
        return self.discount


    def display_order(self):
        print("Customer name:",self.customer_name)
        print("Food name:",self.food_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total bill:",self.total)
        print("Discount gained:",self.discount)
        print("After discount bill:",self.total-self.discount)


   
f1 = FoodOrder("Gnaneshwar", "Pizza", 500, 5)
f1.calculate_total()
f1.apply_discount()
f1.calculate_total
f1.display_order()


"""output:
Customer name: Gnaneshwar
Food name: Pizza
Price: 500
Quantity: 5
Total bill: 2500
Discount gained: 250.0
After discount bill: 2250.0
"""


#==========================================================================================
"""17. Hospital Patient
Create a class Patient with:
• name  
• age  
• disease  
• bill  
Methods:
• display_patient()  
• add_bill(amount)  
• check_bill()  
Create multiple patient objects and update their bills. """


class Patient:
    def __init__(self,name,age,disease,bill):
        self.name=name
        self.age=age
        self.disease=disease
        self.bill=bill


    def display_patient(self):
        print("Patient Name:",self.name)
        print("Age:",self.age)
        print("Disease:",self.disease)
        print("bill:",self.bill)


    def add_bill(self,amount):
        self.bill+=amount
        print("Added Bill:",amount)


    def check_bill(self):
        print("Current bill:",self.bill)
        print()


p1 = Patient("Rahul", 25, "Fever", 5000)
p2 = Patient("Sneha", 30, "Cold", 3000)


p1.display_patient()
p1.add_bill(2000)
p1.check_bill()
p2.display_patient()
p2.add_bill(1500)
p2.check_bill()


"""
Patient Name: Rahul
Age: 25
Disease: Fever
bill: 5000
Added Bill: 2000
Current bill: 7000


Patient Name: Sneha
Age: 30
Disease: Cold
bill: 3000
Added Bill: 1500
Current bill: 4500
"""  


#==========================================================================================
"""18. Employee Attendance
Create a class Employee with:
• name  
• total_days  
• present_days  
Methods:
• attendance_percentage()  
• check_attendance()  
Rules:
Attendance >= 75% → Eligible
Attendance < 75%  → Not Eligible"""


class Employee:
   def __init__(self,name,total_days,present_days):
      self.name=name
      self.total_days=total_days
      self.present_days=present_days


   def attendance_percentage(self):
      Percentage=(self.present_days/self.total_days)*100
      print("Employee Name:",self.name)
      print("attendance_percentage:",Percentage,"%")


   def check_attendance(self):
      Percentage=(self.present_days/self.total_days)*100
      if Percentage>=75:
         print("Elgible")
      else:
         print("Not Elgible")


e1 = Employee("Ravi", 100, 80)
e1.attendance_percentage()
e1.check_attendance()


"""output:=
Employee Name: Ravi
attendance_percentage: 80.0 %
Elgible
"""  


#==========================================================================================
"""19. Movie Ticket Booking
Create a class MovieTicket with:
• movie_name  
• ticket_price  
• number_of_tickets  
Methods:
• calculate_total()  
• apply_discount()  
• display_ticket()  
Rules:
Tickets >= 5 → 10% discount
Otherwise    → No discount"""


class MovieTicket:
    def __init__(self,movie_name,ticket_price,number_of_tickets):
        self.movie_name=movie_name
        self.ticket_price=ticket_price
        self.number_of_tickets=number_of_tickets


    def calculate_total(self):
        self.total=self.number_of_tickets*self.ticket_price
        print("Total amount:",self.total)


    def apply_discount(self):
        if self.number_of_tickets>=5:
           discount=self.total*0.10
        else:
           discount=0


        self.final_price=self.total-discount
        print('Discoont:',discount)
        print("final Price:",self.final_price)


    def display_ticket(self):
        print("Movie name:",self.movie_name)
        print("ticket_price:",self.ticket_price)
        print("Number of Tickets:",self.number_of_tickets)


m1 = MovieTicket("RRR",250,5)
m1.display_ticket()
m1.calculate_total()
m1.apply_discount()


"""output:--
Movie name: RRR
ticket_price: 250
Number of Tickets: 5
Total amount: 1250
Discoont: 125.0
final Price: 1125.0
"""




# #==============================================================================================
"""20. Student Report Card
Create a class Student with:
• name  
• roll_no  
• python  
• sql  
• powerbi  
Create methods:
calculate_total()
calculate_average()
calculate_grade()
display_report()
Grade rules:
Average >= 90 → A
Average >= 75 → B
Average >= 60 → C
Average >= 40 → D
Below 40      → Fail """


class Student:
   def __init__(self,name,roll_no,python,sql,powerbi):
        self.name=name
        self.roll_no=roll_no
        self.python=python
        self.sql=sql
        self.powerbi=powerbi
       
   def calculate_total(self):
        self.total=self.python+self.sql+self.powerbi
        return self.total


   def calculate_average(self):
        self.avg=(self.total)/3
        return self.avg


   def calculate_grade(self):
        if self.avg >= 90:
            self.grade="A"


        elif self.avg >= 75:
            self.grade="B"


        elif self.avg>=60:
            self.grade="C"


        elif self.avg>=40:
            self.grade="D"


        else:
            self.grade="Fail"


   def display_report(self):
       print("Name:",self.name)
       print("Roll no:",self.roll_no)
       print("Python Marks:",self.python)
       print("Sql Marks:",self.sql)
       print("Powerbi Marks:",self.powerbi)
       print("Total Marks:",self.total)
       print("Average:",self.avg)
       print("Grade:",self.grade)
   
S1 = Student("GNANESHWAR", 101, 92, 82, 75)
S1.calculate_total()
S1.calculate_average()
S1.calculate_grade()
S1.display_report()


"""
output:
Name: GNANESHWAR
Roll no: 101
Python Marks: 92
Sql Marks: 82
Powerbi Marks: 75
Total Marks: 249
Average: 83.0
Grade: B
"""



