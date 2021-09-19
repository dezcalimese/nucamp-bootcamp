def login(database, username, password):
    if username in database:
        if database[username] == password:
            print("\nWelcome back", username + "!")
            return username
        elif database[username] != password:
            print("Incorrect password for", username, ".")
            return ""
        else:
            print("User not found. Please register.")
            return ""


def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print("Username", username, "registered!")
        return username
