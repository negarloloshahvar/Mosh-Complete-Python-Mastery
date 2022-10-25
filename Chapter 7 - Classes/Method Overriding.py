class Animal():
    def __init__(self):
        print('Animal Constructor')
        self.age = 1

    def eat(self):
        print('eating!')

class Mamal(Animal):
    def __init__(self):
        print('Mamal Constructor')
        self.weight = 2
        super(Mamal, self).__init__()

    def walk(self):
        print('walking!')


class Fish(Animal):
    def swim(self):
        print('swimming!')

dog = Mamal()
print(dog.weight)
print(dog.age)