#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

"""
In some cases, we need large data to test the program.
This program automatically generates fuzzy soft sets randomly.
This is especially useful for testing the rank reversal.
"""

"""
Change the two values to produce the soft set you want 
attrib: Number of attributes
objects:Number of objects
"""
attrib = 40
objects = 100

"""
Result output file: Randsoftset. txt
"""
filename = "randsoftset.txt"

def randgen_softset():
    softset = []
    for i in range(0, objects):
        obj = []
        for j in range(0, attrib):
            obj.append("%.3f" % random.random())
        softset.append(obj)
    return softset        

def write_softset(sf):
    fo = open(filename, "w")
    for obj in sf:
        li = ",".join(obj) + "\n"
        fo.write(li)


if __name__ == '__main__':
    write_softset(randgen_softset())

