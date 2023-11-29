#! /usr/bin/env python3

# ls -1 | grep '^j' | cut -b 7- > ~/jd_files.txt
#ls -1 ~/Dropbox/ODPRTO/MCDN_en/JAVA_en/JAVA_en_testing/ | grep '^j' | cut -b 7- > ~/jn_files.txt


jnL = []
jdL = []

with open("jd_files.txt", 'rt') as fj:
    for oneL in fj.readlines():
        jdL.append(oneL.strip())

with open("jn_files.txt", 'rt') as fn:
    for oneL in fn.readlines():
        jnL.append(oneL.strip())

# print(jdL)
# print(jnL)

for jd in jdL:
    for jn in jnL:
        if jd == jn:
            print(jd + " and " + jn + " are a MATCH!")
        else:
            print(jd + " only in DOMA, " + jn + " only in EN.")
