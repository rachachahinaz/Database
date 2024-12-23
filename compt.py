class Compt:
    def __init__(self, db):
        self.db = db
        self.user_id = None

    def sign_up(self):
        name = input("Enter your name: ")
        gmail = input("Enter your Gmail: ")
        password_name = input("Enter your name password: ")
        password_gmail = input("Enter your Gmail password: ")
        self.db.add_user(name, gmail, password_name, password_gmail)

    def login(self):
        identifier = input("Enter your name or Gmail: ")
        password = input("Enter your password: ")
        use_gmail = "@" in identifier
        user = self.db.get_user(identifier, password, use_gmail)
        if user:
            self.user_id = user[0]
            print(f"Welcome back, {user[1]}!")
        else:
            print("Invalid name/Gmail or password !")
