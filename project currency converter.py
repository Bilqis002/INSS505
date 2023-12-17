# A function to convert between currencies

USD = 1.05
EUR = 1

print("Welcome to Team4 Converter \n"

      "Enter User ID")

# No of password attempts set after which User ID temporarily Disabled
attempts = 3

# id stored in system database to be called upon for authentication
id = 0000

# User is prompted to enter user_id, after 3 tries, user id is temporarily Disabled
while attempts > 0:
    user_id = int(input("Enter Your Four Digit user id:\n"))

    if user_id != id:
        attempts -= 1
        print("Invalid user id,Please Enter a valid user id!\n"
               "You have", attempts, "Tries left")

# If the correct user id is inputted then user get access and proceed go choose currency choice
    else:
        currency_choice = input(" Choose EUR as 1   \n")

        if EUR == 1:
            EUR = USD * int(input("Enter amount to convert:   €"))
            # balance += user input
            print("You have successfully converted $",EUR, "to your account\n")
            print("total amount is $", EUR, "balance")
            break
        else:
            print("Error")
            continue


# while True:
#     convert = EUR ** int(input("Enter Amount to Convert"))
#     if convert < 0:
#         print("Invalid input, Enter Valid Amount")