#! /usr/bin/env python3

import sys

class Me:
    def __init__(self, namestring):
        self.nms = namestring
        
    def get_name(self):
        return self.nms
        
    def get_rev_name(self):
        S = list(self.nms)
        RS = []
        for N in range(len(S)):
            RS.append(S.pop())
        return ''.join(RS)

    def print_rev_nm(self):
        print("{:<20} {}".format("My name is:", self.get_name()))
        print("{:<20} {}".format("My name REVERSED is:", self.get_rev_name()))
        print("-"*60)


# main        
# execute only if run as standalone script:
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage:\n\t", sys.argv[0], "[name | name surname strig]")
        exit(1)

    print()
    print("Using stack data structure to reverse the name string:")
    print("-"*60)

    nm = Me(sys.argv[1])
    nm.print_rev_nm()


            