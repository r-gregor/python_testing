import Stack
s = Stack.Stack()

print("The initial size is:", s.size())
s.push("Gregor")
s.push("Redelonghi")
s.push("Valvasorjeva ulica 5")
s.push("1000, Ljubljana")
s.push("gredelonghi@gmail.com")

print("The size after filling is:", s.size())

for el in range(s.size()):
	print("\nThe stack:")
	s.print()
	print()
	
	print("The top element, and next to remove is:",s.peek())
	print("Removing the top element:", end=" ")
	print(s.pop() + " ... ")
	print("After the removing of last element the size is:", s.size())
	
print("END!. The size is:", s.size())



