#-*- coding:utf-8 -*-
'''
思路：
(1)放入序列是有顺序要求的，切不可有空隙，故此一个个的插入；
(2)每次插入需要比较 2 *arr[yi] + 1 与 3 * arr[zi] + 1 的大小
 (这里的 yi 和 zi 作为索引，初始值都是 0), 取最小值放进序列，且索引值 + 1；
(3)直到存在arr[n]时为止；
'''

def dbl_linear(n):
    arr = [1]
    yi = 0
    zi = 0
    if n >= 1:
        for i in range(1,n+1):
            tmpRes = min(2 * arr[yi] + 1,3 * arr[zi] + 1)
            arr.append(tmpRes)
            if (arr[i] == 2 * arr[yi] + 1):
                yi += 1
            if (arr[i] == 3 * arr[zi] + 1):
                zi += 1
        return arr[i]
    else:
        i = 0
        return arr[i]