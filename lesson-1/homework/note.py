#1.Given a side of square. Find its perimeter and area.
a = int(input('enter the side length of square '))
Perimeter = 4 * a
Area = a ** 2
print('the perimeter of the  square is ', Perimeter)
print('the area of the square is ', Area)

#2.Given diameter of circle. Find its length.
diameter =int(input('enter the diameter of the circle '))
import math
C = diameter * math.pi
print('the lenght of the circle is ', C)

#3.Given two numbers a and b. Find their mean.
a = int(input('enter the first number '))
b = int(input('enter the second number '))
Mean = (a + b) / 2
print('the mean of numbers is', Mean)

#4.Given two numbers a and b. Find their sum, product and square of each number.
a = int(input('enter the first number '))
b = int(input('enter the second number '))
sum = a + b
product = a * b
square1 = a **2
square2 = b **2
print('the sum of numbers is ', sum)
print('the product of numbers is ', product)
print('the square of first number is ', square1)
print('the square of second number is ', square2)
