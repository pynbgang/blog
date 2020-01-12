---
layout: post
title: "image-overlap"
subtitle: ""
date: 2020-01-07
author: "xiaofo"
tags: 
    - array
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

# [image-overlap](https://leetcode.com/problems/image-overlap/)

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
