from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length=1) -> None:
        super().__init__(side_length, side_length)
