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
    - enumerate
    - wangmazi
created:  2020 Jan 13 22:50:11 AM
categories: [tech]
published: true

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [max-chunks-to-make-sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/)

https://www.lintcode.com/problem/max-chunks-to-make-sorted/description

## solution1 (most voted answer 1) 

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


## solution2 (steal idea from another most voted answer but simplify into better code) 

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

## solution3 (from owen'blind guess)

```python
class Solution(object):
   def maxChunksToSorted(self, arr):
        if len(arr)==1:
            return 1
        count=1
        for i in range(1,len(arr)):
            if min(arr[i:])>max(arr[0:i]):
                count+=1
        return count
```

## solution4: wangmazi

```python
class Solution(object):
    def maxChunksToSorted(self, arr):
        checked = [False]*len(arr)
        count = 0
        i = 0
        while i < len(arr):
            lmax = dodfs(i, -1)
            i += 1
            while i < lmax + 1:
                if not checked[i]:
                    lmax = dodfs(i, lmax)
                i += 1
            count += 1

        def dodfs(cur, lmax):
            checked[cur] = True
            lmax = max(lmax, cur)
            if not checked[arr[cur]]:
                return dodfs(arr[cur], lmax)
            return lmax

        return count
```


## takeaway 

- each chunk should have same set of numbers while seperate from other chunks,
  since index will keep increasing, tracking max value or sum of all previous
  numbers should be reliable
- Owen's solution is to use DP thought,ideally the max possiable count is
  len(arr) if it is already sorted,if it is not the possiable two split should
  hit the condition min(arr[i:])>max(arr[0:i]),basing on that ,the An=An-1+1 or
  An=An-1+0 ,then return the last An

## misc notes

ideas are:

    solution1: cut whenever: current max == current index
    solution2: cut whenever: current sum of index == sum of nums (same as solution1)
    solution3: cut whenever: min(left) < max(right) 
    solution4: dfs
