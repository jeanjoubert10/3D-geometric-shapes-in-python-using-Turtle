


import turtle, math, random

win = turtle.Screen()
win.setup(1000,1000)
win.tracer(0)
win.listen()

t = turtle.Turtle()
t.up()
t.hideturtle()
t.color('blue')
     

verts = (-1,1,1), (1,1,1),(1,-1,1),(-1,-1,1),(-1,1,-1), (1,1,-1),(1,-1,-1),(-1,-1,-1)

# Each represents a line between all of the points
# points in verts are clockwise at z+1 from -1,1 and again at z-1
edges = (0,1), (1,2), (2,3), (3,0),(4,5), (5,6), (6,7), (7,4),(0,4), (1,5), (2,6), (3,7)

while True:
    
    for x,y,z in verts:
        # Draw circles at the points
        z += 5
        f = 200/z
        x,y = x*f, y*f

        t.up()
        t.goto(int(x),int(y))
        t.down()
        t.circle(3)
        t.up()

    for edge in edges:
        points = []
        for x,y,z in (verts[edge[0]], verts[edge[1]]):
            # print(verts[edge[0]]) will give coords of first point of the line(eg (-1,1,1)
            
            z+= 5
            f = 200/z
            x,y = x*f,y*f
            points += [(int(x), int(y))]

        t.up()
        t.goto(points[0])
        t.down()
        t.goto(points[1]) # draw line from point 1 to 2 for each of the sides
        t.up()
            
    

    win.update()
    t.clear()
    
