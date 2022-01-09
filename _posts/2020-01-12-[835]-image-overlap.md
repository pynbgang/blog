---
layout: post
title: "[835]-image-overlap"
subtitle: ""
date: 2020-01-07
author: "xiaofo"
tags:
    - list
    - leetcode
    - medium
    - python
    - xiaofo
    - max
    - dict
    - grid
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
    || Two images A and B are given, represented as binary, square matrices of
    the same size.  (A binary matrix has only 0s and 1s as values.)
    ||
    || We translate one image however we choose (sliding it left, right, up, or
    down any number of units), and place it on top of the other image.  After,
    the overlap of this translation is the number of positions that have a 1 in
    both images.
    ||
    || (Note also that a translation does not include any kind of rotation.)
    ||
    || What is the largest possible overlap?
    ||
    || Example 1:
    ||
    ||
    || Input:
    ||        A = [[1,1,0],
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
    || 	0 <= A[i][j], B[i][j] <= 2

## solution

(again after peeping most voted solution)

```python
class Solution:
    from typing import List
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        #for both grid, get coordinates of all '1' spots
        pa = [(i, j) for j in range(len(A[0])) for i in range(len(A)) if A[i][j]]
        pb = [(i, j) for j in range(len(B[0])) for i in range(len(B)) if B[i][j]]
        d = dict()
        #brute force, between each '1' spot of A and B, and calculate the offset
        #there are chances the offset of some spots happens to be the same
        #so record the number of time that a same offset appears
        #=> a dict is the best structure for this requirements:
        # key: record the different pattern
        # value: record the number of time the pattern appears ever
        for t1 in pa:
            for t2 in pb:
                t = (t1[0] - t2[0], t1[1] - t2[1])
                d[t] = d.get(t, 0) + 1
        return max(d.values() or [0])
```

test:


```python
A=[[1,1,0], [0,1,0], [0,1,0]]
B=[[0,0,0], [0,1,1], [0,0,1]]
S=Solution()
print(S.largestOverlap(A,B))
```

# using complex (from 695)

```python
class Solution:
    from typing import List
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        pa = [i+j*1j for j in range(len(A[0])) for i in range(len(A)) if A[i][j]]
        pb = [i+j*1j for j in range(len(B[0])) for i in range(len(B)) if B[i][j]]
        d = dict()
        for t1 in pa:
            for t2 in pb:
                t = t1-t2
                d[t] = d.get(t, 0) + 1
        return max(d.values() or [0])
```

## tips/takeaway

- get coordinates of spot 1 for both A and B
- between each pair of spots of 1 from A and B, get the offset
  needed for them to overlap, and put in a dict:
  * offset as key
  * value of offset is the number of time same offset appears in all pair of spots
  * each time same offset is used, increase the value by 1
- the offset with maximum value would be the answer
- max 的固定用法 max( expr or [0])  覆盖了如果前面表达式可能为空列表的特例
