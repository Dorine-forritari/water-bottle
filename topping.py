class Topping():
    def __init__(self, name, price) -> None:
        self.__name = name
        self.__price = price

    def __str__(self) -> str:
        return self.__name

    def get_price(self):
        return self.__price