---
layout: post
title: "image-overlap"
subtitle: ""
date: 2020-01-07
author: "xiaofo"
tags: 
    - list
    - leetcode
    - medium
    - python
    - xiaofo
created:  2020 Jan 12 07:37:12 AM
categories: [tech]
published: true

---

TABLE OF CONTENT
[TOC]

- - -

# [[835] image-overlap](https://leetcode.com/problems/image-overlap/)

    || * algorithms
    || * Medium (55.77%)
    || * Likes:    350
    || * Dislikes: 467
    || * Total Accepted:    21.8K
    || * Total Submissions: 37.3K
    || * Testcase Example:  '[[1,1,0],[0,1,0],[0,1,0]]\n[[0,0,0],[0,1,1],[0,0,1]]'
    || * Source Code:       835.image-overlap.py
    || 
    || Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)
    || 
    || We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.
    || 
    || (Note also that a translation does not include any kind of rotation.)
    || 
    || What is the largest possible overlap?
    || 
    || Example 1:
    || 
    || 
    || Input: A = [[1,1,0],
    || ⁠           [0,1,0],
    ||             [0,1,0]]
    ||        B = [[0,0,0],
    ||             [0,1,1],
    ||             [0,0,1]]
    || Output: 3
    || Explanation: We slide A to right by 1 unit and down by 1 unit.
    || 
    || Notes: 
    || 
    || 
    || 	1 <= A.length = A[0].length = B.length = B[0].length <= 30
    || 	0 <= A[i][j], B[i][j] <= 1

## solution (again after peeping most voted solution) 

```python
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        pa = [(i, j) for j in range(len(A[0])) for i in range(len(A)) if A[i][j]]
        pb = [(i, j) for j in range(len(B[0])) for i in range(len(B)) if B[i][j]]
        d = dict()
        for t1 in pa:
            for t2 in pb:
                p = (t1[0] - t2[0], t1[1] - t2[1])
                d[p] = d.get(p, 0) + 1
        return max(d.values() or [0]) 
```
## takeaway 

- get coordinates of all 1 for both A and B
- for each pair of points from A and B, compare coordinates to get the offset needed for them to overlap, and put in dict using offset as key
- the offset with maximum value would be the answer
