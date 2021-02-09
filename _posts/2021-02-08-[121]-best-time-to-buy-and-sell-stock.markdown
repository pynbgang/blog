---
layout: post
title: "[121] Best Time to Buy and Sell Stock"
published: true
created:  2021 Feb 08 17:03:17
tags: [python, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[121] Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

    || * algorithms
    || * Easy (51.17%)
    || * Likes:    7538
    || * Dislikes: 337
    || * Total Accepted:    1.2M
    || * Total Submissions: 2.3M
    || * Testcase Example:  '[7,1,5,3,6,4]'
    || * Source Code:       121.best-time-to-buy-and-sell-stock.py
    || 
    || You are given an array prices where prices[i] is the price of a given
    stock on the i^th day.
    || 
    || You want to maximize your profit by choosing a single day to buy one
    stock and choosing a different day in the future to sell that stock.
    || 
    || Return the maximum profit you can achieve from this transaction. If you
    cannot achieve any profit, return 0.
    || 
    ||  
    || Example 1:
    || 
    || Input: prices = [7,1,5,3,6,4]
    || Output: 5
    || Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    || Note that buying on day 2 and selling on day 1 is not allowed because
    you must buy before you sell.
    || 
    || 
    || Example 2:
    || 
    || Input: prices = [7,6,4,3,1]
    || Output: 0
    || Explanation: In this case, no transactions are done and the max profit = 0.
    ||  
    || Constraints:
    || 
    || 	1 <= prices.length <= 10^5
    || 	0 <= prices[i] <= 10^4

# solution

```python
class Solution:     #lmv
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit
```

# tips

* python max num: `float('inf')`. bigger (and simpler) than `sys.maxsize` (biggest int)
