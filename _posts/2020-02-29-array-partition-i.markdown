---
layout: post
title: "array-partition-i"
published: true
created:  2020 Feb 29 02:29:37 PM
tags: [lintcode, python, easy, list, media, tanyonglin]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [array-partition-i](https://leetcode.com/problems/array-partition-i/description/)

    || * algorithms
    || * Easy (70.84%)
    || * Likes:    707
    || * Dislikes: 2208
    || * Total Accepted:    190.6K
    || * Total Submissions: 268.5K
    || * Testcase Example:  '[1,4,3,2]'
    || * Source Code:       561.array-partition-i.py
    || 
    || 
    || Given an array of 2n integers, your task is to group these integers into n
    pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of
    min(ai, bi) for all i from 1 to n as large as possible.
    || 
    || 
    || Example 1:
    || 
    || Input: [1,4,3,2]
    || 
    || Output: 4
    || Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
    || 
    || 
    || 
    || Note:
    || 
    || n is a positive integer, which is in the range of [1, 10000].
    || All the integers in the array will be in the range of [-10000, 10000].

## ping

```python
class Solution:     # ping
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))
```

## lmv
```python
class Solution:     #lmv: oneliner
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/ur8ZBoPez70" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


