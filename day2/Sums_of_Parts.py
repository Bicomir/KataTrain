#-*- coding:utf-8 -*-
def parts_sums(ls):
    res = [0]
    l = len(ls) - 1
    for i in range(l,-1,-1):
        res.append(ls[i] + res[l-i])
    res = res[::-1]
    return res

