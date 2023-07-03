"""
2. Given two strings. The task is to find the length of the longest common substring.

Example 1:

Input: S1 = "ABCDGH", S2 = "ACDGHR"
Output: 4
Explanation: The longest common substring
is "CDGH" which has length 4.

"""

import functools
from typing import List


def get_longest_common_substring(s1: str, s2: str):
    c1 = {s1[i:j] for i in range(len(s1)) for j in range(i + 1, len(s1) + 1)}
    c2 = {s2[i:j] for i in range(len(s2)) for j in range(i + 1, len(s2) + 1)}

    common_sub_string = c1.intersection(c2)

    print(c1)
    print(c2)
    print(common_sub_string)

    longest_substring = functools.reduce(lambda a, b: a if len(a) > len(b) else b, common_sub_string)
    print(longest_substring)


"""
# 3. Best time to buy and sell stock

# You are given an array of prices where prices[i] is the price of given stock on an its day
# You want to maximise your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock
# Return maximum profit you can achieve from this transaction. 
# If you can't achieve any profit, return 0

# Input - prices =[7,1,5,3,6,4] output = 5
# Explanation - Buy on day 2(price=1) and sell on day 5(price=6)
# Profit = 6-1 = 5
"""


def best_time_to_buy_sell_stock(prices: List[int]) -> int:
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[i]:
                current_profit = prices[j] - prices[i]
                max_profit = max(max_profit, current_profit)

    print(max_profit)
    return max_profit


if __name__ == '__main__':
    # s1 = "ABCDGH"
    # s2 = "ACDGHR"
    # get_longest_common_substring(s1, s2)

    prices = [1,2,3,4,5,6,7]
    best_time_to_buy_sell_stock(prices)
