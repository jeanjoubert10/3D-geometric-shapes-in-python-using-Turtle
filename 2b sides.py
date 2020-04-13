


import turtle, math, random

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
win.listen()

t = turtle.Turtle()
t.up()
t.hideturtle()
t.color('black','blue')
     

verts = (-1,1,1), (1,1,1),(1,-1,1),(-1,-1,1),(-1,1,-1), (1,1,-1),(1,-1,-1),(-1,-1,-1)
side_list = [(0,1,2,3), (0,1,5,4), (1,5,6,2), (2,3,7,6), (0,4,7,3)] # Leave (4,5,6,7) for now

color_list = ['red', 'cyan', 'blue', 'yellow', 'orange', 'lightblue', 'pink', 'green']

while True:
    color_number = 0
    
    for x,y,z in verts:
        z += 5
        f = 200/z
        x,y = x*f, y*f


    for side in side_list:
        
        points = []
        
        for x,y,z in (verts[side[0]], verts[side[1]], verts[side[2]], verts[side[3]], verts[side[0]]):
            z+= 5
            f = 200/z
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
    
    
