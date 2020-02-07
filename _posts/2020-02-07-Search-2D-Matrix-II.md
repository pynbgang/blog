---
layout: post
title: "Search a 2D Matrix II"
published: true
created:  2020 Feb 07 01:57:42 PM
tags: [python, medium, matrix,binary search]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# Search a 2D Matrix II

https://www.lintcode.com/problem/search-a-2d-matrix-ii/description?_from=ladder&&fromId=137
## brute force
within two for
```python
class Solution:
   for ....
    for ...
      count+
```
## within binary search 

```python
class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        if not matrix:
            return 0
        count=0
        for i in matrix:
            if i and i[0]<=target and i[-1]>=target and self.helper(i,target):
                count+=1
        
        return count
    
    def helper(self,list1, target):
        if not list1:
            return False
        if list1[0]==target or  list1[-1]==target:
            return True
        l,r=0,len(list1)-1
        while (l<r-1):
            m=l+(r-l)/2
            if list1[m]==target:
                return True
            if list1[m]<target:
                l=m
            else:
                r=m
        if list1[l]==target or list1[r]==target:
            return True
        return False
```
