# Implement three classes, Shape, Rectangle (which inherits from Shape), and Square (which inherits from Rectangle).

# Implement the member methods get_area() and get_perimeter() on Rectangle and Square (hint: you only have to write 
# the functions once such that it works for both Rectangle and Square).

# Here are a few items you should have in mind:

#     Only implement the __str__ function in the Shape class:
#         Have it return "{name of class} with area of {area} and perimeter of {perimeter}".
#         To get the name of the class you can use type(self).__name__
#     The constructor of Shape can be more or less empty (using the pass statement)
#     The Shape class should not implement the get_area and get_perimeter functions
#     The __str__ function should output all numbers rounded to 2 places.



class Shape:

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with area of {self.area:.2f} and perimeter of {self.perimeter:.2f}"






