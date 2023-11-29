#! /usr/bin/env python3

class MyClass:
	def __init__(self, height = None, weigth = None):
		self.height = height
		self.weigth = weigth
		
	def setWeight(self, new_weight):
		self.weigth = new_weight
	
	def setHeight(self, new_height):
		self.height = new_height
		
	
	def Info(self):
		print("This is an Object instantiated from class MyClass.")
		
		if self.height and self.weigth is not None:
			print("Height an Weigth are: {}/{}.".format(self.height, self.weigth))

def main():

	obj1 = MyClass()
	obj1.Info()

	obj2 = MyClass(1.8, 90)
	obj2.Info()

	obj3 = MyClass()
	obj3.setWeight(105)
	obj3.setHeight(1.72)
	obj3.Info()

	print("Name of a class of object obj3: {}".format(obj3.__class__.__name__))
	
if __name__ == "__main__":
	main()
