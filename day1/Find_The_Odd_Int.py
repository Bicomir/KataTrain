#-*- coding:utf-8 -*-
def find_it(seq):
    # 确定列表中的几个数字
    array_list = set(seq)
    # 遍历列表型数组，然后对每个元素进行计数
    for e in array_list:
        if seq.count(e) % 2 == 1:
            return e

