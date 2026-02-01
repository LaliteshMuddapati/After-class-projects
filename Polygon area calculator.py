class shape:
    def __init__(self, length, height):
        self.length = length
        self.height = height

class quad(shape):
    def __init__(self, length, height):
        
        super().__init__(length, height)
        
        self.area = self.length * self.height
        
    def print_area(self):
        print(self.area)

class triangle(shape):
    def __init__(self, length, height):
        
        shape.__init__(self, length, height)
        
        self.area = 1/2 * self.length * self.height
        
    def print_area(self):
        print(self.area)

# Sample shapes
tri = triangle(10, 4)
sqr = quad(5, 5)
rec = quad(3, 7)

tri.print_area()
sqr.print_area()
rec.print_area()