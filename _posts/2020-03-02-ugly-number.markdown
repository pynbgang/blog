---
layout: post
title: "ugly number ii"
published: true
created:  2020 Mar 02 02:27:07 PM
tags: [python, leetcode, medium, number, math, prime]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[264] Ugly Number II](https://leetcode.com/problems/ugly-number-ii/description/)

    || * algorithms
    || * Medium (38.45%)
    || * Likes:    1350
    || * Dislikes: 81
    || * Total Accepted:    130.8K
    || * Total Submissions: 338K
    || * Testcase Example:  '10'
    || * Source Code:       264.ugly-number-ii.py
    || 
    || Write a program to find the n-th ugly number.
    || 
    || Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
    || 
    || Example:
    || 
    || 
    || Input: n = 10
    || Output: 12
    || Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
    || 
    || Note:  
    || 
    || 
    || 	1 is typically treated as an ugly number.
    || 	n does not exceed 1690.

## ping: brute force: time exceeded

```python
class Solution:  #ping: use #263 and brute force, time exceeded
    def nthUglyNumber(self, n: int) -> int:
        i, num, num1 = 0, 1, 1
        while i < n:
            num = num1
            for p in 2,3,5:
                while num % p == 0 < num:
                    num //= p
            if num == 1:
                i += 1
            num1 += 1
        return num1-1
```

## lmv

```python
class Solution:  #lmv
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
```

## illustration

* init only 1 ugly `nums`: [1]
* muliply 2, 3, 5, get new ugly num 2,3,5, min(2,3,5)=2, so `x2` win. `nums`:[1,2]
* since 1 `x2` win, and its generated new num has been added, when we check who
  is the next ugly number we don't need to check 1 `x2` any more. move the index
  that needs `x2` to the next num 2.
* in contrast, 1 `x3`, `x5` has not win yet, they still has their chance to be
  the "smallest" on next comparison. so when "checking who is the next
  ugly number" we still need to check them.
* repeat this process. each time a `x N` (N=2,3,5) win as smallest, move it to
  the next num, otherwise don't change.

illustrated below:

    init:[1]
        x2                              2 min
        x3                              3
        x5                              5

        1   [2]
        x3                              3 min
        x5                              5
            x2                          4

        1   2   [ 3 ]
        x5                              5
            x2                          4 min
            x3                          6

        1   2   3   [ 4 ]
        x5                              5 min
                x2                      6
            x3                          6


        1   2   3   4   [ 5 ]
            x5                          10
                x2                      6 min
            x3                          6 min

        1   2   3   4   5   [ 6 ]
            x5                          10
                    x2                  10
                x3                      9 min

        1   2   3   4   5   6   [ 9 ]

## good reference

* https://www.geeksforgeeks.org/ugly-numbers/
