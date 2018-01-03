import turtle

f = turtle.Turtle()
l = turtle.Turtle()
w = turtle.Screen()
w.colormode(255)
w.bgcolor(0, 0, 0)
f.speed(0)
l.speed(0)
f.shape("square")
f.turtlesize(0.2)
r = 255
b = 0
g =0
x=255
y=255
z=255
f.begin_fill()
for i in range(2000):
        f.pencolor(r,g,b)
        f.stamp()
        l.pencolor(x,y,z)
        l.pencolor
        r = r - 5
        b = b + 5
        g = g + 5
        x=x-3
        y=y-3
        z=z-13
        f.forward(10*i)
        f.right(131)
        l.forward(10+i)
        l.left(131)
        if r <= 0:
                r = 255
        if b >= 255:
                b = 23
        if g >= 255:
                g = 0
        if x <= 0:
                x = 255
        if y <=0:
                y = 255
        if z <=0:
                z = 255
f.end_fill()


        


