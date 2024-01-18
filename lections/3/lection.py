import math

print(type(type(1)))


# print(dir(range))
# dir выводит все объекты, содержащиеся в  текущем объекте


class Rectangle:
    def __init__(self, height, length):
        self.height = height
        self.length = length
        self.diag = None
        self.area = None

    def calculate_area(self):
        self.area = self.height * self.length
        return self.area

    def __eq__(self, other):
        return self.area == other.area

    def __add__(self, other):
        return self.area + other.area

    def __lt__(self, other):
        return self.area < other.area

    def perimetr(self):
        return (self.length + self.height) * 2

    def diag_len(self):
        self.diag = (self.length ** 2 + self.height ** 2) ** 0.5
        return self.diag

    def triangle_angles(self):
        cos_diag_length = self.length / self.diag
        angle_diag_length = math.acos(cos_diag_length)
        first_angle = math.degrees(angle_diag_length)
        second_angle = 180 - first_angle - 90
        assert first_angle + second_angle == 90
        return f'Если провести диагональ, то углы прямоугольного ' \
               f'треугольника будут равны: {round(first_angle, 3), round(second_angle, 3), 90}'


rectangle1 = Rectangle(10, 30)
print(rectangle1.calculate_area())
print(rectangle1.diag_len())
print(rectangle1.triangle_angles())

rectangle2 = Rectangle(10, 40)
print(rectangle2.calculate_area())
print(rectangle2.diag_len())
print(rectangle2.triangle_angles())
print(rectangle2 + rectangle1)
print(rectangle2 > rectangle1)
rectangle3 = Rectangle(10, 40)
rectangle3.calculate_area()
print(rectangle2 == rectangle3)
