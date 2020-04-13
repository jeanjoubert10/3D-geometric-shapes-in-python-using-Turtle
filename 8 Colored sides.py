


import turtle, math, random

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
win.listen()


dt = 0
radian = 0

def rotate2d(pos,rad):
    x,y=pos
    s,c = math.sin(rad),math.cos(rad)
    return x*c-y*s, y*c+x*s

class Cam:
    def __init__(self, pos=(0,0,0), rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
         

    def updateE(self):# In
        s=dt*5
        
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[0] -= x
        self.pos[2] -= y
        for i in cube_list:
            i.t.clear()
            i.draw()
        
    def updateQ(self): # Out
        s=dt*10
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[0] += x
        self.pos[2] += y
        for i in cube_list:
            i.t.clear()
            i.draw()
        
    def updateD(self): # Right
        s=dt*5
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[0] -=y
        self.pos[2]+=x
        for i in cube_list:
            i.t.clear()
            i.draw()
        
    def updateA(self): # Left
        s=dt*5
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[0] += y
        self.pos[2] -= x
        for i in cube_list:
            i.t.clear()
            i.draw()
        
    def updateS(self): # Down
        s=dt*5
        self.pos[1]+=s
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[1] += s
        for i in cube_list:
            i.t.clear()
            i.draw()
    def updateW(self):# Up
        s=dt*5
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[1] -= s
        for i in cube_list:
            i.t.clear()
            i.draw()
 
class Cube:
    

    def __init__(self, pos, color):
        self.pos = pos
        x,y,z = pos
        
        self.color = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(self.color)

        self.vertices = (-1,1,1), (1,1,1),(1,-1,1),(-1,-1,1),(-1,1,-1), (1,1,-1),(1,-1,-1),(-1,-1,-1)
        #self.edges = (0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)
        self.verts = [(x+X/2,y+Y/2,z+Z/2) for X,Y,Z in self.vertices]
        self.side_list = [(0,1,2,3,0), (0,1,5,4,0), (1,5,6,2,1), (2,3,7,6,2), (0,4,7,3,0), (4,5,6,7,4)] # Leave 4,5,6,7 for now
        self.color_list = ['red', 'cyan', 'blue', 'yellow', 'orange', 'lightblue', 'pink', 'green']

        
    def draw(self):
        self.color_number = 0
        
        for side in self.side_list:
            points = []
            
            for x,y,z in (self.verts[side[0]], self.verts[side[1]], self.verts[side[2]], self.verts[side[3]], \
                          self.verts[side[0]]):

                x -= cam.pos[0]
                y -= cam.pos[1]
                z -= cam.pos[2]

                x,z = rotate2d((x,z),cam.rot[1])
                y,z = rotate2d((y,z),cam.rot[0])
            

                if z != 0:
                    f = 200/(z)
                else:
                    f = 200
                x,y = x*f,y*f
                points += [(int(x), int(y))]

            
            self.t.up()
            self.t.color('black', self.color_list[self.color_number])
            self.t.goto(points[0])
            self.t.begin_fill()
            self.t.down()
            for i in range(4):
                self.t.goto(points[i])
            self.t.end_fill()
            #self.t.up()
            self.color_number += 1
        


cam = Cam((0,0,-5))

win.onkey(cam.updateS, 's')
win.onkey(cam.updateW, 'w')
win.onkey(cam.updateA, 'a')
win.onkey(cam.updateD, 'd')
win.onkey(cam.updateQ, 'q')
win.onkey(cam.updateE, 'e')


cube1 = Cube((0,0,0),'black')
cube2 = Cube((1,0,0),'black')
cube3 = Cube((2,0,0),'black')
cube4 = Cube((0,1,0),'black')
cube5 = Cube((0,2,0),'black')
cube6 = Cube((1,2,0), 'black')

cube_list = [cube1,cube2,cube3, cube4, cube5, cube6]

for i in cube_list:
    i.t.clear()
    i.draw()

    
while True:       
    dt = 0.3
    win.update()
    
    
