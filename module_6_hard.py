# Дополнительное практическое задание по модулю: "Наследование классов.
import math


class Figure:
    COLORS = {
        (0, 0, 0): 'black',
        (255, 255, 255): 'white',
        (255, 0, 0): 'red',
        (0, 255, 0): 'lime',
        (0, 0, 255): 'blue',
        (255, 255, 0): 'yellow',
        (0, 255, 255): 'aqua',
        (255, 0, 255): 'magenta',
        (192, 192, 192): 'silver',
        (128, 128, 128): 'gray',
        (128, 0, 0): 'burgundy',
        (128, 128, 0): 'olive',
        (0, 128, 0): 'green',
        (128, 0, 128): 'purple',
        (0, 128, 128): 'turquoise',
        (0, 0, 128): 'navy',
        (255, 128, 0): 'orange',
        (128, 64, 0): 'burnt orange',
        (0, 64, 0): 'forest green',
        (64, 64, 0): 'brown',
        (64, 0, 0): 'maroon',
        (0, 0, 64): 'dark blue',
        (0, 192, 0): 'light green',
        (128, 255, 128): 'pale green',
        (128, 128, 255): 'slate blue',
        (0, 128, 255): 'sky blue',
        (255, 128, 128): 'rose',
        (64, 64, 64): 'dark gray',
        (0, 255, 255, 255): 'rainbow'
    }
    side_count = 0

    def __init__(self, color, *sides):
        self.__sides = [*sides]
        self.__color = list(color)
        self.filled = False

    def get_color(self):  # check
        return self.__color

    def __is_valid_color(self, r, g, b):  # checkpop в питоне
        new_color = [r, g, b]
        if all(isinstance(color, int) and 0 <= color <= 255 for color in new_color):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            if (r, g, b) in self.COLORS:
                print(f'your color is: {self.COLORS.get((r, g, b))}')

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def check_for_triangle(self, *new_sides):
        if self.__is_valid_color(*new_sides):
            return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    @property
    def radius(self):
        return self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def __is_real(self, *news_sides):
        a, b, c = news_sides
        if (a < b + c) and (b < c + a) and (c < b + a):
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if self.check_for_triangle(*new_sides) and self.__is_real(*new_sides):
            self.__sides = list(new_sides)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides * self.sides_count)
        if len(sides) == 1:
            self.__sides = [sides[0]] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((128, 128, 128), 3, 4, 5)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
triangle1.set_color(128, 128, 128)
print(triangle1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
triangle1.set_sides(4, 6, 7)
print(triangle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка объёма (куба):
print(triangle1.get_square())