#!/usr/bin/env python3


class Shape:
    def __init__(self, name) -> None:
        self.name = name

    # def __str__(self) -> str:
    #     return f"{self.name}"


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    # def __str__(self):
    #     return f"{self.name} with length={self.length} and width={self.width}"


class Square(Rectangle):
    def __init__(self, name, length):
        super().__init__(name, length, length)

    # def __str__(self):
    #     return f"{self.name} with length={self.length}"


class ColoredObject:
    def __init__(self, color) -> None:
        self.color = color

    # def __str__(self) -> str:
    #     return f"{self.color}"


class ColoredSquare(Square, ColoredObject):
    def __init__(self, name, color, length):
        Square.__init__(self, name, length)
        ColoredObject.__init__(self, color)

    # def __str__(self):
    #     color = f"{ColoredObject.__str__(self)}"
    #     desc = f"{Square.__str__(self)}"
    #     return f"{color} {desc}"


# square = Square("Square", 5)
colored_square = ColoredSquare("Colored Square", "blue", 6)

# print(square)
print(colored_square)
