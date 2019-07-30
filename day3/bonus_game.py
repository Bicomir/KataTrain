# -*- coding:utf-8 -*-

'''
未做出来，实际答案待再思考。
'''

def calc(cards):
    length = len(cards)
    sum = 0
    for i in range(length):
        n = i + 1
        print('n',n)
        print('cards[i]',cards[i])
        sum += cards[i] * pow(2,n)
    if sum > 50:
        return 50
    return sum

if __name__ == "__main__":
    # print(calc([1,2,5]))
    # print(calc([1]))
    # print(calc([1, 5, 2]))
    # print(calc([5, 1, 2]))
    # print(calc([5, 2, 1]))


    # print(calc([1,1]))
    print(calc([1,2,1]))
    # print(calc([4, 10, 2, 3, 1, 3, 1, 6, 9]))