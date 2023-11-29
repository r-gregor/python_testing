#! /usr/bin/env python3
'''
20181011:	V1
TO DO: 	classes with methods that return data:
		class mesec --> data number of days in month
					--> method to return number of days in month
					--> method to return number of workdays depending on the start day of the month
					--> method to print report from prevoius two methods
					
'''


teden = ['PO', 'TO', 'SR', 'CE', 'PE', 'SO', 'NE']
dni_v_mescu = 	{	'Januar': 31,
					'Februar': 28,
					'Marec': 31,
					'April': 30,
					'Maj': 31,
					'Junij': 30,
					'Julij': 31,
					'Avgust': 31,
					'September': 30,
					'Oktober': 31,
					'November': 30,
					'December': 31
				}

mesci = list(dni_v_mescu.keys())

		

def ure_po_dnevih(mesec, zacetek):
	start = zacetek
	k = 1
	DD = 0
	dni = dni_v_mescu[mesec]
	print("Mesec: {}".format(mesec))
	while k < dni:
		if start > len(teden) - 1:
			start = 0
		
		if teden[start] != 'SO' and teden[start] != 'NE':
			DD +=1
			
		print("{}: {}; st DD: {}".format(k, teden[start], DD))
	
		start += 1
		k += 1
	
	st_ur = DD * 8

	print("Stvilo delovnih ur: {}".format(st_ur))



def ure_na_mesec(mesec, zacetek):
	"""
	function to print number of work hours per month given the
	start day
	"""
	start = zacetek
	k = 1
	DD = 0
	dni = dni_v_mescu[mesec]
	
	while k < dni:
		if start > len(teden) - 1:
			start = 0
		
		if teden[start] != 'SO' and teden[start] != 'NE':
			DD +=1
		start += 1
		k += 1
	
	st_ur = DD * 8
	print("Mesec: {}, Stevilo dni: {}, Prvi dan: {}, Stevilo delovnih ur: {}".format(mesec,dni, teden[zacetek], st_ur))

	
def ure_na_mesec_po_dnevih(mesec):
	"""
	Function to print number of workhours per month  for each start day of a week
	"""
	for i in range (0,7):
		ure_na_mesec(mesec, i)
		

def ure_za_vse_mesece():
	print("Ure na mesec po zacetnem dnevu:")
	for msc in mesci:
		ure_na_mesec_po_dnevih(msc)
		print("-"*80)
		

# EXECUTE

'''
test
# ure_po_dnevih('Februar', 0)
# ure_na_mesec('Januar', 0)
'''

ure_za_vse_mesece()


