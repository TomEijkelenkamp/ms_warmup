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
        self.last_point = self.points[-1]

    def generate(self):
        animation = FuncAnimation(self.fig, self.animate, interval=200, frames=self.iterations)
        plt.show()

    def random_point(self):
        return self.points[np.random.randint(0, 3)]

    def new_point(self):
        random_point = self.random_point()
        return random_point + self.last_point

    def animate(self, i):
        new_point = self.new_point()
        self.last_point = new_point
        self.ax.scatter(new_point.x, new_point.y, c='blue')

if __name__ == '__main__':
    sierpinski = Sierpinski(10000)
    sierpinski.generate()







