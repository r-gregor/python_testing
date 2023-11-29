#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import sys


def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def redijiTest():
    fml = {}
    for nm in ["Špela", "Spela", "Gregor", "Zala", "Mark", "Tadeja Mali"]:
        strng = fnm = nm + " Redelonghi"
        fml[hash_string(strng)] = strng

    for hsh, nm in fml.items():
        print(f"{hsh} -- {nm}")

def main():
    if len(sys.argv) != 2:
        print("You mast supply a string as argument!")
        return
    else:
        arg = sys.argv[1]

    print(hash_string(arg) + " -- " + arg)

    # redijiTest
    redijiTest()

if __name__ == "__main__":
    main()
else:
    print("Cannot run this as modula but only as standalone program!")
    sys.exit(1)

