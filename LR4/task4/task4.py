import math
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Color:
    def __init__(self):
        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @color.deleter
    def color(self):
        del self._color


class Polygon(Figure):
    def __init__(self, angles_count, side_len, color, name):
        self._n = angles_count
        self._a = side_len
        self.c = Color
        self.c.color = color
        self.name = name

    def area(self):
        super().area()
        perimeter = self._n * self._a
        outer_radius = self._a/(2*math.sin(math.pi/self._n))
        inner_radius = outer_radius * math.cos(math.pi/self._n)
        return int(1/2 * perimeter * inner_radius)

    def get_info(self):
        name = self.name
        area = self.area()
        color = self.c.color
        print("Figure: {}\nColor: {}\nArea: {}".format(name, color, area))

    def plot(self):
        outer_radius = self._a / (2 * math.sin(math.pi / self._n))

        x = [outer_radius * math.cos(2 * math.pi * i / self._n) for i in range(self._n + 1)]
        y = [outer_radius * math.sin(2 * math.pi * i / self._n) for i in range(self._n + 1)]

        fig, ax = plt.subplots()

        ax.plot(x, y)
        ax.fill(x, y, color=self.c.color, alpha=0.5)
        ax.set_aspect('equal')
        ax.set_title(self.name)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.savefig('task4/polygon.png')

        plt.show()


def run_task():
    angles = int(input('Enter angles count: '))
    side_len = int(input('Enter side length: '))
    color = input()
    name = input()
    polygon = Polygon(angles, side_len, color, name)
    polygon.plot()

