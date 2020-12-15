---
layout: post
title: "[56] Merge interval"
date: 2020-01-27
author: "owen"
tags: 
    - list
    - sort
    - sorted
    - class
    - easy
    - medium 
    - python
    - google 
    
created:  20120 Jan 28 12:39:49 PM
categories: [tech]
published: true

---


TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[56] Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)

    || * algorithms
    || * Medium (37.78%)
    || * Likes:    3152
    || * Dislikes: 242
    || * Total Accepted:    487.2K
    || * Total Submissions: 1.3M
    || * Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
    || 
    || Given a collection of intervals, merge all overlapping intervals.
    || 
    || Example 1:
    || 
    || Input: [[1,3],[2,6],[8,10],[15,18]]
    || Output: [[1,6],[8,10],[15,18]]
    || Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    || 
    || Example 2:
    || 
    || Input: [[1,4],[4,5]]
    || Output: [[1,5]]
    || Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    || 
    || NOTE: input types have been changed on April 15, 2019. Please reset to
    default code definition to get new method signature.

see also: [Merge Intervals](https://www.interviewbit.com/problems/merge-intervals/)

## owen

just a sort can solve this issue

```python
#Given a set of non-overlapping intervals, insert a new interval into the
#intervals (merge if necessary).
#You may assume that the intervals were initially sorted according to their
#start times.
#Example 1:
#Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, new_interval):
        new_interval.start, new_interval.end = min(new_interval.start,new_interval.end), max(new_interval.start,new_interval.end)
        intervals.append(new_interval)
        intervals = sorted(intervals, key=lambda x: x.start)
        cur = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if cur.end >= intervals[i].start:
                cur.end = max(intervals[i].end, cur.end)
                continue
            res.append(cur)
            cur = intervals[i]
        res.append(cur)
        return res
```
### Basic idea

检查i的END 和i+1 START/END的关系

## wangmazi

```python
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        result = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result
```

### tips

* sort all lists based on start value

