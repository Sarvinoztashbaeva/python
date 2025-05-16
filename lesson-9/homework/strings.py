class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __int__(self):
            return int(self.radius)
    def area(self):
        pi = 3.14
        area = pi * int(self)**2
        return area
    def perimeter(self):
        pi = 3.14
        perimeter = pi * int(self)*2
        return perimeter

from datetime import date
class Person:
    def __init__(self, name, country, date_of_birth: date):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def get_age(self):
        return date.today().year-self.date_of_birth.year

class Calculator:
    def add(self, a:int, b:int):
        return a + b
    def subtract(self, a:int, b:int):
        return a - b
    def multiply(self, a:int, b:int):
        return a * b
    def divide(self, a:int, b:int):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b

import math
class shapes():
    def perimetr():
        pass
    def area():
        pass
class circle(shapes):
    def area(self, rad:int):
        return 3.14*rad**2
    def perimetr(self, rad:int):
        return 3.14*rad*2
class triangle(shapes):
    def perimeter(self,a:int,b:int,c:int):
        return a+b+c
    def area(self, a:int,b:int,c:int):
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area
class squeare(shapes):
    def area(self,a:int,b:int):
        return a*b
    def perimetr(self, a:int, b:int):
        return (a+b)*2








