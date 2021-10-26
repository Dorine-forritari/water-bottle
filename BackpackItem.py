# Write two classes: Backpack, and BackpackItem.

# The goal of Backpack is to store BackpackItem instances that you add to the Backpack, until you fill up the backpack.

# Based on the usage below, you should be able to figure out what you need:

# Hint: You should implement the __repr__ function in BackpackItem.

# Example usage:

# bp = Backpack(10)
# print(bp)
# bp.add(BackpackItem("Book", 7))
# print(bp)
# bp.add(BackpackItem("Laptop", 3))
# print(bp)
# bp.add(BackpackItem("Headphones", 2))
# print(bp)

# Corresponding output:

# Backpack(0/10): []
# Backpack(7/10): [BackpackItem(Book, 7)]
# Backpack(10/10): [BackpackItem(Book, 7), BackpackItem(Laptop, 3)]
# Maximum capacity would be exceeded!
# Backpack(10/10): [BackpackItem(Book, 7), BackpackItem(Laptop, 3)]

class BackpackItem:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def return_name_size(self):
        return (self.name, self.size)

    def __repr__(self):
        return f"BackpackItem({self.name}, {self.size})"
    


