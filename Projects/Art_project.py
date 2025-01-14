### starts code
import turtle

#### this changes the backround color
turtle.Screen().bgcolor("black")

### this makes the turtles
t5 = turtle.Turtle()
t4 = turtle.Turtle()
t3 = turtle.Turtle()
t2 = turtle.Turtle()
t = turtle.Turtle()

t.penup
t.goto(-50, 50)
t.pendown
t2.penup
t2.goto(50,50)
t2.pendown
t3.penup
t3.goto(50,-50)
t3.pendown
t4.penup
t4.goto(-50,-50)
t4.pendown
t5.penup
t5.goto(0,0)
t5.pendown

### this code is what draws
colors = ["firebrick"] 
colors2 = ["floralwhite"]
colors3 = ["firebrick"]
colors4 = ["floralwhite"]
colors5 = ["firebrick"]
for i in range(900):
    t.color(colors[i % 1]) 
    t.forward(5 + i)
    t.left(90 + 1)
    t.speed(0)
    t2.color(colors2[i % 1]) 
    t2.forward(5 + i)
    t2.left(70 + 1)
    t2.speed(0)
    t3.color(colors3[i % 1]) 
    t3.forward(5 + i)
    t3.left(90 + 1)
    t3.speed(0)
    t4.color(colors4[i % 1]) 
    t4.forward(5 + i)
    t4.left(30 + 1)
    t4.speed(0)
    t5.color(colors5[i % 1]) 
    t5.forward(5 + i)
    t5.left(120 + 1)
    t5.speed(0)
    

### ends the code
turtle.exitonclick()