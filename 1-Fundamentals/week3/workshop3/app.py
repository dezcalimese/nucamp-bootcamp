from donations_pkg.homepage import show_homepage
from donations_pkg.homepage import donate
from donations_pkg.homepage import show_donations
from donations_pkg.user import login
from donations_pkg.user import register

database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)

    option = input("Choose an option: ")
    if option == "1":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
        if authorized_user == login(database, username, password):
            print("Logged in as:", username)
    elif option == "2":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user == register(database, username)
        if authorized_user != "":
            database[username] = password
        elif authorized_user == register(database, username):
            print("Logged in as:", username)
    elif option == "3":
        if authorized_user == "":
            print("\nYou are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif option == "4":
        show_donations(donations)
    elif option == "5":
        print("\nLeaving DonateMe")
        break
