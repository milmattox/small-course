import turtle
import random
ned = turtle.Turtle()
ned.speed(90)
ned.pensize(2)
def rect(length,width,acolor):
  ned.color('black')
  ned.fillcolor(acolor)
  ned.begin_fill()
  for i in range(2):
    ned.forward(length)
    ned.right(90)
    ned.forward(width)
    ned.right(90)
  ned.end_fill()
def move(x,y,turn):
  ned.penup()
  ned.setpos(x,y)
  ned.pendown()
  ned.left(turn)
mycolors=['red','blue','green','yellow','orange','purple']
turn = 0
x = -200
y = 200
for i in range(45):
  x = x + 5
  y = y - 5
  acolor = random.choice(mycolors)
  turn = turn + 1
  move(x,y,turn)
  rect(40,20,acolor)