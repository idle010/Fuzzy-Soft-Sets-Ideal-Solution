#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy as np 
#dataset_name = "randsoftset.txt"
dataset_name = "example1.txt"

def prt_softset(sf):
    for obj in sf:
        print obj

def load_softset():
    softset = []
    for li in open(dataset_name):
        obj = li.strip("\n").split(",")
        obj = [float(c) for c in obj]
        softset.append(obj)

    return softset

def choice_value(sf):
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

def dot_vec(v1, v2):
    tmp = []
    for i in range(0, len(v1)):
        tmp.append(v1[i] * v2[i])
    return sum(tmp)


def weighted_choice_value(sf, weight):
    decision = []
    #candidate,pos = np.dot(sf[0], weight), 0
    candidate,pos = dot_vec(sf[0], weight), 0
    decision.append([candidate, pos])
    pos = 0

    for obj in sf[1:]:
        pos += 1
        #choicevalue = np.dot(obj, weight)
        choicevalue = dot_vec(obj, weight)
        if  choicevalue > decision[0][0]:
            decision = []
            decision.append([choicevalue, pos])
        elif choicevalue == decision[0][0]:
            decision.append([choicevalue, pos])

    return decision

if __name__ == '__main__':
    sfset = load_softset()
    prt_softset(sfset)
    weight = [1.0/2, 1.0/4, 1.0/8, 1.0/16]
    print weight
    result = weighted_choice_value(sfset, weight)
    for ret in result:
        print "The choicevalue is:%.4f position is:%d" % \
            (ret[0], ret[1])

