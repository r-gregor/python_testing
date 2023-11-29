#! /usr/bin/env python3

import os, sys
import datetime as dt

# list of images
limg = []


# header
wpg_head = """<html>
<head></head>
<body>
<h2>PONJAVE</h2>
<p>
"""

wpg_foot = """</p>
</body>
</html>
"""
print("test printing header and footer ...")
print(wpg_head + "\n ... \n" + wpg_foot)


# subdir with images
subd = "ponjave_slike"


# curdir
curdir = os.getcwd()

# timestamp
def tms():
    return dt.datetime.now().strftime('%Y%m%d_%H%M%S')
    
# datestamp
dts = dt.datetime.now().strftime('%Y%m%d')

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))

my_file = "ponjave_slike_" + str(dts) + ".html"

# test
print(my_file)

# images subdir full path
flpth = os.path.join(curdir, subd)

# test
print(flpth)

for imgname in os.listdir(flpth):
    # print(imgname)
    limg.append(imgname)

print(limg)


with open(my_file, "w") as wpg:
    wpg.write(wpg_head)
    wpg.write("\n")
    
    for imgname in limg:
        wpg.write("<img src=\"" + subd + "/" + imgname + "\">&nbsp\n")
    
    wpg.write("\n")
    wpg.write(wpg_foot)
