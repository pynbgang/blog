---
layout: post
title: "[961] N-Repeated Element in Size 2N Array"
published: true
created:  2020 Mar 05 09:46:30 PM
tags: [python, leetcode, list, easy, Counter]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[961] N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/)

    || * algorithms
    || * Easy (72.91%)
    || * Likes:    347
    || * Dislikes: 202
    || * Total Accepted:    98.2K
    || * Total Submissions: 134.5K
    || * Testcase Example:  '[1,2,3,3]'
    || * Source Code:       961.n-repeated-element-in-size-2n-array.py
    || 
    || In an array A of size 2N, there are N+1 unique elements, and exactly one
    of these elements is repeated N times.
    || 
    || Return the element repeated N times.
    || 
    || Example 1:
    || Input: [1,2,3,3]
    || Output: 3
    || 
    || Example 2:
    || Input: [2,1,2,5,3,2]
    || Output: 2
    || 
    || Example 3:
    || Input: [5,1,5,2,5,3,5,4]
    || Output: 5
    || 
    || Note:
    || 	4 <= A.length <= 10000
    || 	0 <= A[i] < 10000
    || 	A.length is even

## ping: with Counter

```python
from collections import Counter
class Solution:     #ping: with Counter
    def repeatedNTimes(self, A: List[int]) -> int:
        return Counter(A).most_common(1)[0][0]
        """
        ||   ✔ Accepted
        ||   ✔ 102/102 cases passed (236 ms)
        ||   ✔ Your runtime beats 37.72 % of python3 submissions
        ||   ✔ Your memory usage beats 73.47 % of python3 submissions (14.1 MB)
        """
```

## lmv: with set

```python
def repeatedNTimes(self, A: List[int]) -> int:  #lmv
    unique = set()       # empty set
    for i in A:
        if i in unique:  # if i already exists then it is a duplicate
            return i     # loop is exited as value is directly returned
        unique.add(i)    # this can be kept in else: part but not required

    """
    ||   ✔ Accepted
    ||   ✔ 102/102 cases passed (232 ms)
    ||   ✔ Your runtime beats 44.44 % of python3 submissions
    ||   ✔ Your memory usage beats 93.88 % of python3 submissions (14 MB)
    """
```
