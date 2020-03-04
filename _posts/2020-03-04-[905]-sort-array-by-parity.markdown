---
layout: post
title: "[905] Sort Array By Parity"
published: true
created:  2020 Mar 04 01:48:42 AM
tags: [python, leetcode, easy, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[905] Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/description/)

    || * algorithms
    || * Easy (73.53%)
    || * Likes:    740
    || * Dislikes: 67
    || * Total Accepted:    161.3K
    || * Total Submissions: 219K
    || * Testcase Example:  '[3,1,2,4]'
    || * Source Code:       905.sort-array-by-parity.py
    || 
    || Given an array A of non-negative integers, return an array consisting of
    all the even elements of A, followed by all the odd elements of A.
    || You may return any answer array that satisfies this condition.
    || 
    || Example 1:
    || Input: [3,1,2,4]
    || Output: [2,4,3,1]
    || The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
    || 
    || Note:
    || 
    || 	1 <= A.length <= 5000
    || 	0 <= A[i] <= 5000

## ping
```python
class Solution:     #ping
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [i for i in A if not i % 2] + [i for i in A if i % 2]
```

## lmv
```python
class Solution:     #lmv
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key = lambda x : x % 2)
```
