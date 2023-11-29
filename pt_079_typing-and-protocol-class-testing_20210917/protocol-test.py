from typing import Protocol
'''
from: ptn_building-implicit-interfaces-with-protocol-classes_20210917.txt
'''


class Flyer(Protocol):
	def fly(self) -> None:
		"""A Flyer can fly"""
		pass


class FlyingHero:
	"""This hero can fly, which is BEAST."""
	def fly(self):
		# Do some flying...
		pass

class RunningHero:
	"""This hero can run. Better than nothing!"""
	def run(self):
		# Run for your life!
		pass

class Board:
	"""An imaginary game board that doesn't do anything."""
	def make_fly(self, obj: Flyer) -> None:   # <- Here's the magic
		"""Make an object fly."""
		return obj.fly()


def main() -> None:
	board = Board()
	board.make_fly(FlyingHero())
	board.make_fly(RunningHero())  # <- Fails mypy type-checking!


if __name__ == '__main__':
	main()