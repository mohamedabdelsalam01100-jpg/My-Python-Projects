from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @width.setter
    def width(self,new_width):
        if new_width >= 0 :
            self.__width = new_width
    @height.setter
    def height(self,new_height):
        if new_height >= 0 :
            self.__height = new_height
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * pow(self.radius,2)
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,new_radius):
        if new_radius >= 0 :
            self.__radius = new_radius
shapes = [Rectangle(10, 5),
          Circle(7)
          ]
for shape in shapes:
    print(shape.area())

        