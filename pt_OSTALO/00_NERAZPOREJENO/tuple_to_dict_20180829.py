# data lists
L = [		('camp_odr', 40, 50),
			('camp_otr', 20, 25),
			('camp_parc', 70, 80),
			('camp_avto', 20, 20),
			('camp_el', 20, 20) ]
			
D = {}

for line in L:
	D[ line[0] ] = [ line[1], line[2] ]
	
# print(D)

camp_odr_nsez = D['camp_odr'][0]
camp_odr_vsez = D['camp_odr'][1]

camp_otr_nsez = D['camp_otr'][0]
camp_otr_vsez = D['camp_otr'][1]

camp_parc_nsez = D['camp_parc'][0]
camp_parc_vsez = D['camp_parc'][1]

camp_avto_nsez = D['camp_avto'][0]
camp_avto_vsez = D['camp_avto'][1]

camp_el_nsez = D['camp_el'][0]
camp_el_vsez = D['camp_el'][1]

for nms in ['odr', 'otr', 'parc', 'avto', 'el']:
	print("camp_"+nms+"_nsez = ", eval("camp_"+nms+"_nsez"))
	print("camp_"+nms+"_vsez = ", eval("camp_"+nms+"_vsez"))

