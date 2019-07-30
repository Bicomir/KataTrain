# -*- coding:utf-8 -*-

import math

def who_say_next(names,r):
    length = len(names)
    sum = length
    n = 1
    while(sum < r):
        n *= 2 # 分身数
        sum += length*n
    return names[math.ceil((r + length*n - sum)/n) - 1]


if __name__ == "__main__":
    # print("helo")
    # data = {0:"Sheldon", 1:"Leonard", 2:"Penny", 3:"Rajesh", 4:"Howard"}
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    print(who_say_next(names,1))
    print(who_say_next(names, 52))
    print(who_say_next(names, 7230702951))



