class Person:
    def __init__(self, f, l):
        self.first_name = f
        self.last_name = l
    def say_hi(self):
        print(f'Hi! My name is {self.first_name} {self.last_name}.')

person1 = Person('Negar', 'Shahvar')
person1.age = 26
person2 = Person('Abtin', 'Eslah')
person3 = Person('Narges', 'Shahvar')

print(person1.age)
