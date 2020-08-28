---
layout: post
title: "[769]-max-chunks-to-make-sorted"
subtitle: ""
date: 2020-01-13
author: "xiaofo"
tags: 
    - list
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

    || [769] Max Chunks To Make Sorted  
    || 
    || https://leetcode.com/problems/max-chunks-to-make-sorted/description/
    || 
    || * algorithms
    || * Medium (53.52%)
    || * Likes:    791
    || * Dislikes: 120
    || * Total Accepted:    38.6K
    || * Total Submissions: 70.5K
    || * Testcase Example:  '[4,3,2,1,0]'
    || * Source Code:       769.max-chunks-to-make-sorted.py
    || 
    || Given an array arr that is a permutation of [0, 1, ..., arr.length - 1],
    we split the array into some number of "chunks" (partitions), and
    individually sort each chunk.  After concatenating them, the result equals
    the sorted array.
    || 
    || What is the most number of chunks we could have made?
    || 
    || Example 1:
    || 
    || Input: arr = [4,3,2,1,0]
    || Output: 1
    || Explanation:
    || Splitting into two or more chunks will not return the required result.
    || For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1,
    2], which isn't sorted.
    || 
    || 
    || Example 2:
    || Input: arr = [1,0,2,3,4]
    || Output: 4
    || Explanation:
    || We can split into two chunks, such as [1, 0], [2, 3, 4].
    || However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
    || 
    || Note:
    || 
    || 	arr will have length in range [1, 10].
    || 	arr[i] will be a permutation of [0, 1, ..., arr.length - 1].

https://www.lintcode.com/problem/max-chunks-to-make-sorted/description

## solution1 (most voted answer) 

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

split whenever: max of previous num equals to current index.

    0 1 2 3 4 5
    3 2 1 0|4|5

    0 1 2 3 4 5
    3 2 0 1|4|5

    0 1 2 3 4 5
    5 4 3 2 1 0

    0 1 2 3 4 5
    0|1|2|3|4|5

## solution2 

(steal idea from another most voted answer but simplify into better code) 

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

## solution3

(from owen'blind guess)

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


## solution: lmv

https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/586378

* Lang:    python3
* Author:  ozoli
* Votes:   0

`arr[i]` and `i` define an interval which has to be in the same chunk to ensure
that after sorting they end up in their correct place. After obtaining all the
initial interval which (the boundary conditions), we merge overlapping
intervals. The count of resulting distinct intervals is the solution `NlogN`
because of sort

```python
class Solution(object):     #lmv
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        intervals = []
        for i, n in enumerate(arr):
            intervals.append([min(i, arr[i]), max(i, arr[i])])
        intervals.sort()
        stack = []
        for interval in intervals:
            if not stack or  interval[0] > stack[-1][1]:
                stack.append(interval)
            else:
                a = stack.pop()
                stack.append([a[0], max(a[1], interval[1])])

        return len(stack)
```

## takeaway 

- each chunk should have same set of numbers while seperate from other chunks,
  since index will keep increasing, tracking max value or sum of all previous
  numbers should be reliable
- Owen's solution is to use DP thought,ideally the max possiable count is
  len(arr) if it is already sorted,if it is not the possiable two split should
  hit the condition min(arr[i:])>max(arr[0:i]),basing on that ,the An=An-1+1 or
  An=An-1+0 ,then return the last An

## notes (ping)

ideas are:

    solution1: cut whenever: current max == current index
    solution2: cut whenever: current sum of index == sum of nums (same as solution1)
    solution3: cut whenever: min(left) < max(right) 
    solution4: dfs


```python
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        if not arr: return 1
        res = 0
        for i in range(len(arr)):  #whenever id equals curr max, can split
            if i==max(arr[:i+1]):
                res += 1
        return res
```
