---
layout: post
title: "[693] Binary Number with Alternating Bits"
published: true
created:  2020 Apr 13 12:16:56 PM
tags: [python, leetcode, easy, recursion]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[693] Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits//)

    || Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
    || 
   
   
   
   
   

## Owen: 
1 math

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        if n==0:return True
        if n%2!=0:
            temp=1
            while (temp<=n):
                if n==temp:return True
                temp=temp*4+1
            return False
        else:
            temp=2
            while(temp<=n):
                if n==temp:return True
                temp=temp*4+2
            return False
```
2 str trick

```python
class Solution(object):
    def hasAlternatingBits(self, n):
        str1=str(bin(n))
        if "00" in str1:return False
        if "11" in str1:return False
        return True
```

3 recursive
class Solution(object):
    def hasAlternatingBits(self, n):
        str1=str(bin(n))[2:]
        return self.helper(str1)

    def helper(self,str1):
        if str1=="0":return True
        if str1=="1":return True
        if str1[0]==str1[1]:return False
        else:return self.helper(str1[1:])
