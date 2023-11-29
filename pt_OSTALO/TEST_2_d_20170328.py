def hr():
	HR = "-"
	print(HR*78)

gr_IME = "Zala"
print("Hello", gr_IME + "!")

deli = ["Hello", gr_IME + "!", "\n\tKako si kaj!?"]
stavek = ' '.join(deli)
print(stavek)

##hr()
##stp = 2
##end = 60
##strt = 0
##knc = end + stp
##for NUM in range(strt, knc, stp):
##	print(NUM)

hr()
# Print system path list for python3
import sys

print("Print system path list for python3 ...")
for line in sys.path:
	print(line)

hr()
vr_POJAVI = ["Sončno", "Oblačno", "Deževno", "Vetrovno", "Pre-LEPO"]
print("Vreme danes je lahko karkoli od sledecega:")
for NUM, VR in enumerate(vr_POJAVI, 1):
	print(NUM, "- " + VR)

print("\n")
hr()



