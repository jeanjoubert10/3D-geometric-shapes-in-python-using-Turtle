


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
        s=dt*10
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[0] -= x
        self.pos[2] -= y
        
    def updateQ(self): # Out
        s=dt*10
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[0] += x
        self.pos[2] += y
        
    def updateD(self): # Right
        s=dt*10
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[0] -=y
        self.pos[2]+=x
        
    def updateA(self): # Left
        s=dt*10
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[0] += y
        self.pos[2] -= x
        
    def updateS(self): # Down
        s=dt*10
        self.pos[1]+=s
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[1] += s
        
    def updateW(self):# Up
        s=dt*10
        x,y = s*math.sin(self.rot[1]), s*math.cos(self.rot[1])
        self.pos[1] -= s
 
class Cube:
    verts = (-1,1,1), (1,1,1),(1,-1,1),(-1,-1,1),(-1,1,-1), (1,1,-1),(1,-1,-1),(-1,-1,-1)
    edges = (0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)

    def __init__(self, pos, color):
        self.pos = pos
        x,y,z = pos
        self.verts = [(x,y,z) for X,Y,Z in self.verts]
        self.color = color
        self.t = turtle.Turtle()
        self.t.ht()
        self.t.color(self.color)

    def draw(self):
        
        
        for edge in edges:
            points = []
            
            for x,y,z in (verts[edge[0]], verts[edge[1]]):

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
            self.t.goto(points[0])
            self.t.down()
            self.t.goto(points[1])
        


verts = (-1,1,1), (1,1,1),(1,-1,1),(-1,-1,1),(-1,1,-1), (1,1,-1),(1,-1,-1),(-1,-1,-1)
edges = (0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)

cam = Cam((0,0,-5))

win.onkey(cam.updateS, 's')
win.onkey(cam.updateW, 'w')
win.onkey(cam.updateA, 'a')
win.onkey(cam.updateD, 'd')
win.onkey(cam.updateQ, 'q')
win.onkey(cam.updateE, 'e')


#for i in cube_list:
    #cube = Cube[cube_list[i]]

cube = Cube((0,0,0),'blue')
cube2 = Cube((1,0,0),'red')

while True:
    cube.t.clear()
    cube2.t.clear()
    cube.draw()
    cube2.draw()
    dt = 0.3
    win.update()
    
    
