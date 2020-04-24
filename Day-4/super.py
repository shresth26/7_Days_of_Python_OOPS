class Shape:
    sname = "Shape"

    def getName(self):
        return self.sname

class Xshape(Shape):
    def __init__(self, name):
        self.xsname = name

    def getName(self):
        return (super().getName() + ", " + self.xsname)

circle = Xshape("Circle")
print(circle.getName())
