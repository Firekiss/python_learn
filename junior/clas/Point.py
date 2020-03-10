
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def string(self):
        print({'X': self.x, 'Y': self.y})


class Circle(Point):
    def __init__(self, x, y, radius):
        super(Circle, self).__init__(x, y)
        self.radius = radius

    def string(self):
        print('该图形初始化点为: {}; {}'.format({'X': self.x, 'Y': self.y}, {'半径为': self.radius}))


class Size():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def string(self):
        print({'Width': self.width, 'Height': self.height})


class Rectangle(Point, Size):
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)

    def string(self):
        print('该图形初始化点为：{}; 长宽分别为：{}'.format({'X': self.x, 'Y': self.y}, {'Width': self.width, 'Height': self.height}))
    


c = Circle(5, 5, 8)
c.string()

r1 = Rectangle(15, 15, 15, 15)
r1.string()

r2 = Rectangle(40, 30, 11, 14)
r2.string()
    