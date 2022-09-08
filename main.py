from cmath import sqrt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __add__(self, b):
        """ Return a new point, the sum of this point and the given point """
        return Point((self.x + b.x) / 2, (self.y + b.y) / 2)


class Sierpinski:

    def __init__(self, iterations):
        self.iterations = iterations
        self.points = [Point(0.0, 0.0), Point(1.0, 0.0), Point(0.5, sqrt(3)/2)]
        self.fig, self.ax = plt.subplots()

    def generate(self):
        animation = FuncAnimation(self.fig, self.animate, interval=1)
        plt.show()

    def random_point(self):
        return self.points[np.random.randint(0, 3)]

    def new_point(self):
        random_point = self.random_point()
        last_point = self.points[-1]
        return random_point + last_point

    def animate(self, i):
        self.points.append(self.new_point)
        self.ax.scatter(self.points)


if __name__ == '__main__':
    sierpinski = Sierpinski(10000)
    sierpinski.generate()







