#! /uer/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
import os

curdir = os.getcwd()

# subdir with images
subd = "ponjave_slike"

# images subdir full path
flpth = os.path.join(curdir, subd)

imgsL = os.listdir(flpth)

imgsD = {}
imgsL_sorted = []

# NEW [20180701]: function return list of imgs sorted by width
def get_sorted_imgs():
    for el in imgsL:
        # if file not an image file: continue
        if not any(end in el for end in ['jpg', 'png', 'gif', 'bmp']):
            continue
        
        # if image file: {'imagename': width}
        else:
            img = Image.open(os.path.join(flpth, el))
            imgsD[el] = img.size[0]

    # test print     
    # print(imgsD)

    # sorted dict by width:
    # LIST!!
    imgsD_sorted = sorted(imgsD.items(), key=lambda kv: kv[1])
    
    # test print
    # print()
    # print(imgsD_sorted)

    for el in imgsD_sorted:
        imgsL_sorted.append(el[0])

    # test print        
    # print()    
    # print(imgsL_sorted)
    
    return imgsL_sorted
