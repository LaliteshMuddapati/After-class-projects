class quadrilateral:
    def __init__ (self, length, height):
        self.length=length
        self.height=height

    def print_area(self):
        print("The area of the quadrilateral is: ", self.length*self.height)


class triangle:
    def __init__(self, length, height):
        self.length=length
        self.height=height

    def print_area(self):
        print("The area of the triangle is: ",0.5*self.length*self.height)


rectangle=quadrilateral(15,2)
tri=triangle(12,4)

for shape in (rectangle, tri):
    shape.print_area()