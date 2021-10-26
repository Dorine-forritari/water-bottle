# Write a class called Square. A Square should have one private (meaning two underscores as a prefix) 
# attribute that represents the length of any of its sides (only need one attribute as all sides of a 
# square are equally long).
# You should be able to create a Square instance by supplying a value for its side. 
# If no arguments are given the default value 1 should be set. Also, 
# if a number <= 0 is passed as an argument it should default to 1.

# You should implement the following methods in the class:

# area() returns the area of the square.
# perimeter() returns the perimeter of the square.
# __str__() which should print the length of its side like this "Side length: 2" where 2 
# is the value that was supplied when the Square instance was constructed.
# You should be able to check whether two Square instances are equal by using the == operator. 
# I'm going to leave it up to you to figure out under what circumstances two squares should be considered equal.

# You should also implement the __repr__() method. If a Square has a side of 10, 
# then this method should return a string like this: "Square(10)"


class Square:
    def __init__(self, side=1) -> None:
        if side <= 0:
            side = 1
        self.__side = side


    def __str__(self):
        return f"Side length: {self.__side}"
    

    def __repr__(self):
        return f"Square({self.__side})"


    def area(self):
        new_area = self.__side * self.__side
        return new_area
    

    def perimeter(self):
        new_parimeter = self.__side * 4
        return new_parimeter


    def __eq__(self, other):
        return self.__side == other.__side
             

sq1 = Square(10)
sq2 = Square(10)
print(sq1)
print(sq1.area())
print(sq1.perimeter())
print(sq1.__repr__())
print(sq1 == sq2)