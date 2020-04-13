


import turtle, math, random

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
win.listen()

t = turtle.Turtle()
t.up()
t.hideturtle()
t.color('blue')

dt = 0.3

class Cam:
    def __init__(self, pos=(0,0,0), rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.s = dt*10
        

    def update1(self):
        self.pos[1] += self.s
        
    def update2(self):
        self.pos[1] -= self.s
        
    def update3(self):
        self.pos[2] += self.s
        
    def update4(self):
        self.pos[2] -= self.s
        
    def update5(self):
        self.pos[0] += self.s
        
    def update6(self):
        self.pos[0] -= self.s
 

verts = (0,6,0),(-2,0,2),(2,0,2),(2,-2,-2),(-2,-2,-2)
edges = (0,1),(0,2),(0,3),(0,4),(1,2),(2,3),(3,4),(4,1)

cam = Cam((0,0,-10))

win.onkey(cam.update1, 's')
win.onkey(cam.update2, 'w')
win.onkey(cam.update3, 'a')
win.onkey(cam.update4, 'd')
win.onkey(cam.update5, 'q')
win.onkey(cam.update6, 'e')


while True:
    
    for edge in edges:
        points = []
        for x,y,z in (verts[edge[0]], verts[edge[1]]):

            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]

            if z != 0:
                f = 200/z
            else:
                f = 200
            x,y = x*f,y*f
            points += [(int(x), int(y))]

        t.up()
        t.goto(points[0])
        t.down()
        t.goto(points[1])
        t.up()
            
    

    win.update()
    t.clear()
    
