import sys


class ChatBook:
    """
    A simple command-line based chat application that allows users to register, login, compose posts, and send text messages.
    Methods
    -------
    __init__():
        Initializes the ChatBook instance and starts the menu.
    menu():
        Displays the main menu and handles user input for different actions.
    register():
        Prompts the user to enter a username and password to register.
    login():
        Prompts the user to enter their username and password to login.
    compose():
        Allows a logged-in user to compose a post.
    text():
        Allows a logged-in user to send a text message to a recipient.
    """

    def __init__(self):
        self.username = None
        self.password = None
        self.logged_in = False
        self.menu()

    def menu(self):
        user_input = input("""
    Welcome to ChatBook
            1. Register
            2. Login
            3. Compose
            4. Text
            5. Exit
        Enter your choice: """)

        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.compose()
        elif user_input == "4":
            self.text()
        else:
            exit()

    def register(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.username = username
        self.password = password
        print(f"You have successfully registered as {username}\n")
        self.menu()

    def login(self):
        if self.username == None and self.password == None:
            print('User not registered, kindly Register')
            self.menu()
        else:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username == self.username and password == self.password:
                self.logged_in = True
                print(f"Welcome {username}")
                self.menu()

            else:
                print(f"⚠️ Invalid username or password; Retry\n")
                self.login()

    def compose(self):
        if self.logged_in == False:
            print("You need to login first...\n")
            self.menu()
        else:
            msg = input("What's on your mind?\n...")
            print(f"Your post 👇\n{msg}")
            self.menu()

    def text(self):
        if self.logged_in == False:
            print("⚠️ You need to login first....\n")
            self.menu()
        else:
            recipient = input('Who do you want to send the message to? \n')
            msg = input("Enter your message:\n")
            print(f"✅ Message sent to {recipient}.\n")
            self.menu()


obj = ChatBook()
