import os.path
from os import path

if not path.exists("userList.txt"):
    uFile = open("userList.txt", "x")

uFile = open("userList.txt", "a+")

userList = open("userList.txt").read().splitlines()

def printUsers():
    if userList:
        print(userList)

def login():
    try:
        userName = input("Login, enter new for account creation:")
    except Exception as e:
        print(str(e))

    if userName.lower() == "new":
        newUser(userName)
    elif userName.title() == "Admin":
        try:
            listPrint = input("Hello, {}. Would you like to see a user list?\n".format(userName.title()))
        except Exception as e:
            print(str(e))
        if listPrint[0].lower() == 'y':
            printUsers()
            uFile.close()
            return 0
        else:
            print("GoodBye.")
            uFile.close()
            return 0
    elif userName in userList:
        print("Welcome back {}.".format(userName.title()))
    else:
        print("Not a valid user.")
        setup(userName)

def newUser(name):
    reading = True
    while reading:
        if name.lower() == "new":
            try:
                userName = input("Enter your new username: ")
            except Exception as e:
                print(str(e))
        else:
            userName = name

        if userName.lower() == "new":
            print("New is not a valid username. Please try another.")
            name = "new"
            continue
        elif userName in userList:
            print("That username is already taken. Please try another.")
            name = "new"
            continue
        else:
            print("That username is available. Creating account.")
            uFile.write(userName)
            uFile.write("\n")
            userList.append(userName)
            reading = False
            login()

def setup(name):
    try:
        validate = input("Would you like to setup a new account? ")
    except Exception as e:
        print(str(e))

    if validate[0].lower() == 'n':
        print("Good Bye.")
        uFile.close()
    else:
        newUser(name)

if userList:
    login()
else:
    print("No users provisioned. Please Create new user.")
    newUser("new")