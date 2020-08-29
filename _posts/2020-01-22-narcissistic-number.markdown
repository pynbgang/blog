---
layout: post
title: "narcissistic-number"
published: true
created:  2020 Jan 22 08:35:58 PM
tags: [python, lintcode, easy, math]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [narcissistic-number](https://www.lintcode.com/problem/narcissistic-number/description?_from=ladder&&fromId=99)

    Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits. See wiki
    For example the 3-digit decimal number 153 is a narcissistic number because 153 = 13 + 53 + 33.

    And the 4-digit decimal number 1634 is a narcissistic number because 1634 = 14 + 64 + 34 + 44.

    Given n, return all narcissistic numbers with n digits.

    Example
    Example 1:

    Input: 1
    Output: [0,1,2,3,4,5,6,7,8,9]
    Example 2:

    Input: 2
    Output: []
    Explanation: There is no Narcissistic Number with 2 digits.
    Notice
    You may assume n is smaller than 8.

## ping

```python
class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # write your code here
        result=[]
        if n==1:
            return list(range(10))
        for number in range( int( '1' + '0'*(n-1) ), int('9'*n)+1):
            sum=0
            for i in str(number):
                sum += int(i) ** n
            if sum==number:
                result.append(number)
        return result
```

```python
#(Sat 29 Aug 2020 02:16:59 PM DST) 
class Solution:
    def getNarcissisticNumbers(self, n):
        #1      0-9            10**0-10**1-1
        #2      10-99          10**1-10**2-1
        #3      100-990        10**2-10**3-1
        #                      10**(n-1) - 10**n-1
        if not n: return []
        res = []
        for i in range(0 if n==1 else 10**(n-1), 10**n):
            if i==sum(int(c)**n for c in str(i)):
                res.append(i)
        return res
#(Sat 29 Aug 2020 02:28:10 PM DST) 

S=Solution()
S.getNarcissisticNumbers(2)

```


## tips

looking at the ranges per numbers:

    n       start           end
    ------------------------------
    1       0       -       9
    2       10      -       99
    3       100     -       999

this can be modeled as:

    range( int( '1'*(n>1) + '0'*(n-1) or  '0'), int('9'*n)+1 ):

where:

    range( int( '1'*(n>1) + '0'*(n-1) or  '0'), int('9'*n)+1 ):
           ---------------------------    ----
            get '' when n=1,              then get a '0'
            only when >1 digits get a '1' and append (n-1) '0's...


so another solution w/o `if n==1`:

```python
class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # write your code here

        result=[]
        for number in range( int('1'*(n>1) + '0'*(n-1) or '0'), int('9'*n)+1):
            sum=0
            for i in str(number):
                sum += pow(int(i), n)
            if sum==number:
                result.append(number)
        return result
```

it looks cool, but not so readable. this is better:

    if n==1:
        return list(range(10))
    for number in range( int('1' + '0'*(n-1) ), int('9'*n)+1):

or simply:

    if n==1:
        return list(range(10))
    for number in range(10 ** (n-1),  10 ** n - 1):


## wangmazi (数字拆分 先MOD 然后除10取整)

```python
class Solution:
    """
    @param n: The number of digits.
    @return: All narcissistic numbers with n digits.
    """
    def getNarcissisticNumbers(self, n):
        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if n == 6:
            return [548834]

        result = []
        for i in range(10 ** (n-1), 10 ** n):
            j, s = i, 0
            while j != 0:
                s += (j % 10) ** n;
                j = j / 10
            if s == i:
                result.append(i)
        return result
```
