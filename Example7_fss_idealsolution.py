#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy as np 
#dataset_name = "randsoftset.txt"
dataset_name = "example7.txt"

def prt_softset(sf):
    for obj in sf:
        print obj

def dot_vec(v1, v2):
    tmp = []
    for i in range(0, len(v1)):
        tmp.append(v1[i] * v2[i])
    return sum(tmp)

def load_softset():
    softset = []
    for li in open(dataset_name):
        obj = li.strip("\n").split(",")
        obj = [float(c) for c in obj]
        softset.append(obj)

    return softset

def norm_Ham_dist(v1, v2):
    ret_value = 0
    for i in range(0, len(v1)):
        ret_value += abs(v1[i] - v2[i])
    return ret_value * 1.0 / len(v1)



def weighted_Ham_dist(v1, v2, weight):
    ret_value = 0
    for i in range(0, len(v1)):
        ret_value += abs(v1[i] - v2[i]) * weight[i]
    return ret_value 


def norm_Ham_dist_choice(sf):
    decision = []
    u_goal = sf[0]
    n_hamdistance = []
    for i in range(1, len(sf)):
        n_hamdistance.append(norm_Ham_dist(u_goal, sf[i]))


    print "The normalized Hamming distance is:", n_hamdistance
    candidate,pos = n_hamdistance[0], 0
    decision.append([candidate, pos])
    pos = 0

    for dist in n_hamdistance[1:]:
        pos += 1
        if  dist < decision[0][0]:
            decision = []
            decision.append([dist, pos])
        elif dist == decision[0][0]:
            decision.append([dist, pos])

    return decision


def weighted_Ham_dist_choice(sf, weight):
    decision = []
    u_goal = sf[0]
    n_hamdistance = []
    for i in range(1, len(sf)):
        n_hamdistance.append(weighted_Ham_dist(u_goal, sf[i], weight))

    print "The weighted Hamming distance is", n_hamdistance
    candidate,pos = n_hamdistance[0], 0
    decision.append([candidate, pos])
    pos = 0

    for dist in n_hamdistance[1:]:
        pos += 1
        if  dist < decision[0][0]:
            decision = []
            decision.append([dist, pos])
        elif dist == decision[0][0]:
            decision.append([dist, pos])

    return decision


if __name__ == '__main__':
    sfset = load_softset()
    prt_softset(sfset)
    result = norm_Ham_dist_choice(sfset)
    for ret in result:
        print "The min distance is:%.4f The choice is:h%d" % \
            (ret[0], ret[1])

    weight = [1.0/2, 1.0/4, 1.0/8, 1.0/16, 1.0/32, 1.0/64, 0]
    print weight
    result = weighted_Ham_dist_choice(sfset, weight)
    for ret in result:
        print "The min distance is:%.4f The choice is:h%d" % \
            (ret[0], ret[1])


