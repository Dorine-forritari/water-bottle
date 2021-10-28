from shape import Shape

class Rectangle(Shape):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.area = self.x * self.y
        self.perimeter = 2 * self.x + 2 * self.y

    def get_area(self):
        return self.area

    def get_perimeter(self):
        return self.perimeter