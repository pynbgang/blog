---
layout: post
title: "a b problem"
published: true
created:  2020 Jan 19 04:21:15 PM
tags: [bit, python, lintcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [a-b-problem](https://www.lintcode.com/problem/a-b-problem/?_from=ladder&&fromId=99)

    1. A + B Problem

    Write a function that add two numbers A and B.

    Example
    Example 1:

    Input:  a = 1, b = 2
    Output: 3	
    Explanation: return the result of a + b.
    Example 2:

    Input:  a = -1, b = 1
    Output: 0	
    Explanation: return the result of a + b.
    Challenge
    Of course you can just return a + b to get accepted. But Can you challenge not do it like that?(You should not use + or any arithmetic operators.)

    Clarification
    Are a and b both 32-bit integers?

    Yes.
    Can I use bit operation?

    Sure you can.
    Notice
    There is no need to read data from standard input stream. Both parameters are given in function aplusb, your job is to calculate the sum and return it.
    Students in the basic class of the algorithm only need to use the arithmetic operator ‘+’ to complete the problem, without considering the requirements of the bit operation.

## solution1 (w/o recursion)

```python
class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        #return a+b
        #return sum([a,b])
        #return (a^b)+((a&b)<<1)
        #return sum([a^b, ((a&b)<<1)])

        #without recursion
        while b:
            a, b = (a ^ b), (a & b) << 1
        return a
```

### tips: bit operation to implement `add`

the fomula:

    addition (w/  carry) = addition w/o carry + carry
    addition (w/o carry) =  a ^ b
    carry                = (a & b) << 1

so:

    a+b = a ^ b + (a & b) << 1
          -----   ------------
          a1    + b1

        = a1 ^ b1 + (a1 & b1) << 1
          -------   --------------
            a2    +     b2

        = a2 ^ b2 + (a2 & b2) << 1

        = ...

    repeat until bn is 0, so result is an.

tips:

* addition w/o carry: 
    * 1+1->0, 0+0->0, 1+0,0+1->1 => 
    * same->0,diff->1 => 
    * this is `^` (异或) operation: `a^b`
* carry: 
    * only 1+1-> carry => 
    * same as & operation, 
    * and need shift, => 
    * this is `&` and `<<1` operation: `(a&b)<<1`
* addition is the sum of above 2 =>
* this is recursion (use a `sum` to implement a `sum`), or
* use loop (`while`) to avoid recursion

- https://stackoverflow.com/questions/30696484/a-b-without-arithmetic-operators-python-vs-c

### step through

```python
a,b=9,3
bin(a)              #1001
bin(b)              #0011
a,b=a^b,(a&b)<<1    #1010 , 0001<<1 (0010)
bin(a)              #1010
bin(b)              #0010
a,b=a^b,(a&b)<<1    #1000 , 0010<<1 (0100)
bin(a)              #1000
bin(b)              #0100
a,b=a^b,(a&b)<<1    #1100 , 0000<<1 (0000)
bin(a)              #1100
bin(b)              #0000
stop since b is 0, return a as sum: 1100 (12)
```
<!--
TODO: read about 补码
-->

### lintcode error

    Time Limit Exceeded
    Powered by LintCode FlashJudge
    50%
    50% test cases passedTotal runtime 1120 ms
    Input
    100
    -100
    Expected
    0
    Hint
    Your code ran too much time than we expected. Check your time complexity. Time limit exceeded usually caused by infinite loop if your time complexity is the best.

## solution2 (recursion)

```python
class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        # with recursion
        if b == 0:
            return a
        return self.aplusb(a^b, ((a&b)<<1))
```

### lintcode error

    Memory Limit Exceeded
    Powered by LintCode FlashJudge
    50%
    50% test cases passedTotal runtime 111 ms
    Input
    100
    -100
    Expected
    0
    Hint
    Your code cost too much memory than we expected. Check your space complexity. Memory limit exceeded usually caused by you create a 2D-array which is unnecessary.

## solution3

```python
class Solution:
    def aplusb(self, a, b):
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK    = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
```
