class Animal():
    def eat(self):
        print('eating!')

class Mamal(Animal):
    def walk(self):
        print('walking!')


class Fish(Animal):
    def swim(self):
        print('swimming!')


dog = Mamal()
ghezelala = Fish()

# dog.walk()
# ghezelala.swim()

print(isinstance(dog, Mamal))
print(isinstance(dog, Animal))
print(isinstance(dog, object))
print(issubclass(Mamal, object))
print(issubclass(Mamal, Animal))
