#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# V2 [20180701]: image list from function in file [img_sizes.py] that sorts images by width (accending)

import os, sys
import datetime as dt
import img_sizes as imgs


# timestamp
def tms():
	return dt.datetime.now().strftime('%Y%m%d_%H%M%S')
	
# datestamp
dts = dt.datetime.now().strftime('%Y%m%d')

# MESSAGE:
print("[ {} ] -- Starting {} ...".format(tms(), sys.argv[0]))


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
# test print
# print("test printing header and footer ...")
# print(wpg_head + "\n ... \n" + wpg_foot)


# subdir with images
subd = "ponjave_slike"

# curdir
curdir = os.getcwd()


my_file = "ponjave_slike_" + str(dts) + "_V2.html"

print("[ {} ] -- Output file: {}.".format(tms(), my_file))


# images subdir full path
flpth = os.path.join(curdir, subd)

# test print
# print(flpth)

sorted_imgs = imgs.get_sorted_imgs()

# V2 new: get list of images sorted by width
for imgname in sorted_imgs:
	# print(imgname)
	limg.append(imgname)

# test print	
# print(limg)


with open(my_file, "w") as wpg:
	wpg.write(wpg_head)
	wpg.write("\n")
	
	for imgname in limg:
		wpg.write("<img src=\"" + subd + "/" + imgname + "\">&nbsp\n")
	
	wpg.write("\n")
	wpg.write(wpg_foot)
