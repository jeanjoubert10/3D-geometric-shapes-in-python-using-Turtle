


import turtle, math, random

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
win.listen()

t = turtle.Turtle()
t.up()
t.hideturtle()
t.color('black','blue')


dt = 0.3

class Cam:
    def __init__(self, pos=(0,0,0), rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.s = dt*10
        

    def update1(self):
        self.pos[1] += self.s
        #print('Down')
        
    def update2(self):
        self.pos[1] -= self.s
        #print('Up')
        
    def update3(self):
        self.pos[2] += self.s
        #print('Closer')
        
    def update4(self):
        self.pos[2] -= self.s
        #print('Further')
        
    def update5(self):
        self.pos[0] += self.s
        #print('Left')
        
    def update6(self):
        self.pos[0] -= self.s
        #print('Right')
        

verts = (-1,1,1), (1,1,1),(1,-1,1),(-1,-1,1),(-1,1,-1), (1,1,-1),(1,-1,-1),(-1,-1,-1)
side_list = [(0,1,2,3), (0,1,5,4), (1,5,6,2), (2,3,7,6), (0,4,7,3), (4,5,6,7)] # Leave 4,5,6,7 for now

color_list = ['red', 'cyan', 'blue', 'yellow', 'orange', 'lightblue', 'pink', 'green']


cam = Cam((0,0,-10))

win.onkey(cam.update1, 's')
win.onkey(cam.update2, 'w')
win.onkey(cam.update3, 'a')
win.onkey(cam.update4, 'd')
win.onkey(cam.update5, 'q')
win.onkey(cam.update6, 'e')

while True:
    color_number = 0

    for side in side_list:
        
        points = []
        
        for x,y,z in (verts[side[0]], verts[side[1]], verts[side[2]], verts[side[3]], verts[side[0]]):
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
        t.color('black', color_list[color_number])
        t.goto(points[0])
        t.begin_fill()
        t.down()
        for i in range(4):
            t.goto(points[i])
            
        t.end_fill()
        t.up()
        color_number += 1

            
    

    win.update()
    t.clear()
    
    
