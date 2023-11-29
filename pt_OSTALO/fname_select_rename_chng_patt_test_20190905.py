#! /usr/bin/env python3

import os, sys

fjls = []

pat = "txt"
newp = "backup"

if len(sys.argv) < 2:
    print("No file selected!")
    sys.exit(1)
    
for el in sys.argv:
    fjls.append(el)
    
print(fjls)

for FF in fjls:
    if pat in FF:
        print("renaming {} to {}".format(FF, FF.replace(pat, newp)))

