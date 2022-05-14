import tkinter
import turtle
import time as tm
import random as rd
from tqdm import tqdm
while True:
    mode = input("mode instant/anim ")
    if mode == "instant" or mode == "anim":
        break
    else:
        print("input exception")
while True:
    diver = input("divergence ")
    try:
        int(diver)
    except ValueError:
        print("must be number")
        continue
    else:
        diver = int(diver)
        break
while True:
    ampl = input("amplitude ")
    try:
        int(ampl)
    except ValueError:
        print("must be number")
        continue
    else:
        if int(ampl) < 101:
            ampl = int(ampl)
            break
        else:
            print("must be smaller than 100")
            continue
while True:
    ite = input("iterations ")
    try:
        int(ite)
    except ValueError:
        print("must be number")
        continue
    else:
        if int(ite) < 100001:
            ite = int(ite)
            break
        else:
            print("must be smaller than 100000")
            continue
turtle.setup(700, 750, 10, 10)
t = turtle.Pen()
u = turtle.Pen()
v = turtle.Pen()
w = turtle.Pen()
x = turtle.Pen()
turtle.tracer(0, 0)
t.hideturtle()
u.hideturtle()
v.hideturtle()
w.hideturtle()
x.hideturtle()
w.speed("fastest")
x.speed("fastest")
t.goto(0, 0)
u.penup()
u.goto(-285, -320)
u.pendown()
v.penup()
v.goto(-285, -305)
v.pendown()
w.up()
w.goto(-290, 290)
w.down()
for g in range(4):
    w.forward(580)
    w.right(90)
x.up()
x.goto(290,-290)
x.down()
x.right(90)
x.forward(32)
x.right(90)
x.forward(580)
x.right(90)
x.forward(32)
turtle.update()
c = 0
if mode == "anim":
    for i in tqdm(range(ite)):
        u.clear()
        v.clear()
        u.write("count %s / %s" %(i + 1, ite))
        v.write("corrections %s" %(c))
        if int(t.xcor()) > 280 or int(t.xcor()) < -280 or int(t.ycor()) > 280 or int(t.ycor()) < -280:
            turtle.tracer(0, 0)
            t.up()
            t.goto(rd.randint(-250, 250), rd.randint(-250, 250))
            t.down()
            t.forward(rd.randint(-ampl, ampl))
            t.left(rd.randint(-diver, diver))
            c = c + 1
            tm.sleep(0.01)
            turtle.update()
        else:
            turtle.tracer(0, 0)
            t.forward(rd.randint(-ampl, ampl))
            t.left(rd.randint(-diver, diver))
            tm.sleep(0.01)
            turtle.update()
elif mode == "instant":
    turtle.tracer(0, 0)
    for i in tqdm(range(ite)):
        if int(t.xcor()) > 280 or int(t.xcor()) < -280 or int(t.ycor()) > 280 or int(t.ycor()) < -280:
            t.up()
            t.goto(rd.randint(-250, 250), rd.randint(-250, 250))
            t.down()
            t.forward(rd.randint(-ampl, ampl))
            t.left(rd.randint(-diver, diver))
            c = c + 1
        else:
            t.forward(rd.randint(-ampl, ampl))
            t.left(rd.randint(-diver, diver))
    u.write("count %s / %s" %(i + 1, ite))
    v.write("corrections %s" %(c))
    turtle.update()
while True:
    save = input("save in desktop y/n ")
    if save == "y":
        while True:
            gui = input("show gui y/n ")
            if gui == "y":
                turtle.getscreen()
                turtle.getcanvas().postscript(file="drawing.eps")
                print("file saved")
                print("end of process")
                break
            elif gui == "n":
                u.clear()
                v.clear()
                x.clear()
                turtle.getscreen()
                turtle.getcanvas().postscript(file="drawing.eps")
                print("file saved")
                print("end of process")
                break
            else:
                print("input exception")
        break
    elif save == "n":
        print("end of process")
        break
    else:
        print("input exception")
input("exit with enter")
turtle.bye()
quit()

