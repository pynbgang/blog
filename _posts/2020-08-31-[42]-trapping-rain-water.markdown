---
layout: post
title: "[42] trapping rain water"
published: true
created:  2020 Aug 31 03:44:10 PM
tags: [python, leetcode, leetcode, hard, timeit]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[42] Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)

    || * algorithms
    || * Hard (46.53%)
    || * Likes:    7844
    || * Dislikes: 130
    || * Total Accepted:    553.1K
    || * Total Submissions: 1.1M
    || * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
    || * Source Code:       42.trapping-rain-water.py
    ||
    || Given n non-negative integers representing an elevation map where the
    width of each bar is 1, compute how much water it is able to trap after
    raining.
    ||
    ||
    || The above elevation map is represented by array
    [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
    section) are being trapped. Thanks Marcos for contributing this image!
    ||
    || Example:
    ||
    ||
    || Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    || Output: 6

# ping

## diagram and idea

height = [2,1,3,5,2,3,4]

             +--+
             |5 |
             |  |     +--+
           3 |  |   3 |4 |
     2    +--+  |2 +--+  |
    +--+  |  |  +--+  |  |
    |  |1 |  |  |  |  |  |
    |  +--+  |  |  |  |  |
    +--------+--+--+--+--+----
     0  1  2  3  4  5  6

idea(great):

http://logos23333.top/algorithm/2017/12/04/leetcode-42/

## code

psudo code:

```python
for i in range(len(height)):
    lower_of_highest_walls = min(left_most, right_most)
    drops = lower_of_highest_walls - height[i]
    res += drops
```

code:

```python
class Solution: #ping, per http://logos23333.top/algorithm/2017/12/04/leetcode-42/
    def trap(self, height: List[int]) -> int:
        return sum(min(max(height[:i+1]), max(height[i:])) - height[i] for i in range(len(height)))
```

## timeit

```python
[ins] In [6]: %%timeit -r 3 -n 10
         ...: S=Solution()
         ...: height = [2,1,3,5,2,3,4]*100
         ...: S.trap(height)
         ...:
         ...:
32.1 ms ± 4.18 ms per loop (mean ± std. dev. of 3 runs, 10 loops each)
```


# jj: double pointers

## code

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        lbar, rbar, res, l, r = 0, 0, 0, 0, len(height) - 1
        while l < r:
            lbar, rbar = max(lbar, height[l]), max(rbar, height[r])
            if lbar < rbar:
                res, l = res + lbar - height[l], l + 1
            else:
                res, r = res + rbar - height[r], r - 1
        return res
```

## timeit

```python
[ins] In [8]: %%timeit -r 3 -n 10
         ...: S=Solution()
         ...: height = [2,1,3,5,2,3,4]*100
         ...: S.trap(height)
         ...:
         ...:
2.18 ms ± 401 µs per loop (mean ± std. dev. of 3 runs, 10 loops each)
```

this is 10 times faster!

