class Person:
    
    def __init__(self, name) -> None:
        self.name = name
        print(id(self))

# Here we are sending the reference to object 'cust' as argument and any changes made will be made to original object, we are printing ids to make sure we are referencing the same object, hence objects are mutable in nature

def change_name(personObj):
    personObj.name = "Ankita"
    print(personObj.name)
    print(id(personObj))

# cust = Person("Nitish")

# change_name(cust)

# Lists are also mutable so if we send reference of it and made some changes then it will reflect in original list as well, so if you want that no changes happen in original list then pass the copy of list like add_to_list(L[:])
def add_to_list(L1):
    L1.append(5)
    print(id(L1))

L = [1,2,3,4]
#print(id(L))

#add_to_list(L)
#print(L)


# Tuples are immutable so if we pass tuple and make some changes then it will not reflect in original one as we can see ids are different so we are actually sending the copy of tuple
def add_to_tuple(T1):
    T1 = T1 + (5,6)
    print(id(T1))

T = (1,2,3,4)
print(id(T))
add_to_tuple(T)
print(T)