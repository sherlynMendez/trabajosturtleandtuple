import turtle 
#trabajo 60
for i in  range (o,4):
turtle.forward(100)
turtle.right(90)

turtle.exitonclick()


#trabajo 61
import turtlefor i in range (0,3):
   turtle.forward(100)
   turtle.left(120)
   
   turtle.exitonclick()

   
   #trabajo 62
   import turtle 
   for i in range (0,360):
    turtle.forward(1)
    turtle.right (1)

turtle.exitonclick()

#trabajo 63
import turtle

turtle.colo("black","blue")
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black","purple")
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black","green")
turtle.begin_fill()
for i in range (0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()

#trabajo 64
import turtle 

for i in range (0,5):
    turtle.forward(100)
    turtle.right(144)

turtle.exitonclick()

#trabajo 65
import turtle

turtle.left (90)
turtle.forward (100)
turtle.right (90)
turtle.penup ()
turtle.forward (50)
turtle.pendown ( )
turtle.forward (75)
turtle.right (90)
turtle.forward (50)
turtle.right (90)
turtle.forward (75)
turtle.left (90)
turtle.forward (50)*
turtle.left (90)
turtle.forward (75)
turtle.penup ()
turtle.forward (50)
turtle.pendown ()
turtle.forward (75)
turtle.left (90)
turtle.forward (50)
turtle.left (90)
turtle.forward (45)
turtle.left (180)
turtle.forward (45)
turtle.left (90)
turtle. forward (50)
turtle.left (90)
turtle.forward (75)

turtle.hideturtle ()

turtle.exitonclick()

#trabajo 66
import turtle
import random 

turtle.pensize(3)

for i in range  (0,8) :
    turtle.color(random.choice(["purple","orange","green","pink","blue","red"]))
    turtle.forward(50)
    turtle.right(45)

    turtle.exitonclick()

    #trabajo 67
import turtle
 import random

for in range (0, 10) :
  for i in range (0,8):
   turtle. forward (50)
    turtle.right (45)
  turtle.right (36)

turtle.hideturtle ()

turtle.exitonclick (
    
#trabajo 68
 import turtle
import random
lines = random.randint (5, 20)

for x in range (0,lines):
   length = random. randint (25, 100)
    rotate= random. randint (1, 365)
    turtle. forward (length)
    turtle.right (rotate)
    
turtle.exitonclick ()     