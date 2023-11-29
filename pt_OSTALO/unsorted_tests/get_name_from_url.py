#! /usr/bin/env python3
import argparse

# getting URL as first parameter ...
parser = argparse.ArgumentParser()
parser.add_argument('url', help = "The URL without trailing '/'")
args = parser.parse_args()

gr_URL = args.url

print("URL = ", gr_URL)

gr_3w, gr_FJL = gr_URL.rsplit('/', 1)

print("gr_3w = ", gr_3w)
print("gr_FJL = ", gr_FJL)

if ('.' in gr_FJL):
    gr_NM, gr_ext = gr_FJL.rsplit('.')
else:
    gr_NM = gr_FJL

print("gr_NM = ", gr_NM)
# print("gr_ext = ", gr_ext)

gr_TJTL = str(gr_NM.replace('-', ' '))
gr_SBJ = gr_TJTL.capitalize()
print("\n" + gr_SBJ + "\n" + gr_URL)

"""
python3 ./get_name_from_url.py http://www.majhost.com/gubd/fft.jjj/filename-gggg-zzzz.html
"""
