#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:     #brute force
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        if len(prices) == 1: return 0
        max1 = max([max(prices[i+1:]) - prices[i] for i in range(len(prices)-1)] or [0])
        return max1 if max1 > 0 else 0

class Solution:     #half baked
    def maxProfit(self, prices: List[int]) -> int:
        d = {v: i for i, v in enumerate(prices)}
        prices_s, len1 = sorted(prices), len(prices)
        p, q = 0, len1
        while p < q:
            if d[prices_s[p]] < d[prices_s[q]]:
                return prices_s[q] - prices_s[p]
            else:
                p += 1
                if d[prices_s[p+1]] < d[prices_s[q]] and d[prices_s[p]] < d[prices_s[q+1]]:
                    return max(prices_s[q] - prices_s[p+1], prices_s[q-1] - prices_s[p])

class Solution:     #lmv
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

"""
[7,1,5,3,6,4]
max_profit = 0; min_price = inf
7:
    min_price = min(min_price, price) = 7
    profit = price - min_price = 7-7 = 0
    max_profit = max(max_profit, profit) = 0
1:
    min_price = 1
    profit = 1 - 1 = 0
    max_profit = 0
5:
    min_price = 1
    profit = 5-1 = 4
    max_profit = 4
3:
    min_price = 1
    profit = 3-1 = 2
    max_profit = 4
6:
    min_price = 1
    profit = 6-1 = 5
    max_profit = 5
4:
    min_price = 1
    profit = 4-1 = 3
    max_profit = 5
"""
# @lc code=end
