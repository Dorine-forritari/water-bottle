"""Create a class called Vector2D that has a constructor that takes two numbers, representing the x and y component of a two dimensional vector.
The class should have the following methods:
__str__: returns the string representation of the vector:
|x|
|y|
add(other) : method that adds another vector to the one that called this method
subtract(other) : method that subtracts one vector from another
scale(scalar) : method that scales a vector according to a scalar"""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"|{self.x}|\n|{self.y}|\n"

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y

    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar
