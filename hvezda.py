from turtle import  *
import random
barvy = ["#F00", "green", "blue", "cyan", "magenta"]
pencolor(random.choice(barvy))
color(random.choice(barvy))
shape("turtle")
delka = 100
left(45)

for i in range(0, 12):
	forward(delka)
	left(120)
	forward(delka)
	left(270)
done()
