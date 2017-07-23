from turtle import *

def move():
	for i in range(200):
		right(1)
		forward(1)

color('red')
begin_fill()
hideturtle()
left(140)
forward(111.65)
move()
left(120)
move()
forward(111.65)
end_fill()
done()