#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy as np 
""" 
If you want to test with a large random dataset, 
change the dataset name to randsoftset.txt 
run command:           python randgen_softset.py 
generate a new random soft set (F,A)
"""

#dataset_name = "randsoftset.txt"
dataset_name = "example9.txt"

def prt_softset(sf):
    """Print the soft set
    """
    for obj in sf:
        print obj

def dot_vec(v1, v2):
    """ Vector multiplication
    """
    tmp = []
    for i in range(0, len(v1)):
        tmp.append(v1[i] * v2[i])
    return sum(tmp)

def load_softset():
    """ Fetches rows from a soft set.
    """
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
    """ The weighted Hamming distance
    """
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
    """The fss-ideal ideal solution Algorithm
    Args:
        sf: The Table of soft set.
        weight: Subjective weight
    Returns:
        decision: A list of the the decision-making 
        n_hamdistance: A list of Hamming distance
    """
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

    return decision, n_hamdistance

from operator import itemgetter
from collections import OrderedDict
def sort_dist_order(data_list):
    data_dict = {}
    for i in range(0,len(data_list)):
        data_dict[i] = data_list[i] 
    
    print data_dict
    retdata = OrderedDict(sorted(data_dict.items(), key=lambda t: t[1]))
    return retdata.keys()

if __name__ == '__main__':
    sfset = load_softset()
    prt_softset(sfset)

    weight = [2.0/15, 2.0/15, 2.0/15, 5.0/15 , 2.0/15, 2.0/15]
    result = weighted_Ham_dist_choice(sfset, weight)
    for ret in result[0]:
        print "The min distance is:%.4f The choice is:h%d" % \
            (ret[0], ret[1])
    tmppos = sort_dist_order(result[1])
    
    print " < ".join([str(c ) for c in tmppos])


