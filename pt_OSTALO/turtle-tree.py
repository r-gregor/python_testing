from turtle import *

# from: #TechWithTim #FractalArt
# Make Fractal Art With Python!
# https://www.youtube.com/watch?v=_ABdBoW4DV8

shape("turtle")
speed(0)

def tree(size, levels, angle):
	if levels == 0:
		color("green")
		dot(size)
		color("black")
		return
	
	forward(size)
	right(angle)

	tree(size * 0.8, levels - 1, angle)
	
	left(angle * 2)
	tree(size * 0.8, levels - 1, angle)

	right(angle)
	backward(size)

def snowflake_side(length, levels):
	if levels == 0:
		forward(length) # different tha in the tree!!
		return
	
	length /= 3.0
	snowflake_side(length, levels -1)
	left(60)
	snowflake_side(length, levels -1)
	right(120)
	snowflake_side(length, levels -1)
	left(60)
	snowflake_side(length, levels -1)


def create_snowflake(sides, length):
	colors=["black", "green", "orange"]
	for i in range(sides):
		if i > len(colors) - 1:
			i = 0
		color(colors[i])
		snowflake_side(length, sides)
		right(360 / sides)
	color("black")


# main commands
# left(90)
# tree(70, 5, 60)
# tree(100, 7, 20)
# tree(70, 5, 30)

# snowflake_side(200 ,2)
create_snowflake(3, 200)
left(90)
tree(70, 5, 30)


mainloop()
