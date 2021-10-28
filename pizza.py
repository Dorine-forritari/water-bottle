# Write two classes Topping and Pizza.
# Topping:
# Each topping class must take two attributes, name and price.
# It has the following methods:
# __str__() : returns the name of the topping
# get_price() : returns the price of the topping
# Each attribute in the class must be private (self.__name = ...)
# Pizza:
# Pizza can take up to 3 arguments, name, size, and toppings. By default, the name 
# is "Unnamed", size is "large" and toppings is an empty list ([]).
# The size can only be "small", "medium" or "large", if any other size is given as 
# an argument, raise a ValueError with the message "Invalid size of pizza" 
# (this is simply done with raise ValueError("Invalid size of Pizza"))
 
# The class should have the following methods:
# __str__() : returns the string "{size} {name} pizza with {toppings separated by ", "}"
# if there are no toppings the function should return "{size} {name} pizza with nothing
# add_topping(topping) : Adds a topping item to the pizza class (should be stored in a list)
# add_toppings(toppings): Takes a list of toppings and adds every topping to the pizza
# get_price(): returns the total price of the pizza (depends on pizza size and toppings).
# Base prices for pizza:
# small: 800
# medium: 1200
# large: 1500
# (you might want to use a dict for this)
 

# You should practice implementing classes in their own separate files, please do so for this assignment.

# Example usage:

# pizza = Pizza()
# print(pizza)

# ham_topping = Topping("ham", 200)
# pineapple_topping = Topping("topping", 300)

# hawaiian_pizza = Pizza("Hawaiian", "medium", [ham_topping, pineapple_topping])
# print(hawaiian_pizza)
# hawaiian_pizza.add_topping(Topping("Ton of pineapple", 1000))
# print(hawaiian_pizza)
# print(hawaiian_pizza.get_price())
# Corresponding output:

# Large Unnamed pizza with nothing
# Medium Hawaiian pizza with ham, topping
# Medium Hawaiian pizza with ham, topping, Ton of pineapple
# 2700

# class Topping():
#     def __init__(self, name, price) -> None:
#         self.__name = name
#         self.__price = price

#     def __str__(self) -> str:
#         return f"Topping({self.__name}, {self.__price})"

#     def get_price(self):
#         return self.__price
from topping import Topping

class Pizza:
    def __init__(self, name="Unnamed", size="large", toppings=[]) -> None:
        self.legal_sizes = ["small", "medium", "large"]
        self.name = name
        if size in self.legal_sizes:
            self.size = size
        else:
            raise ValueError("Invalid size of Pizza")
        self.toppings = toppings

    def __str__(self) -> str:
        if self.toppings:
            toppings_str = ""
            for topping in self.toppings:
                toppings_str += str(topping) + ", "
            toppings_str = toppings_str[:-2]
            size_str = self.size.capitalize()
            return f"{size_str} {self.name} pizza with {toppings_str}"
        else:
            size_str = self.size.capitalize()
            return f"{size_str} {self.name} pizza with nothing"
    
    def add_topping(self, topping):
        self.toppings.append(topping)

    def add_toppings(self, toppings):
        self.toppings.extend(toppings)

    def get_price(self):
        sizes_dict = {
            "small": 800,        
            "medium": 1200,
            "large": 1500
        }
        total_price = sizes_dict[self.size]
        for topping in self.toppings:
            total_price += topping.get_price()
        return total_price


my_pizza = Pizza("delicious", "small")
my_pizza.add_topping(Topping("apple", 500))
print(my_pizza)



    