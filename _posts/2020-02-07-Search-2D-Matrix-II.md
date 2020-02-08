---
layout: post
title: "Search a 2D Matrix II"
published: true
created:  2020 Feb 07 01:57:42 PM
tags: [python, medium, matrix, binary search, brute force, any]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [Search a 2D Matrix II](https://www.lintcode.com/problem/search-a-2d-matrix-ii/description?_from=ladder&&fromId=137)


|| https://leetcode.com/problems/search-a-2d-matrix-ii/description/
|| 
|| * algorithms
|| * Medium (42.29%)
|| * Likes:    2348
|| * Dislikes: 65
|| * Total Accepted:    258.2K
|| * Total Submissions: 610.4K
|| * Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'

|| Write an efficient algorithm that searches for a value in an m x n matrix. This
|| matrix has the following properties:
||     * Integers in each row are sorted in ascending from left to right.
||     * Integers in each column are sorted in ascending from top to bottom.
|| Example:
|| Consider the following matrix:
|| [
||   [1,   4,  7, 11, 15],
||   [2,   5,  8, 12, 19],
||   [3,   6,  9, 16, 22],
||   [10, 13, 14, 17, 24],
||   [18, 21, 23, 26, 30]
|| ]
|| Given target = 5, return true.
|| Given target = 20, return false.

## owen

### brute force

with two for

```python
class Solution:
   for ....
    for ...
      count+
```

### binary search

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
||   ✔ Accepted
||   ✔ 129/129 cases passed (28 ms)
||   ✔ Your runtime beats 94.19 % of python3 submissions
||   ✔ Your memory usage beats 92.59 % of python3 submissions (17.4 MB)
"""
```

## ping

### brute force: most intuitive

```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for l in matrix:
            if target in l:
                return True
        return False

"""
||   ✔ Accepted
||   ✔ 129/129 cases passed (24 ms)
||   ✔ Your runtime beats 98.41 % of python3 submissions
||   ✔ Your memory usage beats 88.89 % of python3 submissions (17.5 MB)
"""
```

### one liner (any) (lmv)

```python
class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)

"""
||   ✔ Accepted
||   ✔ 129/129 cases passed (32 ms)
||   ✔ Your runtime beats 82.37 % of python3 submissions
||   ✔ Your memory usage beats 92.59 % of python3 submissions (17.4 MB)
"""
```

### how generator expression works with BIF

    [ins] In [8]: any([1 in row for row in [[1,2],[2,3]]])           
    Out[8]: True

    [ins] In [9]: any((1 in row for row in [[1,2],[2,3]]))          
    Out[9]: True

    [ins] In [7]: any(1 in row for row in [[1,2],[2,3]])             
    Out[7]: True

why the 3rd one works? 
shouldn't it be within [] - list comprehension?

        return any([target in row for row in matrix])

or () - list generator:

        return any((target in row for row in matrix))


https://stackoverflow.com/questions/16505456/how-exactly-does-the-python-any-function-work/16505590
https://www.python.org/dev/peps/pep-0289/

looks like it is just the design, so no need:

    func( (generator expression) )

just:

    func( generator expression )

### use "ascending" (lmv)

```python
class Solution:
    def searchMatrix(self, matrix, target):
        j = -1
        for row in matrix:
            if row:
                while j + len(row) and row[j] > target:
                    j -= 1
                if row[j] == target:
                    return True
        return False

"""
||   ✔ Accepted
||   ✔ 129/129 cases passed (40 ms)
||   ✔ Your runtime beats 37.36 % of python3 submissions
||   ✔ Your memory usage beats 74.07 % of python3 submissions (17.5 MB)
"""
```
