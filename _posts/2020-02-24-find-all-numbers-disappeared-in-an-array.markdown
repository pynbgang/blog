---
layout: post
title: "find-all-numbers-disappeared-in-an-array"
published: true
created:  2020 Feb 24 10:07:30 AM
tags: [easy, list, python, leetcode, brute force]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [find-all-numbers-disappeared-in-an-array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/)

|| * algorithms
|| * Easy (54.99%)
|| * Likes:    2281
|| * Dislikes: 207
|| * Total Accepted:    211.5K
|| * Total Submissions: 383.8K
|| * Testcase Example:  '[4,3,2,7,8,2,3,1]'
|| * Source Code:       448.find-all-numbers-disappeared-in-an-array.py
|| 
|| Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
|| 
|| Find all the elements of [1, n] inclusive that do not appear in this array.
|| 
|| Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
|| 
|| Example:
|| 
|| Input:
|| [4,3,2,7,8,2,3,1]
|| 
|| Output:
|| [5,6]

# ping

## plain brute force: timeout

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(1, max(len(nums), max(nums or [0]))+1):
            if i not in nums:
                res.append(i)
        return res
```

## passed

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        len1, nums = max(len(nums), max(nums or [0])), sorted(list(set(nums)))
        nums.insert(0, 0)
        nums.append(len1+1)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                res.extend(range(nums[i]+1, nums[i+1]))
        return res
```

# lmv

    """
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/313703

    * Lang:    python3
    * Author:  ndave
    * Votes:   14
    """

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0: nums[a] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
```
