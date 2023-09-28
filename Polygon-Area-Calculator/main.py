from shape_calculator import Rectangle

# Create an instance of a Rectangle
rect = Rectangle(10, 5)

# Call methods and display results
print("Area of rectangle:", rect.get_area())
rect.set_height(3)
print("Perimeter of the rectangle:", rect.get_perimeter())
print(rect)
print(rect.get_picture())

from shape_calculator import Square

# Create an instancce of a Square
sq = Square(9)

# Call methods and display results
print("Area of the square:", sq.get_area())
sq.set_side(4)
print("Diagonal of the square:", sq.get_diagonal())
print("Representation of the square:", sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))