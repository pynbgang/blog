---
layout: post
title: "Ugly Number"
published: true
created:  2020 Mar 01 02:45:47 PM
tags: [python, math, leetcode, easy, set, precedence, media]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Ugly Number](https://leetcode.com/problems/ugly-number/submissions/)

    || * algorithms
    || * Easy (41.16%)
    || * Likes:    355
    || * Dislikes: 548
    || * Total Accepted:    186.2K
    || * Total Submissions: 451.8K
    || * Testcase Example:  '6'
    || * Source Code:       263.ugly-number.py
    || 
    || Write a program to check whether a given number is an ugly number.
    || 
    || Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
    || 
    || Example 1:
    || Input: 6
    || Output: true
    || Explanation: 6 = 2 × 3
    || 
    || Example 2:
    || 
    || Input: 8
    || Output: true
    || Explanation: 8 = 2 × 2 × 2
    || 
    || Example 3:
    || Input: 14
    || Output: false 
    || Explanation: 14 is not ugly since it includes another prime factor 7.
    || 
    || Note:
    || 
    || 	1 is typically treated as an ugly number.
    || 	Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].

## Owen - recursive

```python
class Solution(object):
    def isUgly(self, num):
        if num==0:return False
        if num==1:return True
        k=self.helper(num)
        if k[0]:return self.isUgly(num/k[1])
        return False

    def helper(self,num):
        flag=False
        for i in [2,3,5]:
            if num%i==0:
                return (True,i)
        return (False,0)
```

## ping and lmv

```python
class Solution:     #ping: prime issue
    def isUgly(self, num: int) -> bool:
        num1, i, set1 = num, 2, set()
        while i**2 <= num:
            if not num % i:
                set1.add(i)
                num //= i
            else:
                i += 1
        set1.add(num)   #don't forget the last factor
        return True if set1.issubset({2,3,5}) or num1==1 else False

        """
        ||   ✔ Accepted
        ||   ✔ 1012/1012 cases passed (604 ms)
        ||   ✔ Your runtime beats 5.44 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
        """

class Solution:     #lmv
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            #while num % p == 0 < num:      #zb way
            while not num % p and num>0:    #normal way
                num //= p
        return num == 1

        """
        ||   ✔ Accepted
        ||   ✔ 1012/1012 cases passed (28 ms)
        ||   ✔ Your runtime beats 76.09 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
        """
```

## tip


regarding `num % p == 0 < num`:
it is NOT: `(num % p) == (0 < num)`
instead it is: `(num % p) and (0 < num)`

<iframe width="560" height="315" src="https://www.youtube.com/embed/Wz4WWds2HjQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
