#!/usr/bin/env python
# -*- coding: utf-8 -*-
#dataset_name = "randsoftset.txt"
dataset_name = "example6.txt" # also for Example2

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

def comp_two_objs(v1,v2):
    k = 0
    for i in range(0,len(v1)):
        if (v1[i] >= v2[i]):
            k += 1
    return k

def gen_comp_scotable(fss):
    ret = []
    for e1 in fss:
        tmp = []
        for e2 in fss:
            tmp.append(comp_two_objs(e1, e2))
        ret.append(tmp)
    return ret

def gen_score(ret):
    compurow = []
    for e in ret:
        compurow.append(sum(e))
    print "row-sum:", compurow

    compucol = []
    for i in range(0, len(ret[0])):
        tmp = 0
        for e in ret:
            tmp += e[i]
        compucol.append(tmp)
    print "col-sum:", compucol

    print "Score Table="
    score_pos = []
    for i in range(0, len(compucol)):
        scorei = compurow[i] - compucol[i]
        print compurow[i], "&", compucol[i], "&", scorei
        score_pos.append( scorei )

    return score_pos

def get_choice(score):
    decision = []
    candidate,pos = score[0], 0
    decision.append([candidate, pos])
    pos = 0

    for obj in score[1:]:
        pos += 1
        choicevalue = obj
        if  choicevalue > decision[0][0]:
            decision = []
            decision.append([choicevalue, pos])
        elif choicevalue == decision[0][0]:
            decision.append([choicevalue, pos])

    return decision

from operator import itemgetter
from collections import OrderedDict
def sort_score_order(data_list):
    data_dict = {}
    for i in range(0,len(data_list)):
        data_dict[i] = data_list[i] 
    
    print data_dict
    retdata = OrderedDict(sorted(data_dict.items(), key=lambda t: t[1]))
    return retdata.keys()

if __name__ == '__main__':
    sfset = load_softset()
    print "------------------\nSoft Set = "
    prt_softset(sfset)
    print "------------------\nComparison Table = "
    score_table = gen_comp_scotable(sfset)
    prt_softset(score_table)

    score = gen_score(score_table)
    print "------------------\nScore:"
    print score
    choice = get_choice(score)
    for ch in choice:
        print "The max score is:%d , pos is:%d" % (ch[0], ch[1])

    tmp_position = sort_score_order(score)
    print tmp_position
    print " > ".join([str(c) for c in tmp_position])

