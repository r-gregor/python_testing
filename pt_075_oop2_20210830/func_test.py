class Users:
	"""Users class - contains Users usersDb (dict)"""
	def __init__(self):
		self.usersDb = {}
		count = 1
		names = ["Gregor", "Tadeja", "Zala", "Mark", "Špela", "Sisi"]
		for el in names:
			self.usersDb[count] = el
			count += 1

		self.usersDb[16] = "PopoKatePetl"

	def display_users_data(self):
		"""Display al members of usersDb (dict)"""
		data = self.usersDb
		for k in data.keys():
			print(f"{k}: {data.get(k)}")
	
	def get_users_data(self):
		"""Return the usersDb (dict)"""
		return self.usersDb

class DisplayUserData:
	"""Display data from another object"""
	def __init__(self, obj):
		self.obj = obj
			
	def print_out(self):
		"""Print out all elements of usersDb (dict) from another object"""
		data = self.obj.get_users_data()
		print("-------------------------------")
		for k in data.keys():
			print("{:<12}{}".format("Member-"+ str(k) +":", data.get(k)))

def main():
	"""Main method - only to be run as standalone python program."""
	# 1st option - direct onject method
	users1 = Users()
	users1.display_users_data()

	#2nd option - create DisplayUserData of Users object and then call print_out method
	data2 = DisplayUserData(users1)
	data2.print_out()

	#3rd option - call print_out method directly, without asignig object to variable
	DisplayUserData(users1).print_out()


if __name__ == "__main__":
	main()

