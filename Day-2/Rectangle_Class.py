class Rectangle():
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

rect = Rectangle(5 , 5)
print("Area is : ", rect.area())
print("Perimeter is : " , rect.perimeter())
