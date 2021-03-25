from turtle import *
shape("turtle")
penup()
left(270)
forward(100)
left(90)
pendown()
for j in range(1,5):
	for i in range(1,11):
		forward(i * j)
		penup()
		forward(41 - i * j)
		pendown()
	left(90)
done()