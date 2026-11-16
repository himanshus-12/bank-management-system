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
        while True:
            alpha = random.choices(string.ascii_letters, k=3)
            num = random.choices(string.digits, k=3)
            spchar = random.choices("!@#$%^&*", k=1)
    
            id = alpha + num + spchar
            random.shuffle(id)
    
            accountNo = "".join(id)
    
            if not any(i['accountNo'] == accountNo for i in cls.data):
                return accountNo

    # Create account
    def Createaccount(self):

        try:
            name = input("Tell your name:- ").strip()
            age = int(input("Tell your age:- "))
            email = input("Tell your email:- ").strip()
            pin = input("Tell your pin:- ")

        except ValueError:
            print("Invalid input. Please enter age correctly.")
            return

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }

        if (
            not name                    
            or age < 18                 
            or age > 120
            or len(pin) != 4
            or not pin.isdigit()
            or "@" not in email
            or email.startswith("@")
            or email.endswith("@")
        ):
            print("Sorry, you cannot create your account")
            return



        print("\nAccount has been created successfully")

        for i in info:
            if i != 'pin':
                print(f"{i} : {info[i]}")

        print("\nPlease note down your account number")

        Bank.data.append(info)
        Bank.__update()

    # Deposit money
    def depositmoney(self):

        accnumber = input("Please enter your account number:- ")
        pin = input("Please enter your pin:- ")
        

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            try:
                amount = int(input("Enter amount to deposit:- "))
            except ValueError:
                print("Please enter a valid amount")
                return

            if amount > 10000 or amount <= 0:
                print(
                    "Sorry, you can only deposit an amount between 1 and 10000"
                )

            else:
               
                userdata[0]['balance'] += amount

                Bank.__update()

                print("Amount deposited successfully")


    #Withdraw

    def withdraw(self):

        accnumber = input("Please enter your account number:- ")
        pin = input("Please enter your pin:- ")

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            try:
                amount = int(input("Enter amount to withdraw:- "))
            except ValueError:
                print("Please enter a valid amount")
                return

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
        pin = input("Please enter your pin:- ")

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            print("\nYour account details are as follows:")

            for i in userdata[0]:
                if i != 'pin':
                    print(f"{i} : {userdata[0][i]}")


    #Update details
    
    def update(self):

        accnumber = input("Please enter your account number:- ")
        pin = input("Please enter your pin:- ")

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            print("\nYour current account details are as follows:")

            for i in userdata[0]:
                if i != 'pin':
                    print(f"{i} : {userdata[0][i]}")

            field = input("\nEnter the field you want to update:- ")

            allowed_fields = ['name', 'age', 'email', 'pin']

            if field not in allowed_fields:
                print("Invalid field. Please try again.")
                return

            new_value = input(f"Enter the new value for {field}:- ").strip()

            if field == 'name':
                if not new_value:
                    print("Name cannot be empty")
                    return

            elif field == 'age':
                try:
                    new_value = int(new_value)
                except ValueError:
                    print("Invalid age")
                    return

                if new_value < 18 or new_value > 120:
                    print("Invalid age")
                    return

            elif field == 'email':
                
                if (
                    "@" not in new_value
                    or new_value.startswith("@")
                    or new_value.endswith("@")
                ):
                    print("Invalid email")
                    return

            elif field == 'pin':
                if len(new_value) != 4 or not new_value.isdigit():
                    print("PIN must contain exactly 4 digits")
                    return

            userdata[0][field] = new_value

            Bank.__update()

            print("Account details updated successfully")   


    def delete(self):
        accnumber = input("Please enter your account number:- ")
        pin = input("Please enter your pin:- ")

        userdata = [
            i for i in Bank.data
            if i['accountNo'] == accnumber and i['pin'] == pin
        ]

        if not userdata:
            print("Sorry, no data found")

        else:
            if userdata[0]['balance'] > 0:
                print("Please withdraw your remaining balance before deleting.")
                return

            confirm = input("Are you sure you want to delete your account? (yes/no):- ")

            if confirm.lower().strip() == 'yes':
                Bank.data.remove(userdata[0])
                Bank.__update()
                print("Account deleted successfully")

            else:
                print("Account deletion cancelled")



#DashBoard

# Create Bank object
user = Bank()


# Dashboard
while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("Press 1 for creating an account")
    print("Press 2 for depositing money")
    print("Press 3 for withdrawing money")
    print("Press 4 for details")
    print("Press 5 for updating the details")
    print("Press 6 for deleting your account")
    print("Press 7 for exit")

    try:
        check = int(input("Tell your response:- "))

    except ValueError:
        print("Please enter a valid number")
        continue

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



