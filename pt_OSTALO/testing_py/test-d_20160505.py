#! /usr/bin/env python
# -*- coding: UTF-8 -*-

print("Test 1 " + "-"*100) # ----------------------------------------------------

gr_FJL = ["Gregor", 20160505, 20150505, 20140505, "Tadeja"]
print(gr_FJL)

print( """
CODE:
    gr_A = 2016
    if str(gr_A) in str(gr_FJL):
        print( str(gr_A) + " is in!"
    else:
        print( str(gr_A) + " is NOT in!"

OUTPUT:
""",)

gr_A = 2016
if str(gr_A) in str(gr_FJL):
    print( str(gr_A) + " is in!")
else:
    print( str(gr_A) + " is NOT in!")


print( "\nTest 2 " + "-"*100) # --------------------------------------------------
gr_DCT = {
"oci" : "Gregor Redelonghi",
"mami" : "Tadeja Mali Redelonghi",
"hci_1" : "Zala Redelonghi",
"hci_2" : "Špela Redelonghi",
"sin_1" : "Mark Redelonghi",
"zci-1" : "Čukovićijus Žađašćki"
}

print( gr_DCT)
print( """
CODE:
    gr_B = "ci"
    print( "print( those elements of dict, whose key has \"" + str(gr_B) + "\" in name:")
    for key in gr_DCT:
       if gr_B in key:
           print( key + ": " + gr_DCT[key]

OUTPUT:
""",)

gr_B = "ci"
print( "display those elements of dict, whose key has \"" + str(gr_B) + "\" in name:")
for key in gr_DCT:
    if gr_B in key:
        print( key + ": " + gr_DCT[key])


print( "\nTest 3 " + "-"*100) # --------------------------------------------------

