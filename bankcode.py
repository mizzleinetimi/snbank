 import random
import os
from datetime import datetime


def options():
    firstChoice = input(
        "Input  number to select an option\n\t1 Staff Login\n\t2 Close App\n\t> ")
    if firstChoice == '1':
        username = input("Enter Username: ")
        password = input("Enter  Password: ")

        def check_password(username, password, lines):
            for line in lines:
                if username in line and password in line:
                    session = open("session.txt", "x")
                    dateTimeObj = str(datetime.now())
                    session.write(dateTimeObj)
                    session.close()

                    def optionFour():
                        login = input("Input  number to select an option\n\t1 Create bank account\n\t2 Check Account details\n\t3 Logout\n\t> ")
                        if login == '1':
                            accountName = input("Enter account name: ")
                            def balance():
                                global openingBalance
                                openingBalance = input("Enter opening balance: $")
                            
                                if openingBalance.isdigit():
                                    openingBalance = openingBalance
                                else:
                                    print("Opening balance must be a whole number\n")
                                    balance()
                            balance()
                            accountType = input("Enter account type: ")
                            accountEmail = input("Enter account e-mail: ")
                            global accountNumber
                            accountNumber = random.randrange(1000000000,10000000000)

                            customer = open("customer.txt","w")
                            customer.write("Account Name: %s Opening Balance: %s Account Type: %s Account Email: %s Account number: %d\n" % (accountName, openingBalance, accountType, accountEmail, accountNumber))
                            customer.close()
                            print(f"Your account number is {accountNumber}\n")
                            optionFour()
                        elif login == '2':
                            def loginTwo():
                                checkAccount = input("Input your account number: ")
                                if checkAccount == str(accountNumber):
                                    customer = open("customer.txt","r")
                                    cusread = customer.read()
                                    print(cusread)
                                    customer.close()
                                    optionFour()
                                else:
                                    print("wrong account number try again.\n")
                                    loginTwo()
                            
                            loginTwo()
                        elif login == '3':
                            os.remove("session.txt")
                            options()

                    optionFour()


                else:
                    print("Username or Password incorrect try again.\n")
                    options()
                    

        check_password(username, password, open('staff.txt').readlines())
    elif firstChoice == '2':
        exit(0)
    else:
        print("Please Select a valid option\n")
        options()


options()
