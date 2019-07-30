#-*- coding:utf-8 -*-
import math

def primeFactors(num):
    number = num
    result = ''
    factor = 2
    while number > 1:
        cnt = 0
        while number % factor == 0:
            number = math.floor(number / factor)
            cnt += 1
        if cnt > 0:
            if cnt > 1:
                result += "({}**{})".format(factor,cnt)
            else:
                result += "({})".format(factor)
        factor += 1
    return result