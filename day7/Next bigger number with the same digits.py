# -*- coding:utf-8 -*-

# 按rightSize来分割digits数组，不合规格的话，则按rightSize+1来递归分割
def splitDigits(digits, rightSize):
    # print('digits',digits)
    if rightSize > len(digits):
        return []
    right = digits[-rightSize : ]
    # 判断right是否符合要求
    if right[0] < right[1]:
        return [digits[0:-rightSize], right]
    return splitDigits(digits, rightSize + 1)

def reSort(right):
    first = right[0]
    # print(first)
    rest = right[1:]
    rest.sort()
    # print('rest',rest)
    # 找一个更大数字的索引
    for element in rest:
        if element > first:
            idx = rest.index(element)
            break
    res = []
    p = rest[idx]
    rest[idx] = first
    res.append(p)
    res.extend(rest)
    return res

# 将处理好的列表化的数字转化为整型
def getListNum(lst):
    lst = lst[::-1]
    sum = 0
    for i in range(len(lst)):
        sum += lst[i] * pow(10,i)
    return sum

# 接近原整数更大的数字
def next_bigger(n):
    # 通过splitDigits分割出left和right两部分
    arr = [int(i) for i in list(str(n))]
    res = splitDigits(arr,2)
    if len(res) > 1:
        left, right = res
        # print(left,right)
        right = reSort(right)
        left.extend(right)
        return getListNum(left)
    else:
        return -1
