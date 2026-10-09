"""Tasks / Requirements"""
"""1.Define a class Book with an integer pages attribute
and overload the + operator to produce a new Book whose 
pages equals the sum of the two operands’ pages."""

from turtle import distance


class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,others):
        return book(self.pages+others.pages)
    
b1=book(100)
b2=book(150)
b3=b1+b2
print("total pages:",b3.pages)

"""total pages: 250"""


"""2.Define a class Employee with a numeric salary attribute and
overload the > operator to compare the salaries of two employees."""

class Employee:
    def __init__(self,salary):
        self.salary=salary
    def __gt__(self, other):
        return self.salary>other.salary

e1=Employee(15000)
e2=Employee(20000)
print(e1>e2)

"""False"""

        
"""3.Define a class Temperature with a numeric celsius attribute and
overload the - operator to return the numeric difference between two temperatures."""

class Temparature:
    def __init__(self,celsius):
        self.celsius=celsius
    def __sub__(self, other):
        return self.celsius-other.celsius
t1=Temparature(35)
t2=Temparature(26)
t3=t1-t2
print("Temparature Difference:",t3)

"""Temparature Difference: 9"""

"""4.Define a class Rectangle with length and width attributes
and overload the * operator so that multiplying two rectangles 
yields a numeric value equal to the product of their individual areas."""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __mul__(self, other):
        area1 = self.length * self.width
        area2 = other.length * other.width
        return area1 * area2

r1 = Rectangle(10, 5)
r2 = Rectangle(4, 3)

print("Product of Areas:", r1 * r2)

"""Product of Areas: 600"""

"""5.Define a class Time with hours and minutes attributes and 
overload the + operator to add two Time objects, normalizing 
minutes (e.g., 70 minutes becomes 1 hour 10 minutes)."""


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        total_minutes = (
            self.hours * 60 + self.minutes
            + other.hours * 60 + other.minutes)

        hours = total_minutes // 60
        minutes = total_minutes % 60

        return Time(hours, minutes)

    def display(self):
        print(self.hours, "hours", self.minutes, "minutes")

t1 = Time(1, 40)
t2 = Time(0, 30)

t3 = t1 + t2
t3.display()

"""output:---
2 hours 10 minutes"""

"""6.Define a class ShoppingCart that stores a collection of item prices and 
overload the + operator to combine two carts into a new cart containing all items from both."""

class ShoppingCart:
    def __init__(self,price):
        self.price=price

    def __add__(self, other):
        return self.price+other.price

cart1=ShoppingCart([5000,250,8999])
cart2=ShoppingCart([2999,459,999,669])
cart3=cart1+cart2

print("Combined Items:", cart3)
print("Total Price:", sum(cart3))

"""output:---
Combined Items: [5000, 250, 8999, 2999, 459, 999, 669]
Total Price: 19375"""

"""7.Define a class Distance with a numeric meters attribute and 
overload the +, -, and == operators to add, subtract, and compare distances respectively."""

class Distance:
    def __init__(self, meters):
        self.meters = meters

    def __add__(self, other):
        return Distance(self.meters + other.meters)

    def __sub__(self, other):
        return Distance(self.meters - other.meters)

    def __eq__(self, other):
        return self.meters == other.meters

    def display(self):
        print(self.meters, "meters")

d1 = Distance(100)
d2 = Distance(40)
d3 = Distance(100)

print("Addition:")
(d1 + d2).display()

print("Subtraction:")
(d1 - d2).display()

print("Equality:", d1 == d3)

"""output:--
Addition:
140 meters
Subtraction:
60 meters
Equality: True""" 


"""8.Define a class Vector with x and y numeric components and 
overload the +, -, and * operators to perform vector addition, subtraction, and compute the dot product (*)."""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def display(self):
        print(f"({self.x}, {self.y})")

v1 = Vector(3, 4)
v2 = Vector(2, 5)

print("Addition:")
(v1 + v2).display()

print("Subtraction:")
(v1 - v2).display()

print("Dot Product:", v1 * v2)

"""output:---
Addition:
(5, 9)
Subtraction:
(1, -1)
Dot Product: 26"""

