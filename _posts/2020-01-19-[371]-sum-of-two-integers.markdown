---
layout: post
title: "[371] Sum of Two Integers"
published: true
created:  2020 Jan 19 04:21:15 PM
tags: [bit, python, lintcode, leetcode, easy, binary, bit, pending]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[371] Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/description/)

    || * algorithms
    || * Easy (50.68%)
    || * Likes:    1323
    || * Dislikes: 2320
    || * Total Accepted:    194.5K
    || * Total Submissions: 383.9K
    || * Testcase Example:  '1\n2'
    || * Source Code:       371.sum-of-two-integers.py
    || 
    || Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
    || 
    || Example 1:
    || Input: a = 1, b = 2
    || Output: 3
    || 
    || Example 2:
    || 
    || Input: a = -2, b = 3
    || Output: 1
    || 
    || [Finished in 5 seconds]

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
    Of course you can just return a + b to get accepted. But Can you challenge
    not do it like that?(You should not use + or any arithmetic operators.)

    Clarification
    Are a and b both 32-bit integers?  Yes.
    Can I use bit operation?  Sure you can.

    Notice
    There is no need to read data from standard input stream. Both parameters
    are given in function aplusb, your job is to calculate the sum and return
    it.  Students in the basic class of the algorithm only need to use the
    arithmetic operator ‘+’ to complete the problem, without considering the
    requirements of the bit operation.

## solution1 (w/o recursion, works for positive only)

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

## solution2 (recursion, works for positive only)

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

## solution3 (works for negative also)

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

## lmv

https://leetcode.com/problems/sum-of-two-integers/discuss/489210

* Lang:    python3
* Author:  IKMalik
* Votes:   30

In Python unlike other languages the range of bits for representing a value is
not 32, its much much larger than that. This is great when dealing with non
negative integers, however this becomes a big issue when dealing with negative
numbers ( two\'s compliment) 

Why ?

Lets have a look, say we are adding -2 and 3, which = 1

In Python this would be ( showing only 3 bits for clarity ) 

    1  1 0 +
    0  1 1 

Using binary addition you would get

    0 0 1 

That seems fine but what happended to the extra carry bit ? ( 1 0 0 0 ), if you
were doing this by hand you would simply ignore it, but Python does not,
instead it continues \'adding\' that bit and continuing the sum. 

    1 1 1 1 1 1 0 +
    0 0 0 0 0 1 1 
    0 0 0 1 0 0 0 + ( carry bit ) 

so this actually continues on forever unless ... 

Mask ! 

The logic behind a mask is really simple, you should know that x & 1 = x right,
so using that simple principle,

if we create a series of 4 1\'s and & them to any larger size series, we will
get just that part of the series we want, so 

    1 1 1 1 1 0 0 1
    0 0 0 0 1 1 1 1 &

    0 0 0 0 1 0 0 1 ( Important to note that using a mask removes the two\'s compliment) 

For this question leetcode uses 32 bits, so you just need to create a 32 bit
mask of 1\'s , the quickest way is to use hexadecimal and 0xffffffff, you can
write the binary form if you prefer it will work the same. 

Here is my code ,

```
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        
        # works both as while loop and single value check 
        while (b & mask) > 0:
            
            carry = ( a & b ) << 1
            a = (a ^ b) 
            b = carry
        
        # handles overflow
        return (a & mask) if b > 0 else a
```
Note the final check, if b = 0 that means the carry bit \'finished\', but when
there is a negative number ( like -1), the carry bit will continue until it
exceeds our 32 bit mask ( to end while loop ) it wont be 0 so in that case we
use the mask. 


## tips

### bit operation to implement `add`

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

### nagative 

https://blog.csdn.net/qq506124204/article/details/7521996

* 运算用补码!!
* 正数反码：与原码相同
* 负数反码：符号位为“1”，数值位按位 取反。
* 正数补码：与原码相同
* 负数补码：求反加一

        1: 0000 0001
        反 0000 0001
        补 0000 0001       #<---
            
        -1: 1000 0001
        反 1111 1110 +1
        补 1111 1111       #<---

so: 1 ^ -1 :

        0000 0001       1
     ^  1111 1111      -1
     =====================
     =  1111 1110 (补)
        1000 0001 (反) + 1
        1000 0010 (原)= -2


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

### leetcode error

    || - Waiting for judge result
    ||   ✘ Time Limit Exceeded
    ||   ✘ 8/13 cases passed (N/A)
    ||   ✘ Testcase: -1
    || 1
    ||   ✘ Answer: 
    ||   ✘ Expected Answer: 
    ||   ✘ Stdout: 
    || [Finished in 9 seconds]

## pending

negative number problem

