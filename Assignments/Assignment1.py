# Q1. Write a Python program using a class and constructor to accept two numbers and display their addition, subtraction, multiplication, and division. 
class MathOperations:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.add = n1 + n2
        self.subtract = n1-n2 if(n1 > n2) else n2-n1 #ternary operator : ValueTrue if(condition) else ValueFalse
        self.multiply = n1 * n2
        self.division = n1/n2
    
    def showResult(self):
        print("Q1 Math Operation:")
        print("n1= ", self.n1, " n2= ", self.n2)
        print("\n Addition= ", self.add, "\n Subtraction = ", self.subtract, "\n Multiplication= ", self.multiply, "\n Division= ", self.division)

n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
mo = MathOperations(n1, n2)
mo.showResult()

#Q2. Write a Python class to calculate and display the area and perimeter of a rectangle using constructor initialization.
class Rectangle:
    def __init__(self, w, l):
        self.area = w * l
        self.perimeter = 2*(w+l)

    def showRectangleResult(self):
        print("\n Perimeter Of Rectangle: ",self.perimeter, "\n Area of Rectangle: ", self.area)

w = int(input("Enter Width of Rectangle: "))
l = int(input("Enter Length of Rectangle: "))

rec = Rectangle(w,l)
rec.showRectangleResult();

#Q3. Write a Python class that calculates Simple Interest using the formula (P x R x T) / 100. Use constructor to accept P, R, and T. 
class CalculateInterest:
    def __init__(self, p, r, t):
        self.simpleInterest = (p * r* t)/100
        
    def showInterestResult(self):
        print("Simple Interest = ", self.simpleInterest)

p = int(input("Enter Principle: "))
r = int(input("Enter Rate of Interest: "))
t= int(input("Enter Tenure: "))

int1 = CalculateInterest(p,r,t)
int1.showInterestResult()

#Q4. Write a Python class named Circle to find the area and circumference of a circle using the radius given through constructor. 

class Circle:
    def __init__(self, r):
        pi = 3.141592653589793
        self.r = r
        self.area = pi * r * r
        self.circum = 2 * pi * r

    def showCircleResult(self):
        print("\n Area of Circle= ", round(self.area,2), "\n Circumference of Circle= ", round(self.circum,2))

r = int(input("Enter Radius of Circle:"))
circle = Circle(r)
circle.showCircleResult()

#Write a class TimeConvert with a constructor that accepts minutes and displays the equivalent hours and remaining minutes. 

class TimeConvert:
    def __init__(self, m):
        self.m = m
        self.calcHour = m//60
        self.calcMinute = m % 60

    def timeResult(self):
        print("\n Hours: ", self.calcHour, "\n Minutes: ", self.calcMinute)
        
m = int(input("Enter minutes to convert: "))
tm= TimeConvert(m)
tm.timeResult()