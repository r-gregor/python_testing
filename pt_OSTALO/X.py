L1 = []
def print_me(fst, *args):

	L1.append(fst)
	for el in args:
		L1.append(el)

	print(f'first = {L1[0]}')
	print(f'last = {L1[-1]}')
	print(f'rest = {L1[1:len(L1) - 1]}')

print_me('AAA', 'BBB', 'DDD', 'KKK', 'ZZZ')
