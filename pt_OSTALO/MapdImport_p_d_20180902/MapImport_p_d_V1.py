#! /usr/bin/env python3

camp = {};

with open('camp_in.txt', 'r') as fin:
    for line in fin.readlines():
        if line != "":
            # test print
            # print(line.strip())
            kat, nsez, vsez = line.strip().split(',')
            camp[kat] = [nsez, vsez]

# test print
# print(camp)

print()
print("{0:<15}{1:>10}{2:>10}".format("camp [HRK]", "nsez", "vsez"))

print("-"*35)
for k, v in camp.items():
    print("{0:<15}{1:>10}{2:>10}".format(k, camp[k][0], camp[k][1]))
