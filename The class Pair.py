# Write the class Pair which encapsulates two values val1 and val2  and initializes them to 0 by default.  
# When two instances of this class are added together using the '+' operator, 
# the result is a new Pair, where val1 is the sum of the val1 of instances 1 and 2, and likewise for val2..

# The class should also support the '*' operator, where the result is a new Pair, 
# where val1 is the product of the val1 of the instances of 1 and 2, and likewise for val2.

# Example usage:

# Example usage:

# pair1 = Pair(20,30)
# print(pair1)
# pair2 = Pair(40,50)
# pair3 = pair1 + pair2
# print(pair3)
# pair4 = pair1 * pair2
# print(pair4)
# Corresponding output:

# Value 1: 20, Value 2: 30
# Value 1: 60, Value 2: 80
# Value 1: 800, Value 2: 1500
# You should only submit the class code.

class Pair:
    def __init__(self, val1=0, val2=0):
        self.val1 = val1
        self.val2 = val2

    def __add__(self, other):
        new_val1 = self.val1 + other.val1
        new_val2 = self.val2 + other.val2
        return Pair(new_val1, new_val2)

    def __mul__(self, other):
        new_val1 = self.val1 * other.val1
        new_val2 = self.val2 * other.val2
        return Pair(new_val1, new_val2)

    def __str__(self):
        return f"Value 1: {self.val1}, Value 2: {self.val2}"


pair1 = Pair(20,30)
print(pair1)
pair2 = Pair(40,50)
pair3 = pair1 + pair2
print(pair3)
pair4 = pair1 * pair2
print(pair4)