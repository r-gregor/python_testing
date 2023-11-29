#! /usr/bin/env python
# -*- coding: utf-8 -*-

# copy file from SRD to DEST

# setup
import os, shutil

gr_PRFX="/home/gregor.redelonghi/majstaf/coding/testing-en/PYTHON-en_testing"
gr_SRCD=gr_PRFX + "/SRC1"
gr_FJL="src-fajl-1.txt"
gr_SRCF=gr_SRCD + "/" + gr_FJL
gr_DSTD="/home/gregor.redelonghi/majstaf/coding/testing-en/PYTHON-en_testing/DEST1"
gr_DEST=gr_DSTD + "/"

print("Prefix: ", gr_PRFX)
print("Src: ", gr_SRCD)
print("Source file :" + gr_FJL)
print("Sorce: " + gr_SRCF)
print("Dest: " + gr_DEST)

from distutils.dir_util import copy_tree
copy_tree(gr_SRCD + "/" , gr_DSTD)




