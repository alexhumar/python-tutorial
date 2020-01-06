# We use classes to declare new types
# We should name classes with Pascal naming convention (class name should start with capital letter)
# For variables and functions we use lowercase letters and we separate multiple words using an underscore


class Point:
    # Constructor. Here, we are defining and initializing the class members
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, x_dist: int, y_dist: int):
        self.x += x_dist
        self.y += y_dist

    def draw(self):
        print(f"({self.x}, {self.y})")


point1 = Point(10, 20)
point1.draw()
# Attributes can be added dynamically
point1.an_attribute = 30
print(point1.an_attribute)
point1.move(1, 1)
point1.draw()
