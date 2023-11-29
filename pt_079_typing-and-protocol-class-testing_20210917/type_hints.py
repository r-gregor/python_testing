'''
	from https://www.youtube.com/watch?v=rytP_vIjzeE

	1 - make venv
	3 - (venv)pip install mypy
		module "typing" in stdlib from version 3.8

	Test:
		(venV)python.exe -m mypy [python_file.py]

	Union[type1, type2]	-- mypy accepts both types
	Any					-- mypy accepts any type
'''

from typing import Callable, List, Dict, Any, Union

def factorial(i: Union[int, float]) -> int:
	i = int(i)
	if i < 0:
		# return None --> typing error !!
		return -1
	
	if i == 0:
		return 1
	
	return i * (factorial(i-1))

# print(factorial(3))

def map_int_list(fnc: Callable, list: List[int]) -> List[int]:
	''' return a list of factorials of elements in input list'''
	return [fnc(el) for el in list]

def map_int_dict(fnc: Callable, dct: Dict[Any, int]) -> Dict[Any, int]:
	''' return a dictionary of factorials of values in input dict'''
	return {key: fnc(value) for key, value in dct.items()}


# my function -- NO mypy error
def print_factorials(list):
	print(map_int_list(factorial, list))


if __name__ == "__main__":
	L=[x for x in range(6)]
	print_factorials(L)

	L.append(7.2)
	print_factorials(L)

	# NO mypy error
	print_factorials([0,2,4,6,7.2])

	# mypy error
	print(map_int_list(factorial, [0,2,4,6,7.2]))


	print(map_int_dict(factorial, {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}))
	print(map_int_dict(factorial, {'zero': 0, 'one': 1, (1, 2): 2.5, 'three': 3, 4: 4.3, 'five': 5, 'six': 6}))
