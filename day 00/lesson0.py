from turtle import*

print("tazo terterashvili")
speed(10)
#paint house

width(3)
color("lime")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square 

#drawing a door

width(2)
forward(70)
left(90)
color("gray")
begin_fill()
forward(60)
right(90)
forward(36)
right(90)
forward(60)
end_fill()
#end of door

penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(206)
end_fill()
#end of roof

#start 
penup()
goto(200,200)
pendown()

color("lime")

left(31)

forward(40)

begin_fill()
color("blue")

right(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

#end of part

penup()
goto(200,200)
pendown()

# start 

color("lime")

right(179)
forward(200)
left(90)

forward(40)
left(90)

color("blue")
begin_fill()

forward(60)

right(93)
forward(60)

right(90)
forward(60)
right(90)
forward(60)

end_fill()

exitonclick()