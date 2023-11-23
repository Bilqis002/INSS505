product1=int(input("Enter product1:"))
for product1 in range(1,product1):
    if(product1%3==0) and (product1%5==0):
        print(product1,"Tic Tac")
    if(product1%3==0):
        print(product1,"Tic")
    if(product1%5==0):
        print(product1,"Tac")

for product1 in range(1,product1):
    if(product1%3==0) and (product1%5==0):
        print(product1,"Tic Tac")
    if(product1%3==0):
        print(product1,"Tic")
    if(product1%5==0):
        print(product1,"Tac")

#using while loop statement to print numbers 1-20

i=0
while i < 20:
    i = i + 1
    print(i)
input1=int(input('Enter input1:'))
input1=1
#using while loop
while input1<16:
    input1+=1
    if input1%3==0 and input1%5==0:
        print(input1,"Tic Tac")
    elif input1%3==0:
        print(input1,"Tic")
    elif input1%5==0:
        print(input1,"Tac")
#step8
import random
value=0
if value > 0:
    random_value = random.randint(20, 40)
    print("Random number:", random_value)

#step9
import random
count = 0
value = 0
while count < 5 and value <= 0:
    value = int(input("Enter a positive number: "))
    if value <= 0:
        print("Invalid input. Try again.")
    count = count + 1
if value > 0:
    random_value = random.randint(1, 10)
    if value == random_value:
        print("Perfect match!")
    else:
        print("The numbers don't match.")
        print("Your number:", value)
        print("Random number:", random_value)
else:
    print("You have exceeded the maximum number of attempts.")
