


import turtle, math, random

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
win.listen()

t = turtle.Turtle()
t.up()
t.hideturtle()
t.color('blue')
     
# points(-1,1) (1,1) (1,-1) and (-1,-1) in z = 1 and again all 4 at z = -1
verts = (-1,1,1), (1,1,1),(1,-1,1),(-1,-1,1),(-1,1,-1), (1,1,-1),(1,-1,-1),(-1,-1,-1)


while True:
    
    for x,y,z in verts:
        # Go to each point at the x,y,z and draw a circle
        
        z += 5
        f = 400/z   # Used for scalling - larger number, larger object
        x,y = x*f, y*f

        t.up()
        t.goto(int(x),int(y))
        t.down()
        t.circle(3)
        t.up()
    

    win.update()
    t.clear()
    
