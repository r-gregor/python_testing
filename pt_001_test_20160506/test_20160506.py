#! /usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# Test-1 ---------------------------------
print("Test 1: " + "-"*100,)
print("""
gr_VAR1 = 1
if gr_VAR1 != 1:
	print("OK!")
else:
	print("Not OK!")

OUTPUT:
""",)
gr_VAR1 = 1
if gr_VAR1 != 1:
	print("OK!")
else:
	print("Not OK!")

	
# Test-2 ---------------------------------
print("\nTest 2: " + "-"*100,)
print("""
gr_VAR2 = "Redelonghi"
print("Gregor " + gr_VAR2)
print("%s %s --> %0.2f" % ("Gregor", gr_VAR2, 125.456789))

OUTPUT:
""",)
gr_VAR2 = "Redelonghi"
print("Gregor " + gr_VAR2)
print("%s %s --> %0.2f" % ("Gregor", gr_VAR2, 125.456789))


# Test-3 ---------------------------------
print("\nTest 3: " + "-"*100,)
print("""
s = "InterspammerS"
if 'spam' in s:
	has_spam = True
else:
	has_spam = False
print("has_spam=" + str(has_spam))

OUTPUT:
""",)
s = "InterspammerS"
if 'spam' in s:
	has_spam = True
else:
	has_spam = False

print("has_spam=" + str(has_spam))


# Test-4 ---------------------------------
print("\nTest 4: " + "-"*100,)
print("""
has_spam = 'spam' in s
print("has_spam=" + str(has_spam))

OUTPUT:
""",)
has_spam = 'spam' in s
print("has_spam=" + str(has_spam))



# Test-5 ---------------------------------
print("\nTest 5: " + "-"*100,)
print("""
print("Reading a file test-2.txt:"
f = open("test-2.txt") 		# Returns a file object
line = f.readline() 		# Invokes readline() method on file
while line:
	print line,		# trailing ',' omits newline character
#	print(line, end='')	# Use in Python 3
	line = f.readline()
f.close()

OUTPUT:

""",)
print("Reading a file test-2.txt:")
f = open("test-2.txt") 		# Returns a file object
line = f.readline() 		# Invokes readline() method on file
while line:
#	print(line,)		# trailing ',' omits newline character
	print(line, end='')	# Use in Python 3
	line = f.readline()
f.close()
print("")

# Test-6 ---------------------------------
print("\nTest 6: " + "-"*100)
print("Display a substring of string ...")

print("""
a = "Gregor Redelonghi"
printa([5:len(a)])

OUTPUT:
""",)
a = "Gregor Redelonghi"
print(a[5:len(a)])



# Test-7 ---------------------------------
print("\nTest 7: " + "-"*100,)
print("""
Use of dict ...

druzina = {
"oce" : "Gregor Redelonghi",
"mama" : "Tadeja Mali Redelonghi",
"hci-1" : "Zala Redelonghi",
"hci_2" : "Spela Redelonghi",
"sin" : "Mark Redelonghi"
}

print("\"Oce je " + druzina["oce"] + " in prva hci je " + druzina["hci-1"] + "\"")
print("dict \"druzina\" as list: " + str(list(druzina)))

gr_EXP="ci"
for gr_KEY in druzina:
	if gr_EXP in str(gr_KEY):
		print("Records whose KEY has \"" + gr_EXP + "\" in name:")
		print(gr_KEY + " : " + druzina(gr_KEY))

OUTPUT:
""",)
druzina = {
"oce" : "Gregor Redelonghi",
"mama" : "Tadeja Mali Redelonghi",
"hci-1" : "Zala Redelonghi",
"hci_2" : "Spela Redelonghi",
"sin" : "Mark Redelonghi"
}

print("\"Oce je " + druzina["oce"] + " in prva hci je " + druzina["hci-1"] + "\"")
print("dict \"druzina\" as list: " + str(list(druzina)))

gr_EXP="ci"
print("\nRecords whose KEY has \"" + gr_EXP + "\" in name:")
for gr_KEY in druzina:
	if gr_EXP in gr_KEY:
		print("\"" + gr_EXP + "\" is in KEY " + gr_KEY + ": " + druzina[gr_KEY])


		



# Test-8 ---------------------------------
print("\nTest 8: " + "-"*100,)
print("""
for n in range(1,10):
	print("2 to the %d power is %d" % (n, 2**n)

OUTPUT:
""",)

for n in range(1,10):
	print("2 to the %d power is %d" % (n, 2**n))

