#! /usr/bin/env pyrthon3

import sys
import os

if len(sys.argv) < 2:
    print("There should be at least one filename as argumet to " + str(sys.argv[0]))
    sys.exit(1)

gr_FILES = []


# Check if files exist:
for FILE in sys.argv[1:]:
    if not os.path.isfile(FILE):
        print("There is no " + FILE + ".")
        print("Exiting. Bye.")
        sys.exit(1)
    else:
        gr_FILES.append(FILE)


print("The list of filenames:", end='')
print(gr_FILES)
