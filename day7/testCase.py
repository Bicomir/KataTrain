#-*- coding:utf-8 -*-

class TestCase(object):
    def __init__(self):
        pass

    def fizzbuzz2(self,n):
        if n < 1:
            return []
        outList = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                outList.append("FizzBuzz")
            elif i % 5 == 0:
                outList.append("Buzz")
            elif i % 3 == 0:
                outList.append("Fizz")
            else:
                outList.append(str(i))
        return outList

    def describe(self, str):
        return str

    def it(self, title):
        return title

    def assert_equals(self,funcResults,result):
        if(funcResults == result):
            return "pass"
        else:
            return "fail"





Test = TestCase()
Test.describe("FizzBuzz:")
Test.it("should work for regular fizzbuzz")
print(Test.assert_equals(Test.fizzbuzz2(3),['1', '2', 'Fizz']))
print(Test.assert_equals(Test.fizzbuzz2(4),['1', '2', 'Fizz', '4']))
print(Test.assert_equals(Test.fizzbuzz2(5),['1', '2', 'Fizz', '4', 'Buzz']))


Test.it("should work for the example")
