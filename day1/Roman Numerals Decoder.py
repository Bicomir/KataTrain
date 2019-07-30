#-*- coding:utf-8 -*-
def solution(roman):
  """complete the solution by transforming the roman numeral into an integer"""
  # 建立罗马数据字典
  data = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
  sum = 0
  length = len(roman)
  for i in range(length):
    tmp = data[roman[i]]
    if i+1 < length and data[roman[i+1]] > tmp:
        sum -= tmp
    else:
        sum += tmp
  return sum
