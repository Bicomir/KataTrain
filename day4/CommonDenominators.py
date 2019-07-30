# -*- coding:utf-8 -*-
import math
def convertFracts(lst):
    lst = processList(lst)
    if len(lst) > 1:
        cM = getCM(lst)
        res =[]
        for item in lst:
            tmp = math.floor(cM / item[1])*item[0]
            res.append([tmp, cM])
        return res
    else:
        return lst

# 找最小公分母，也就是所有公分母的最小公倍数
def maxDivisionWay(a, b):
    tiple = a * b
    while(b != 0):
        tmp = a % b
        a = b
        b = tmp
    return a

def minDivisionWay(a, b):
    tiple = a * b
    tmp = maxDivisionWay(a, b)
    min = math.floor(tiple / tmp)
    return min

def processList(lst):
    length = len(lst)
    res = []
    if length > 1:
        for item in lst:
            gcd = maxDivisionWay(item[0],item[1])
            res.append([math.floor(item[0]/gcd),math.floor(item[1]/gcd)])
        return res
    else:
        res = lst
        return res

def getCM(res):
    lcm = res[0][1]
    for item in res:
        lcm = minDivisionWay(item[1],lcm)
    return lcm
