from cmath import sqrt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from random import randint



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
        self.points = [Point(0.0, 0.0), Point(1.0, 0.0), Point(0.5, sqrt(3)/2), Point(0.6,0.2)]
        self.fig, self.ax = plt.subplots()
        self.last_point = self.points[-1]

    def generate(self):
        for i in range(3):
            self.ax.scatter(self.points[i].x, self.points[i].y, )
        animation = FuncAnimation(self.fig, self.animate, interval = 100, frames=self.iterations, repeat=True)
        plt.show()
   
        
    def animate(self, i):
        self.last_point =  (self.points[randint(0, 2)] + self.last_point)
        plt.plot(self.last_point.x, self.last_point.y, linestyle='',  marker='o')
        plt.draw()
              
if __name__ == '__main__':
    sierpinski = Sierpinski(1000)
    sierpinski.generate()
    
    






