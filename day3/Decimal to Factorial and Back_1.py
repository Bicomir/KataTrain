# -*- coding:utf-8 -*-
from math import factorial

def factpos(num,pos): #对要使用的数字，并找到位置
    return num*factorial(pos)

def _36ToDec(digit):
    wordsDict = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20,
        'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31,
        'W': 32, 'X': 33, 'Y': 34, 'Z': 35
    }
    return wordsDict[digit]

def decTo36(digit):
    wordsDict = {
         0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',
        10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K',
        21:'L', 22:'M', 23:'N', 24:'O', 25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V',
        32:'W', 33:'X', 34:'Y', 35:'Z'
    }
    return wordsDict[digit]

def dec2FactString(nb):
    digits, pos = '',1
    quotient, rem = divmod(nb, pos) # 返回商和余数的元组
    while quotient != 0:
        digits += str(decTo36(rem))
        pos += 1
        quotient,rem = divmod(quotient,pos)
    digits += str(decTo36(rem))
    digits = digits[::-1]
    return digits


# 将阶乘表达式转为36进制数
def factString2Dec(string):
    sum = 0
    digits = list(string)
    pos = [i for i in range(len(digits))]
    pos.reverse()
    for i,digit in enumerate(digits):
        sum += factpos(_36ToDec(digit), pos[i])
    return sum
