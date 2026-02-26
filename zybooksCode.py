
# "New" means new compared to previous level
class Shape:
    default_color = "red"
    # New: Change from background_color
    count = 0

    def __init__(self):
        Shape.count += 1
        self.number = self.count
        self.color = self.default_color

    def print_description(self):
        print(f"{self.number} of {self.count} - {self.color}")

shape1 = Shape()
shape2 = Shape()
shape2.color = "gold"

print(Shape.count)
shape1.print_description()
shape2.print_description()