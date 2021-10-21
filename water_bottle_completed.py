"""Write a class `WaterBottle` which has max capacity (parameter should be called max_capacity, with default 2L) and volume (member variable should be called volume, and initializes as 0L).
It has 3 methods (excluding __init__)
1. __str__() : returns a string representing how many liters are in the bottle (print to 1 decimal places, e.g. "2.3L").
2. fill() : Fills the bottle to max capacity
3. drink(amount) : drinks a certain amount from the bottle
* if the amount is less than 0, nothing changes
* if the amount is more than the current volume, volume becomes 0
* else the amount is subtracted from the volume"""


class WaterBottle:
    def __init__(self, max_capacity=2, volume=0):
        self.max_capacity = max_capacity
        self.volume = volume

    def __str__(self):
        return f"{self.volume:.1f}L"
    
    def fill(self):
        self.volume = self.max_capacity
    
    def drink(self,amount):
        if amount > 0:
            self.volume -= amount
            if self.volume < 0:
                self.volume = 0