class User:

    def login(self):
        print("logging from parent")

    def register(self):
        print("register")

#Here student class is inheriting methods and variables of User class by mentioning its name in argument, if the variable or methods are private then they can't inherited, also if the contructor is not present in child but present in parent then parents constructor will be called when we create an object of child.

#Note: method overloading is not allowed in python but by using default arguments and conditions we can do the same work
class Student(User):

    def enroll(self):
        print("enrolled")

    #Super keyword helps in invoking methods & constructor from parent, so we can do half work from parent's constructor and other half from child's constructor 
    def login(self):
        print("logging from child")
        super().login()
    
    def review(self):
        print("reviewed")


s = Student()
s.login()