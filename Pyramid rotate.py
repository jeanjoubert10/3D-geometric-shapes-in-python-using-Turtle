
# Jean Joubert 14 April 2020
# Simple rotation of 3d pyramid

import turtle
from math import sin,cos
import random

win = turtle.Screen()
win.setup(600,600)
win.tracer(0)
counter = 0

def rotate(x,y,r):
    s,c = sin(r), cos(r)
    return x*c-y*s, x*s+y*c

 
class Cube:
    VERTEXES = (0,3,0),(-1,0,1),(1,0,1),(1,-1,-1),(-1,-1,-1)
    EDGES = (0,1),(0,2),(0,3),(0,4),(1,2),(2,3),(3,4),(4,1)

    def __init__(self, pos, counter):
        self.pos = pos
        x,y,z = pos
        self.counter = counter
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color('black')


    def draw(self):

        for edge in self.EDGES:
            points = []
            
            for vertex in edge:
                x,y,z = self.VERTEXES[vertex]

                x,z = rotate(x,z,self.counter)
                y,z = rotate(y,z,self.counter)
                x,y = rotate(x,y,self.counter)
                
            
                z += 5
                if z != 0:
                    f = 400/(z)
               
                sx, sy = x*f,y*f
                points.append((sx,sy))

            self.t.up()
            self.t.goto(points[0][0], points[0][1])
            self.t.down()
            self.t.goto(points[1][0], points[1][1])
            self.t.goto(points[0][0], points[0][1])
            self.t.up()


cube = Cube((0,0,0),counter)

while True:
    cube.t.clear()
    cube.draw()

    
    win.update()
    cube.counter += 0.005
    
    
