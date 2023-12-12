
# To take input from the user
while True:
    num = int(input("Enter a number > 0: "))
    if num >0:
        break
    else:
        print("invalid input.Please enter a number >0.")
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print (num, "is an odd number.")

if num == 1:
    print(num, "is not a prime number")

    # check for number is a prime or not
# If given number is greater than 1
# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

