print("Defining func to get multiline text ...")
def grf_usrinp():
	global gr_user_input
	gr_user_input = []
	entry = input("Enter BODY text, 'done' on its own line to send:\n----------------------------------------------------------------------\n")
	while entry != "done":
		gr_user_input.append(entry)
		entry = input("")
	gr_user_input = '\n'.join(gr_user_input)
	return gr_user_input

# assign return value user input func to variable:
print("Assigning return value user input func to variable ...")
print("\nStarting USER input: ")

print()
gr_MSG = grf_usrinp()

print("\n-------------------------------\nPrinting user input values ...")
print(gr_MSG)
