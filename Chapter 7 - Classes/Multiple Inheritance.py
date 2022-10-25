class Employee():
    def greet(self):
        print('Employee greets!')

class Person():
    def greet(self):
        print('Person greets!')

# If these two classes have nothing in common, it is okay to use multiple inheritance.
class Manager(Person, Employee):
    pass


manager = Manager()
manager.greet()
