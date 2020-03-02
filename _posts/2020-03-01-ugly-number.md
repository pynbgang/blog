---
layout: post
title: "Ugly Number"
published: true
created:  2020 Mar 01 02:45:47 PM
tags: [python, math, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Ugly Number](https://leetcode.com/problems/ugly-number/submissions/)

||Write a program to check whether a given number is an ugly number.                                                                         
||                                                                                                                                          
||Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
||Output: 1->2->3->4->5                                                                                                                                                                                                                                                                                                                                                                                     
||Example 1:                                                                                                                                                        
||                                                                                                                                                                  
||Input: [8,1,5,2,6]                                                                                                                                                
||Output: 11                                                                                                                                                        
||                                                                                                                                                                                                                                                                                                                                                                                                                                          

## Owen - fast/slow pointers 

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




