---
layout: post
title: "remove element"
published: true
created:  2020 Feb 07 03:51:05 PM
tags: [python, easy, list, lintcode, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [remove-element (in place)](https://leetcode.com/problems/remove-element/description/)

[lintcode](https://www.lintcode.com/problem/remove-element)

|| Given an array nums and a value val, remove all instances of that value in-
|| place and return the new length.
|| Do not allocate extra space for another array, you must do this by modifying
|| the input array in-place with O(1) extra memory.
|| The order of elements can be changed. It doesn't matter what you leave beyond
|| the new length.
|| Example 1:
|| Given nums = [3,2,2,3], val = 3,
|| 
|| Your function should return length = 2, with the first two elements of nums
|| being 2.
|| 
|| It doesn't matter what you leave beyond the returned length.
|| Example 2:
|| Given nums = [0,1,2,2,3,0,4,2], val = 2,
|| 
|| Your function should return length = 5, with the first five elements of nums
|| containing 0, 1, 3, 0, and 4.
|| 
|| Note that the order of those five elements can be arbitrary.
|| 
|| It doesn't matter what values are set beyond the returned length.
|| Clarification:

# ping

```python
class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        i = 0
        while i <= len(A)-1:
            if A[i] == elem:
                A.remove(elem)
            else:
                i += 1
        return len(A)
```

# lmv

```python
class Solution:
    def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start
```
