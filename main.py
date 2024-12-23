from Database import Database
from compt import Compt


def main():
    db = Database()
    planner = Compt(db)

    print("Connected successfully!")
    print("Program is started...")

    while True:
        print("\n1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option please : ")

        if choice == "1":
            planner.sign_up()
        elif choice == "2":
            planner.login()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. try again")

if __name__ == "__main__":
    main()