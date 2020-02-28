---
layout: post
title: "Happy-Number"
published: true
created:  2020 Feb 26 02:45:47 PM
tags: [python, list, leetcode, easy, set]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Happy Number](https://leetcode.com/problems/happy-number/)

||Write an algorithm to determine if a number is "happy".
||
||A happy number is a number defined by the following process: Starting with
any positive integer, replace the number by the sum of the squares of its
digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for
which this process ends in 1 are happy numbers.
||
||Example:
||
||Input: 19
||Output: true
||Explanation:

|| 1^2 + 9^2 = 82
|| 8^2 + 2^2 = 68
|| 6^2 + 8^2 = 100
|| 1^2 + 0^2 + 0^2 = 1

## Owen - while

```python
class Solution(object):

    def isHappy(self, n):
        str1=str(n)
        set1=set([])
        while (str1):
            list1=[int(i)**2 for i in str1]
            temp=sum(list1)
            if temp in set1:
                break
            set1.add(temp)
            str1=str(temp)
        return 1 in set1
```

## Owen - recursive

```python
class Solution(object):

    def isHappy(self, n):
        self.set1=set([])
        str1=str(n)
        self.helper(str1)
        return 1 in self.set1

    def helper(self,str1):
        temp=0
        for i in str1:
            temp+=int(i)**2
        if temp in self.set1:
            return
        self.set1.add(temp)
        print self.set1
        self.helper(str(temp))

```


## ping - while

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()
        while True:
            n = sum(int(i) ** 2 for i in str(n))
            if n is 1:
                return True
            if n in set1:
                return False
            set1.add(n)

    """
    ||   ✔ Accepted
    ||   ✔ 401/401 cases passed (24 ms)
    ||   ✔ Your runtime beats 96.99 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
    """
```
