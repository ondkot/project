from turtle import *
import random
barvy = ["#F00", "green", "blue", "cyan", "magenta","red","orange"]
shape("turtle")
pencolor(random.choice(barvy))
color(random.choice(barvy))
for i in range(0, 361):
	forward(1)
	left(1)
done()

