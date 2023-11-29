#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# filename: hashlib_sha256_test_02_oop.py

import hashlib
import sys


class HashTestOOP:
    def __init__(self, string):
        self.string = string


    def hash_string(self, str2):
        """
        Return a SHA-256 hash of the given string
        """
        return hashlib.sha256(str2.encode('utf-8')).hexdigest()

    def redijiTest(self):
        fml = {}
        for nm in ["Špela", "Spela", "Gregor", "Zala", "Mark", "Tadeja Mali"]:
            strng = nm + " Redelonghi"
            fml[self.hash_string(strng)] = strng

        for hsh, nm in fml.items():
            print(f"{hsh} -- {nm}")

def main():
    if len(sys.argv) != 2:
        print("You mast supply a string as argument!")
        return
    else:
        arg = sys.argv[1]

    hto  = HashTestOOP(arg)

    print(hto.hash_string(arg) + " -- " + arg)

    # TEST
    hto.redijiTest()

if __name__ == "__main__":
    main()
else:
    print("Cannot run this as modula but only as satndalone program!")
    sys.exit(1)

