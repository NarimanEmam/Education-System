import re

class User:
    def __init__(self, id, username, password, full_name, email):
        self.id = id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.email = email

    def signIn(self):
        pass

    def signOut(self):
        print(f"{self.username} has logged out.")
        return "main_menu"

    def shutdownSystem(self):
        print("System is shutting down...")

    def checkEmail(self):
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            print("Email is valid.")
        else:
            print("Email is invalid.")
