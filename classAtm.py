class Atm:

    # Constructor

    # This 'self' is object itself, whenever we create an object of class and call any method inside the class then object sends itself as the argument for that method because a method cannot call other methods inside a class, only an Obj can call, so we need to give (self) to every method we create inside a class.
    
    def __init__(self) -> None:
        """Only gets called when a new obj of class is created, these are called magic methods in python which gets called on their own at their moment, they don't need to be called using objects."""

        #These are instance variables (pin,balance) as they are different for every object , also the variables which you don't want accessible to objects so that they can directly alter it should be kept private, hence we use __ before the variable name

        #Note that nothing is python is truly private you can still access the private variables using _Atm__balance format and alter it (Atm is class name)
        self.__pin = ""
        self.__balance = 0
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

    # For programmers we can add get and set variable methods so they can modify code additionally we can add our login in methods so the code doesn't crash, it is better than directly accessing the variables and altering it.
    def get_pin(self):
        print(self.__pin)

    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print(self.__pin)
        else:
            print("Not allowed")

    def change_pin(self):
        self.__pin = input("Enter your pin")
        print("Pin changed successfully!")

    def deposit_money(self):
        temp = input("Enter your pin")
        if(temp == self.__pin):
            amount = int(input("Enter amount to deposit"))
            self.__balance += amount
            print("Amount added successfully!")
        else:
            print("Wrong pin entered, try again.")

    def withdraw_cash(self):
        print("")
