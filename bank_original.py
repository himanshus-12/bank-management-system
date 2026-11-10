import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    # Load existing data from JSON file
    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.load(fs)
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occurred as {err}")

    # Update JSON file
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    # Generate account number
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)

        id = alpha + num + spchar

        random.shuffle(id)

        return "".join(id)

    # Create account
    def Createaccount(self):

        info = {
            "name": input("Tell your name:- "),
            "age": int(input("Tell your age:- ")),
            "email": input("Tell your email:- "),
            "pin": int(input("Tell your pin:- ")),
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }

        
        if (
            info['age'] < 18
            or len(str(info['pin'])) != 4
            or "@" not in info['email']
        ):
            print("Sorry, you cannot create your account")

        else:
            print("\nAccount has been created successfully")

            for i in info:
                print(f"{i} : {info[i]}")

            print("\nPlease note down your account number")

            
            Bank.data.append(info)

           
            Bank.__update()

    # Deposit money
    def depositmoney(self):

        accnumber = input("Please enter your account number:- ")
        pin = int(input("Please enter your pin:- "))

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            amount = int(input("Enter amount to deposit:- "))

            if amount > 10000 or amount <= 0:
                print(
                    "Sorry, you can only deposit an amount between 1 and 10000"
                )

            else:
               
                userdata[0]['balance'] += amount

                Bank.__update()

                print("Amount deposited successfully")

    def withdraw(self):
        accnumber = input("Please enter your account number:- ")
        pin = int(input("Please enter your pin:- "))

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            amount = int(input("Enter amount to withdraw:- "))

            if amount > userdata[0]['balance'] or amount <= 0:
                print(
                    "Sorry, you can only withdraw an amount between 1 and your current balance"
                )

            else:
                userdata[0]['balance'] -= amount

                Bank.__update()

                print("Amount withdrawn successfully")




    def showdetails(self):
        accnumber = input("Please enter your account number:- ")
        pin = int(input("Please enter your pin:- "))

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            print("\nYour account details are as follows:")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")




    def update(self):
        accnumber = input("please enter your account number:-")
        pin = int(input("please enter your pin:-"))

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            print("\nYour current account details are as follows:")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")

            # Ask user for the field to update
            field = input("\nEnter the field you want to update:- ")
            if field in userdata[0]:
                new_value = input(f"Enter the new value for {field}:- ")
                userdata[0][field] = new_value
                Bank.__update()
                print("Account details updated successfully")
            else:
                print("Invalid field. Please try again.")   


    def delete(self):
        accnumber = input("Please enter your account number:- ")
        pin = int(input("Please enter your pin:- "))

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            Bank.data.remove(userdata[0])
            Bank.__update()
            print("Account deleted successfully")





# Create Bank object
user = Bank()


#DashBoard
while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("Press 1 for creating an account")
    print("Press 2 for depositing money")
    print("Press 3 for withdrawing money")
    print("Press 4 for details")
    print("Press 5 for updating the details")
    print("Press 6 for deleting your account")
    print("Press 7 for exit")

    check = int(input("Tell your response:- "))

    if check == 1:
        user.Createaccount()

    elif check == 2:
        user.depositmoney()

    elif check == 3:
        user.withdraw()

    elif check == 4:
        user.showdetails()  

    elif check == 5:
        user.update()

    elif check == 6:
        user.delete()

    elif check == 7:
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice. Please try again.")


