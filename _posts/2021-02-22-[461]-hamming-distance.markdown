---
layout: post
title: "[461] Hamming Distance"
published: true
created:  2021 Feb 22 12:06:18
tags: [python, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[461] Hamming Distance](https://leetcode.com/problems/hamming-distance/description/)

    || * algorithms
    || * Easy (73.05%)
    || * Likes:    2108
    || * Dislikes: 175
    || * Total Accepted:    385.3K
    || * Total Submissions: 526.5K
    || * Testcase Example:  '1\n4'
    || * Source Code:       461.hamming-distance.py
    || 
    || The Hamming distance between two integers is the number of positions at
    which the corresponding bits are different.
    || 
    || Given two integers x and y, calculate the Hamming distance.
    || 
    || Note:
    || 0 ≤ x, y < 2^31.
    || 
    || 
    || Example:
    || 
    || Input: x = 1, y = 4
    || 
    || Output: 2
    || 
    || Explanation:
    || 1   (0 0 0 1)
    || 4   (0 1 0 0)
    || ⁠      ↑   ↑
    || 
    || The above arrows point to positions where the corresponding bits are different.

# solution

```python
class Solution:     #exactly same as lmv, :D...
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
```

