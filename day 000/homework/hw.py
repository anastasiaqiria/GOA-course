from turtle import *

#we want to paint a house

#step 1 draw a square
speed(30)
width(8)
color("blue")
forward (200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("red")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)

#drawing windows

penup()
goto(30,170)
pendown()
color("purple")

forward(45)
left(90)

forward(45)
left(90)

forward(45)
left(90)

forward(45)
left(90)

penup()
goto(135,170)
pendown()

forward(45)
left(90)

forward(45)
left(90)

forward(45)
left(90)

forward(45)
left(90)


penup()
goto(200, 200)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()




exitonclick()