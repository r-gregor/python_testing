#! /usr/bin/env python3
# -*- coding: utf8 -*-

'''
TERMINAL ESCAPE SEQUENCE:
    u"\u001b[
OR
    \x1b[
OR
    \033[   

'''

import os
os.system('clear')

def crt(ch, num):
    print("\n" + ch*num)


print("PRINTING TERMINAL COLORS!")
    
crt('-', 80)
print("Just numbers ...\n")
for i in range(0, 16):
     for j in range(0, 16):
         code = str(i * 16 + j)
         print("\x1b[38;5;" + code + "m " + code.ljust(4), end = '')
     print ("\x1b[0m")
     
crt('-', 80)
print("Backgrounds AND numers ...\n")
import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        print("\x1b[48;5;" + code + "m " + code.ljust(4), end = '')
    print("\x1b[0m")
    
print("DONE!")

# MY way -----------------------------------------------------------------------------------------------------
print("\nMY WAY ...")
print("BACKGROUNDS IN FORWARD ORDER AND NUMS IN BACKWARD ORDER:\n")
C1 = [NUM1 for NUM1 in range(0, 256)]
C2 = [NUM2 for NUM2 in range(255, -1, -1)]

# print(C1)
# print(C2)

print("PRINTING TERMINAL COLORS!")
 
'''
crt('-', 80)
print("Just numbers ...\n")
for i in C1:
    code = str(C1[i])
    if i == 0:
        print("\x1b[38;5;" + code + "m " + code.ljust(4), end = '')
        continue
    elif i % 16 == 0:
        print("\n", end='')
    print("\x1b[38;5;" + code + "m " + code.ljust(4), end = '')
    print ("\x1b[0m", end = '')
''' 
crt('-', 80)
print("Just numbers ...\n")
for i in C1:
    code = str(C1[i])
    if i == 0:
        print("\033[38;5;" + code + "m " + code.ljust(4), end = '')
        continue
    elif i % 16 == 0:
        print("\n", end='')
    print("\033[38;5;" + code + "m " + code.ljust(4), end = '')
    print ("\033[0m", end = '')


crt('-', 80)
print("Backgrounds AND numers ...\n")
import sys
for i in range(0, 256):
    code = str(C1[i])
    bckg = str(C2[i])
    if i == 0:
        print("\x1b[48;5;" + code + "m" + "\x1b[38;5;" + bckg + "m " + code.ljust(4), end='')
        continue
    elif i % 16 == 0:
            print("\n", end='')
            print("\x1b[48;5;" + code + "m" + "\x1b[38;5;" + bckg + "m " + code.ljust(4), end='')
            print("\x1b[0m", end = '')
    else:
        print("\x1b[48;5;" + code + "m" + "\x1b[38;5;" + bckg + "m " + code.ljust(4), end = '')
        print("\x1b[0m", end = '')
    
print("\nDONE!")


