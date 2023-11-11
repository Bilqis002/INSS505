#count from 0 to 10
for b in range(0,11):
    print(b)

#count from 1 to 10
for count in range(1,11):
    print(count)

#count from 1 to 10 with increment +2
for passcode in range(1,10,2):
    print(passcode,end="")

#import math
import math
radius=float(input("Enter the radius for a circle:"))
math.pi
if radius>0:
    area = ((math.pi * radius ** 2))
    print("the area of a circle with radius",radius,"is:",area)
else:
    print("the radius entered is not greater than 0. Cannot compute area of circle")
#logic for area of rectangle
length=float(input("Enter the length of rectangle:"))
width=float(input("Enter the width of rectangle:"))
if length > 0 and width > 0:
    area= length * width
    print("the area of rectangle with length",length,"and width", width,"is:",area)
else:
    print("the length and/or width entered is not greater than 0. Cannot compute area of rectangle")