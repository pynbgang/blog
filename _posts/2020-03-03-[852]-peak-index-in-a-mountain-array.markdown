---
layout: post
title: "[852] Peak Index in a Mountain Array"
published: true
created:  2020 Mar 03 01:32:56 AM
tags: [leetcode, python, easy, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[852] Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/)

    || * algorithms
    || * Easy (70.78%)
    || * Likes:    473
    || * Dislikes: 978
    || * Total Accepted:    129.3K
    || * Total Submissions: 182.4K
    || * Testcase Example:  '[0,1,0]'
    || * Source Code:       852.peak-index-in-a-mountain-array.py
    || 
    || Let's call an array A a mountain if the following properties hold:
    || 
    || 	A.length >= 3
    || 	There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    || 
    || Given an array that is definitely a mountain, return any i such
    that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
    || 
    || Example 1:
    || Input: [0,1,0]
    || Output: 1
    || 
    || Example 2:
    || Input: [0,2,1,0]
    || Output: 1
    || 
    || Note:
    || 
    || 	3 <= A.length <= 10000
    || 	0 <= A[i] <= 10^6
    || 	A is a mountain, as defined above.

## ping: just find the index of the max

```python
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))

        """
        ||   ✔ Accepted
        ||   ✔ 32/32 cases passed (64 ms)
        ||   ✔ Your runtime beats 99.84 % of python3 submissions
        ||   ✔ Your memory usage beats 96.97 % of python3 submissions (14 MB)
        """
```
