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

* auto-gen TOC:
{:toc}

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
## solution (from owen'blind guess)
class Solution(object):

   def maxChunksToSorted(self, arr):
   
        if len(arr)==1:
            return 1
        count=1
        for i in range(1,len(arr)):
            if min(arr[i:])>max(arr[0:i]):
                count+=1
        return count
        

## takeaway 

- each chunk should have same set of numbers while seperate from other chunks, since index will keep increasing, tracking max value or sum of all previous numbers should be reliable
- Owen's solution is to use DP thought,ideally the max possiable count is len(arr) if it is already sorted,if it is not the possiable two split should hit the condition min(arr[i:])>max(arr[0:i]),basing on that ,the An=An-1+1 or An=An-1+0 ,then return the last An
