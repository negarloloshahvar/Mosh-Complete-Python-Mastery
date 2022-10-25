from collections import namedtuple

#Point is type, something like a class.
Point = namedtuple('Point', ['x', 'y'])

# This is a Class Method
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


p1 = Point(x= 1,y= 2)
p2 = Point(1, 3)

#Point type objects are immutable.
p1.x = 4
print(p1.x)

print(p1 == p2)

print(id(p1))
print(id(p2))