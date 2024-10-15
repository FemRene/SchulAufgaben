from pyfiglet import Figlet
import random
import sys

import UserManager


f = Figlet(font='slant')


def Lotto():
    print(f.renderText("Lotto"),"\n\n")
    lottozahlen_user = input("Choose your lottery numbers from 1 to 49: (6 pieces) ")
    zahlen_user: set[6] = set()
    if "," in lottozahlen_user:
        for zahl in lottozahlen_user.split(","):
            if int(zahl) in range(1, 50):
                zahlen_user.add(int(zahl))
            else:
                print("Only numbers between 1 and 49")
    if " " in lottozahlen_user:
        for zahl in lottozahlen_user.split(" "):
            if int(zahl) in range(1, 50):
                zahlen_user.add(int(zahl))
            else:
                print("Only numbers between 1 and 49")
    if len(zahlen_user) != 6:
        print("Please enter exactly 6 different numbers, separated by \",\" or \" \"")
        exit(-1)

    zahlen_system: set[6] = set()
    while len(zahlen_system) < 6:
        zahlen_system.add(random.randint(1, 49))

    print(zahlen_user)
    print(zahlen_system)

    anzahl_richtige_zahlen = 0
    richtige_zahlen = []
    for zahl in zahlen_system:
        if zahl in zahlen_user:
            anzahl_richtige_zahlen += 1
            richtige_zahlen.append(zahl)

    print("You had " + str(anzahl_richtige_zahlen) + " tips")
    print("Were correct: " + str(richtige_zahlen))


def Palindrome(wort):
    wort = wort.lower().replace(" ", "")
    return wort == wort[::-1]


def Users():
    cont: bool = True
    while cont:
        print(f.renderText("Usermanager"), "\n\n")
        action = input("Select a what would you do:\n"
                       "1)  List all Users\n"
                       "2)  Get User by ID\n"
                       "3)  Get User by Name\n"
                       "4)  Add new User\n"
                       "5)  Delete User by ID\n"
                       "6)  Delete User by Name\n"
                       "(1-6): ")

        match action:
            case "1":
                for user in UserManager.getAllUsers():
                    print(f"ID: {user[0]}\n"
                          f"last name: {user[1]}\n"
                          f"first name: {user[2]}\n"
                          f"birthday: {user[3]}\n"
                          f"adress: {user[4]}\n"
                          f"email: {user[5]}\n"
                          f"-----------------------------------------")
            case "2":
                id = input("Enter ID of the User: ")
                for user in UserManager.getUserByID(int(id)):
                    print(f"ID: {user[0]}\n"
                          f"last name: {user[1]}\n"
                          f"first name: {user[2]}\n"
                          f"birthday: {user[3]}\n"
                          f"adress: {user[4]}\n"
                          f"email: {user[5]}\n")
            case "3":
                name = input("Enter Name of the User: ")
                for user in UserManager.getUserByName(name):
                    print(f"ID: {user[0]}\n"
                          f"last name: {user[1]}\n"
                          f"first name: {user[2]}\n"
                          f"birthday: {user[3]}\n"
                          f"adress: {user[4]}\n"
                          f"email: {user[5]}\n")
            case "4":
                last_name = input("Enter Last Name: ")
                first_name = input("Enter First Name: ")
                birth_date = input("Enter Birth Date: ")
                adress = input("Enter Adress: ")
                email = input("Enter Email: ")
                UserManager.addUser(last_name, first_name, birth_date, adress, email)
                print("User created")
            case "5":
                id = input("Enter ID of the User: ")
                print(UserManager.deleteUserByID(int(id)))
            case "6":
                name = input("Enter Name of the User: ")
                print(UserManager.deleteUserByName(name))
            case _:
                cont = False


while True:
    print(f.renderText("Grundlagen Listen"), "\n\n")
    action = input("Select a what would you do:\n"
                   "1)  Play Lotto\n"
                   "2)  Check for Palindrome\n"
                   "3)  Usermanager\n"
                   "(1-3): ")
    match action:
        case "1":
            Lotto()
        case "2":
            print(f.renderText("Palindrome"), "\n\n")
            word = input("Enter your Word here: ")
            print(f"{word} is a Palindrome." if Palindrome(word) else f"{word} is not a Palindrome")
        case "3":
            Users()
        case _:
            sys.exit(-1)
