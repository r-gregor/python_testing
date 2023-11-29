#! /usr/bin/env python3
# -*- coding: utf-8 -*-
print("First Fibbonacci exxpression:")
FB = [1, 1]
i = 2
print(FB[i-2])

while FB[-1] < 300:
	FB.append(FB[i-2] + FB[i-1])
	print(FB[i-1])
	i += 1

print("-------------------------------------")
print("Second Fibbonacci exxpression:")

FB2, FB1 = 1, 1
FB = 0
while FB < 300:
	while FB < 2:
		print(1)
		FB += 1
	print(FB)
	FB2 = FB1
	FB1 = FB
	FB = FB2 + FB1
	

print("-------------------------------------")
print("Third Fibbonacci exxpression:")

def fib():
	a, b = 0, 1
	while True:			# First iteration:
		yield a			# yield 0 to start with and then
		a, b = b, a + b	# a will now be 1, and b will also be 1, (0 + 1)

for index, fibonacci_number in enumerate(fib()):
	 print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
	 if index == 10:
		 break

