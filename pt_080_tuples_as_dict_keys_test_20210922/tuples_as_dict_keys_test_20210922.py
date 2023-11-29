from typing import Tuple

testd = {}

testd[(0,0)] = "Top left"
testd[(0,100)] = "Top right"
testd[(100,0)] = "Bottom left"
testd[(100,100)] = "Bottom right"
testd[(50,50)] = "Middle center"

def arrange_coodinate(num: int) -> int:
	'''gravitate point to square corner point or the middle one'''
	if num < 50:
		return 0
	elif num > 50:
		return 100
	else:
		return 50

# python 3.9 on (and no 'import typing' nedded):
# def get_point_location(x: int, y: int) -> tuple[int, int]:
# but to stay on the safe side ...
def get_point_location(x: int, y: int) -> Tuple[int, int]:

	'''return the gravitated point'''
	x = arrange_coodinate(x)
	y = arrange_coodinate(y)
	return testd[(x,y)]

def get_corner(a: int, b:int) -> None:
	'''
	Print description of one of four corners or the center of sqare where
	middle point is 50, 50, and all other points gravitate to corners of
	square [(0,0), (0,100), (100,0), (100,100)] '''

	note = f'The arranged location of {a}, {b} is:'
	result = f'"{get_point_location(a, b)}"'

	print(f'{note:<40}{result:>15}')


if __name__ == '__main__':
	get_corner(75, 55)
	get_corner(-100, 55)
	get_corner(50, 50)
	get_corner(2, 1555)
	get_corner(49, 13)