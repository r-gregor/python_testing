#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# COMPOSITION - PART 2

class CountUp:
	def increment(self, num):
		self.counter = num + 1
		return self.counter
		
class CountDown:
	def decrement(self, num):
		self.counter = num - 1
		return self.counter

c1 = CountUp()
print(c1.increment(5))


c2 = CountDown()
print(c2.decrement(10))

		