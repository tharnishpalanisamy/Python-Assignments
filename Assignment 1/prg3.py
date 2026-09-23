print("Welcome to our Atm")

users = {
    1234 : {
        "name" : "tharnish",
        "balance" : 20000.00
    }
}

attempts = 0
authorized = False
while attempts < 3:
    pin = int(input("Enter your PIN: "))

    if pin in users:
        authorized = True
        break

    attempts += 1
    print("Incorrect PIN")

if authorized :
    user = users[pin]
    is_using = True
    print(f"Welcome Back {user['name']}\n")
    while is_using :
        choice = int(input(f""
                           f"press 1 to check Balance\n"
                           f"press 2 to deposit\n"
                           f"press 3 to withdraw\n"
                           f"press 4 to change pin\n"
                           f"press 0 to Exit : "))

        match choice :
            case 0 :
                print("Thank you for Banking with us")
                break

            case 1 :
                print(f"Your Account Balance is : {user['balance']}")
            case 2 :
                while True :
                    amount = float(input("Enter the amount you want to deposit: "))
                    if amount <= 0 :
                        print("Please enter a positive number")
                        continue
                    else :
                        user["balance"] += amount
                        print("Successfully deposited " + str(amount))
                        print('Your current Balance : ' + str(user["balance"]))
                        break
            case 3 :

                while True :
                    amount = float(input("Enter the amount you want to withdraw: "))
                    if amount <= 0 :
                        print("Please enter a positive number")
                        continue
                    elif amount > user["balance"] :
                        print("Insufficient Balance")
                        continue
                    else:
                        user["balance"] -= amount
                        print("Successfully withdrawn " + str(amount))
                        print('Your current Balance : ' + str(user["balance"]))
                        break
            case 4 :
                while True :
                    new_pin = int(input("Enter your new PIN: "))
                    if new_pin < 1000 or new_pin > 9999 :
                        print("Please enter a valid PIN (1000 - 9999)")
                        continue
                    else:
                        del users[pin]
                        users[new_pin] = user
                        pin = new_pin
                        print('Pin successfully Changed ')
                        break

            case _ :
                print("Please Select a valid Choice")








