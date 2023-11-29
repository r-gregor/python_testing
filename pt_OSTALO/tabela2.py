st_0 = 4
st_1 = 10
st_2 = 20
st_3 = 12
st_4 = 4

#Needed for format specifying padding in SECTION-2:
s0 = str(st_0)
s1 = str(st_1)
s2 = str(st_2)
s3 = str(st_3)
s4 = str(st_4)

L_crta = st_0 + st_1 + st_2 + st_3 + st_4

def crt():
	CRT = "-" * L_crta
	print(CRT)


# SECTION-1
# padding declared ditectly at format specifier:
crt() # -----------
print('{0:<4}{1:<10}{2:<20}{3:<12}{4:<4}'.format("#", "Ime", "Priimek", "Sorodstvo", "Spol"))
crt() # -----------
print('{0:<4}{1:<10}{2:<20}{3:<12}{4:<4}'.format("1", "Gregor", "Redelonghi", "Oče", "M"))
print('{0:<4}{1:<10}{2:<20}{3:<12}{4:<4}'.format("2", "Tadeja", "Mali Redelonghi", "Mama", "Ž"))
print('{0:<4}{1:<10}{2:<20}{3:<12}{4:<4}'.format("3", "Špela", "Redelonghi", "Hči-2", "Ž"))
crt() # -----------


# SECTION-2
# padding declared indirectla trough a "str(padding)" variable:
crt() # -----------
print('{0:<{s_0}}{1:<{s_1}}{2:<{s_2}}{3:<{s_3}}{4:<{s_4}}'.format("#", "Ime", "Priimek", "Sorodstvo", "Spol", s_0=s0, s_1=s1, s_2=s2, s_3=s3, s_4=s4))
crt() # -----------
print('{0:<{s_0}}{1:<{s_1}}{2:<{s_2}}{3:<{s_3}}{4:<{s_4}}'.format("1", "Gregor", "Redelonghi", "Oče", "M", s_0=s0, s_1=s1, s_2=s2, s_3=s3, s_4=s4))
print('{0:<{s_0}}{1:<{s_1}}{2:<{s_2}}{3:<{s_3}}{4:<{s_4}}'.format("2", "Tadeja", "Mali Redelonghi", "Mama", "Ž", s_0=s0, s_1=s1, s_2=s2, s_3=s3, s_4=s4))
print('{0:<{s_0}}{1:<{s_1}}{2:<{s_2}}{3:<{s_3}}{4:<{s_4}}'.format("3", "Špela", "Redelonghi", "Hči-2", "Ž", s_0=s0, s_1=s1, s_2=s2, s_3=s3, s_4=s4))
crt() # -----------


# SECTION-3
# padding declared in list of strings with string method .ljust(padding):
crt() # -----------
print('{0:}{1:}{2:}{3:}{4:}'.format("#".ljust(st_0), "Ime".ljust(st_1), "Priimek".ljust(st_2), "Sorodstvo".ljust(st_3), "Spol".ljust(st_4)))
crt() # -----------
print('{0:}{1:}{2:}{3:}{4:}'.format("1".ljust(st_0), "Gregor".ljust(st_1), "Redelonghi".ljust(st_2), "Oče".ljust(st_3), "M".ljust(st_4)))
print('{0:}{1:}{2:}{3:}{4:}'.format("2".ljust(st_0), "Tadeja".ljust(st_1), "Mali Redelonghi".ljust(st_2), "Mama".ljust(st_3), "Ž".ljust(st_4)))
crt() # -----------


