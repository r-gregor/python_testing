from abc import ABC, abstractmethod
import math

class Calculations(ABC):
	@abstractmethod
	def calculate_area(self):
		""" Calculation of area of 2D shape (circle or square) """
	
	def print_out(self):
		""" Prints out the area statemenet """


class Circle(Calculations):
	def __init__(self, radius: int):
		self.radius = radius

	def calculate_area(self):
		return math.pi * self.radius * self.radius
	
	def print_out(self):
		print(f'The area of circle with radius of {self.radius} mm is: {self.calculate_area():.2f} mm2')

class Square(Calculations):
	def __init__(self, side: int):
		self.side = side

	def calculate_area(self):
		return self.side * self.side

	def print_out(self):
		print(f'The area of square with side of {self.side} mm is: {self.calculate_area():.2f} mm2')

class Rectangle(Calculations):
	def __init__(self, side_a: int, side_b: int):
		self.a = side_a
		self.b = side_b

	def calculate_area(self):
		return self.a * self.b

	def print_out(self):
		print(f'The area of rectangle with sides of a = {self.a} mm and b = {self.b} mm is: {self.calculate_area():.2f} mm2')


def main():
	side_or_radius = 20

	c1 = Circle(side_or_radius)
	c1.print_out()

	c2 = Circle(100)
	c2.print_out()

	sq1 = Square(side_or_radius)
	sq1.print_out()

	rct1 = Rectangle(4, 5)
	rct1.print_out()

if __name__ == "__main__":
	main()
