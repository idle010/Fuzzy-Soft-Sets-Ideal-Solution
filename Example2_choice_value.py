#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
If you want to test with a large random dataset, 
change the dataset name to randsoftset.txt 
run command:           python randgen_softset.py 
generate a new random soft set (F,A)
"""
#dataset_name = "randsoftset.txt"
dataset_name = "example1.txt"

def prt_softset(sf):
    for obj in sf:
        print obj

def load_softset():
    """
    Fetches rows from a soft set.
    """
    softset = []
    for li in open(dataset_name):
        obj = li.strip("\n").split(",")
        obj = [float(c) for c in obj]
        softset.append(obj)

    return softset

def choice_value(sf):
    """The choice value Algorithm
    Args:
        sf: The Table of soft set.
    Returns:
        decision: A list of the the decision making 
        example:  [[4.0, 0], [4.0, 5], ...]
    """
    decision = []
    candidate,pos = sum(sf[0]), 0
    decision.append([candidate, pos])
    pos = 0

    for obj in sf[1:]:
        pos += 1
        choicevalue = sum(obj)   # get the sum of an object $F(u_i)$
        if  choicevalue > decision[0][0]:
            decision = []
            decision.append([choicevalue, pos])
        elif choicevalue == decision[0][0]:
            decision.append([choicevalue, pos])
    return decision

def weighted_choice_value(sf, weight):
    """The choice value Algorithm
    Args:
        sf: The Table of soft set.
        weight:the weights specified by the experts
    Returns:
        decision: A list of the the decision making 
        example:  [[4.0, 0], [4.0, 5], ...]
    """
    decision = []
    candidate,pos = sum(sf[0]), 0
    decision.append([candidate, pos])
    pos = 0

    for obj in sf[1:]:
        pos += 1
        choicevalue = sum(obj)
        if  choicevalue > decision[0][0]:
            decision = []
            decision.append([choicevalue, pos])
        elif choicevalue == decision[0][0]:
            decision.append([choicevalue, pos])
    return decision

if __name__ == '__main__':
    sfset = load_softset()
    prt_softset(sfset)
    result = choice_value(sfset)
    for ret in result:
        print "The choicevalue is:%.3f position is:%d" % \
            (ret[0], ret[1])


