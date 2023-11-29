#! /usr/bin/env python3
# -*- coding=utf-8 -*-


print("Imported SubPackage_1.module_1 as m1 ...")
import SubPackage_1.module_1 as m1

print("Imported SubPackage_2.module_2 as m2 ...")
import SubPackage_2.module_2 as m2


print()
print("Running function info() from both modules ...")

m1.info()
m2.info()

display = '''[AppName]
	__init.py__
	AppName.py
	
	[SubPackage_1]
	   __init.py__
	   __pycache__
		   module_1.cpython-36.pyc
		module_1.py
		
	 [SubPackage_2]
		__init.py__
		__pycache__
			module_2.cpython-36.pyc
		 module_2.py
'''

print()
print("Package dir_struct:")
print(display)
