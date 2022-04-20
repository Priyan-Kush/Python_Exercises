class Rectangle:
    def __init__(self, *args):
        if len(args) == 0:
            self.length = 0
            self.breadth = 0
        elif len(args) == 1:
            self.length = self.breadth = args[0]
        else:
            self.length = args[0]
            self.breadth = args[1]
    def area(self):
        return self.length * self.breadth

rect1 = Rectangle(10,3)
rect2 = Rectangle(10,20)
rect3 = Rectangle(30)
print(rect1.area())
print(rect2.area())
print(rect3.area())