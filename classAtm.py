class Atm:

    # Constructor

    # This 'self' is object itself, whenever we create an object of class and call any method inside the class then object sends itself as the argument for that method because a method cannot call other methods inside a class, only an Obj can call, so we need to give (self) to every method we create inside a class.
    
    def __init__(self) -> None:
        """Only gets called when a new obj of class is created, these are called magic methods in python which gets called on their own at their moment, they don't need to be called using objects."""
        self.pin = ""
        self.balance = 0
        self.choice()

    def choice(self):
        user_input = int(input("""Enter 1 to change PIN.\nEnter 2 to deposit money.\nEnter 3 to withdraw cash.
        """))

        if user_input == 1:
            self.change_pin()
        elif user_input == 2:
            self.deposit_money()
        elif user_input == 3:
            self.withdraw_cash()
        else:
            print("Invalid choice")

    def change_pin(self):
        self.pin = input("Enter your pin")
        print("Pin changed successfully!")

    def deposit_money(self):
        temp = input("Enter your pin")
        if(temp == self.pin):
            amount = int(input("Enter amount to deposit"))
            self.balance += amount
            print("Amount added successfully!")
        else:
            print("Wrong pin entered, try again.")

    def withdraw_cash(self):
        print("")
