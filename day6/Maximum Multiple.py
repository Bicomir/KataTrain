# -*- coding:utf-8 -*-
import math
def max_multiple(divisor, bound):
    factor = math.floor(bound / divisor)
    N = factor * divisor
    N1 = (factor+1)*divisor
    if N <= bound and N1 > bound and N >= 0:
        return N


