class Point:

# Defining a Class Attribute:
    default_color = 'Red'

# Defining an Instance Attribute:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Defining a Class Method:
    @classmethod
    def zero(cls):
        return cls(0, 0)

# Defining an Instance Method:
    def draw(self):
        print(f'Point ({self.x}, {self.y})')

# Magic Methods:
#     def __str__(self):
#         return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point.zero()
combined = point1 + point3


print(combined.x)