#! /usr/bin/env python3
### fibonacci series calculation
### start from n = 0, to ENDNUM
### suplied by user

## Inform user what is to be done:
print("""
This script calculates numbers in fibonacci series
from 0 to end number which you will supply.""")

## ask user to supply END number:
endn = int(input("Enter end number: "))

a, b = 1, 1
FB = 0
while FB < 2:
    print(1)
    FB += 1
   
while FB < endn:
    print(FB)
    a, b = b, a + b
    FB = a + b
  
