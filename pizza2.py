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