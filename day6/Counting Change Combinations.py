# -*- coding:utf-8 -*-
def count_change(money, coins):
    # your implementation here
    if money < 0 or len(coins) == 0:
        return 0
    elif money > 0:
        return count_change(money - coins[0], coins) + count_change(money, coins[1:])
    else:
        return 1
