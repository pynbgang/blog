---
layout: post
title: "[343] Integer Break"
published: true
created:  2020 Sep 05 01:27:58 PM
tags: [python, leetcode, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[343] Integer Break](https://leetcode.com/problems/integer-break/description/)

    || * algorithms
    || * Medium (49.22%)
    || * Likes:    1159
    || * Dislikes: 233
    || * Total Accepted:    113.1K
    || * Total Submissions: 223.8K
    || * Testcase Example:  '2'
    || * Source Code:       343.integer-break.py
    || 
    || Given a positive integer n, break it into the sum of at least two
    positive integers and maximize the product of those integers. Return the
    maximum product you can get.
    || 
    || Example 1:
    || 
    || Input: 2
    || Output: 1
    || Explanation: 2 = 1 + 1, 1 × 1 = 1.
    || 
    || Example 2:
    || 
    || Input: 10
    || Output: 36
    || Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
    || 
    || Note: You may assume that n is not less than 2 and not larger than 58.

## jj

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        res = [1] * (n + 1)
        for i in range(3, n + 1):
            res[i] = max(max(j, res[j]) * max(i - j, res[i - j]) for j in range(2, i // 2 + 2))
        return res[-1]
```

## lmv

```python
class Solution:     #internet
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        result = 1
        while n > 4:
            n -= 3
            result *= 3
        return n * result
```

idea: it seems like only 3 is the number that when splitted into 2 number
(1+2), the product is less than self.

    6=3+3, 3*3>6
    5=2+3, 2*3>5
    4=2+2, 2*2=4
    but
    3=2+1, 2*1<3


