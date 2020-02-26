---
layout: post
title: "two-sum-ii-input-array-is-sorted"
published: true
created:  2020 Feb 26 02:45:47 PM
tags: [python, list, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [two-sum-ii-input-array-is-sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

||Write an algorithm to determine if a number is "happy".                                                                                                                                                                                                                                                                                                         
||                                                                                                                                                                                                                                                                                                                                                                
||A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
||                                                                                                                                                                                                                                                                                                                                                                
||Example:                                                                                                                                                                                                                                                                                                                                                        
||                                                                                                                                                                                                                                                                                                                                                                
||Input: 19                                                                                                                                                                                                                                                                                                                                                       
||Output: true                                                                                                                                                                                                                                                                                                                                                    
||Explanation:                                                                                                                                                                                                                                                                                                                                                    
||12 + 92 = 82                                                                                                                                                                                                                                                                                                                                                    
||82 + 22 = 68                                                                                                                                                                                                                                                                                                                                                    
||62 + 82 = 100                                                                                                                                                                                                                                                                                                                                                   
||12 + 02 + 02 = 1                                                                                                                                                                                                                                                                                                                                                

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


