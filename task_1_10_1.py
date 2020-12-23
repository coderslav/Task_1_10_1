class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_str_rectangle(self):
        return f"Rectangle ({self.x}, {self.y}, {self.width}, {self.height})"


rectangle = Rectangle(5, 10, 50, 100)
print(rectangle.get_str_rectangle())
