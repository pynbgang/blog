---
layout: post
title: "max-chunks-to-make-sorted"
subtitle: ""
date: 2020-01-13
author: "xiaofo"
tags: 
    - array
    - leetcode
    - medium
    - python
    - xiaofo
created:  2020 Jan 13 22:50:11 AM
categories: [tech]
published: true

---

TABLE OF CONTENT
[TOC]

- - -

# [max-chunks-to-make-sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/)

## solution (most voted answer 1) 

```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curmax, res = -1, 0
        for i, n in enumerate(arr):
            curmax = max(curmax, n)
            if i == curmax:
                res += 1
        return res
```

## solution (steal idea from another most voted answer but simplify into better code) 

```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        idxsum, numsum, res = 0, 0, 0
        for i, n in enumerate(arr):
            idxsum, numsum = idxsum + i, numsum + n
            if idxsum == numsum:
                res += 1
        return res
```

## takeaway 

- each chunk should have same set of numbers while seperate from other chunks, since index will keep increasing, tracking max value or sum of all previous numbers should be reliable
