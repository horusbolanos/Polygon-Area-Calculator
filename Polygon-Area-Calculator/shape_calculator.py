class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"

from shape_calculator import Rectangle

# Crear una instancia de Rectangle
rect = Rectangle(10, 5)

# Llamar a los métodos y mostrar los resultados
print("Área del rectángulo:", rect.get_area())
rect.set_height(3)
print("Perímetro del rectángulo:", rect.get_perimeter())
print("Representación del rectángulo:")
print(rect.get_picture())
