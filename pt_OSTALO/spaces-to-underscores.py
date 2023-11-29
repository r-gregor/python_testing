#! /usr/bin/env python3

import re
# import pyperclip
import sys

if len(sys.argv) != 2:
	print("""Usage:
	{} <STRING>""".format(sys.argv[0]))
	sys.exit(1)
  
S = sys.argv[1]

S2 = re.sub(r"\s+", "_", S).rsplit('.')[0].lower().rsplit('.')[0]

# PrintOut:
print(S2)

# pipe through putclip (bash) on Cygwin
# or uncomment the line below:
# pyperclip.copy(S2)


