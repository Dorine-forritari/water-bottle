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

from BackpackItem import BackpackItem

class Backpack:

    def __init__(self, max_cap):
        self.list = []
        self.max_cap = max_cap
        self.itemsize = 0
        self.current_cap = 0

    def check_capacity(self):
        if (self.current_cap + self.itemsize) > self.max_cap:
            print("Maximum capacity would be exceeded!")
            return True
        return False

    def add(self, backpackitem):
        self.itemname, self.itemsize = backpackitem.return_name_size()
        if self.check_capacity() == False:
            self.list.append(backpackitem)
            self.current_cap += self.itemsize

    def __str__(self):
        return f"Backpack({self.current_cap}/{self.max_cap}): {self.list}"

bp = Backpack(10)
print(bp)
bp.add(BackpackItem("Book", 7))
print(bp)
bp.add(BackpackItem("Laptop", 3))
print(bp)
bp.add(BackpackItem("Headphones", 2))
print(bp)