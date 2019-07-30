#-*- coding:utf-8 -*-

from functools import reduce


def fizzBuzz1(n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        outList = []
        for i in range(1,n+1):
            if i % 15 == 0:
                outList.append("FizzBuzz")
            elif i % 5 == 0:
                outList.append("Buzz")
            elif i % 3 == 0:
                outList.append("Fizz")
            else:
                outList.append(str(i))
        return outList


for i in range(1,100):
    print(fizzBuzz1(i))




'''
# fizzbuzz++
def fizzbuzz_plusplus(nums, words):
    res = []
    # flag3 = False
    # flag5 = False
    ln = reduce(lambda x,y : x*y, nums)
    length = len(nums)

    data = {}
    for i in range(length):
        data[nums[i]] = words[i]

    item = 1
    while True:
        # for i in range(length):
        #     if item % nums[i] == 0 and item % ln != 0:
        #         res.append(words[i])
        #     elif item % nums[i] != 0:
        #         res.append(item)
        #     elif item % ln == 0:
        #         break

        print('item', item)
        if item % ln == 0:
            break
        item += 1

    return res
'''




