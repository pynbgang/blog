---
layout: post
title: "Maximum Distance in Arrays"
published: true
created:  2020 Feb 29 09:58:16 PM
tags: [python, list, easy, leetcode, media]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[624] Maximum Distance in Arrays](https://leetcode.com/problems/maximum-distance-in-arrays/description/)

    || * algorithms
    || * Easy (38.43%)
    || * Likes:    310
    || * Dislikes: 46
    || * Total Accepted:    17.8K
    || * Total Submissions: 46.2K
    || * Testcase Example:  '[[1,2,3],[4,5],[1,2,3]]'
    || * Source Code:       624.maximum-distance-in-arrays.py
    || 
    || 
    || Given m arrays, and each array is sorted in ascending order. Now you can
    pick up two integers from two different arrays (each array picks one) and
    calculate the distance. We define the distance between two integers a and b
    to be their absolute difference |a-b|. Your task is to find the maximum
    distance.
    || 
    || 
    || Example 1:
    || 
    || Input: 
    || [[1,2,3],
    || ⁠[4,5],
    || ⁠[1,2,3]]
    || Output: 4
    || Explanation: 
    || One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
    || 
    || 
    || 	
    || Note:
    || 
    || Each given array will have at least 1 number. There will be at least two non-empty arrays.
    || The total number of the integers in all the m arrays will be in the range of [2, 10000].
    || The integers in the m arrays will be in the range of [-10000, 10000].

## ping: failed

```python
from typing import List
class Solution:     #ping: failed, answer not correct

    def isinsameset(self, low, high, arrays):
        set1 = set(); set2 = set()
        for i in range(len(arrays)):
            if low in arrays[i]:
                set1.add(i)
            if high in arrays[i]:
                set2.add(i)
        if set1 != set2 or len(set1) > 1:
            return high-low
        else:
            return -1

    def maxDistance(self, arrays: List[List[int]]) -> int:
        l = []
        #arrays=[[1,2,3],[4,5],[1,2,3]]
        for array in arrays: l.extend(array)
        l = sorted(list(set(l)))
        i, j = 0, len(l)-1

        while i<j:
            res = self.isinsameset(l[i], l[j], arrays)
            if res is not -1: return res
            else:
                res = max(
                    max(self.isinsameset(l[i+1], l[j], arrays),
                        self.isinsameset(l[i], l[j-1], arrays)
                    )
                )
                if res is not -1:
                    return res
                else:
                    i+=1; j-=1
        return 0
```

## ping: passed

```python
class Solution:     #ping: passed

    def isinsameset(self, low, high, arrays):
        set1 = set(); set2 = set()
        for i in range(len(arrays)):
            if low in arrays[i]:
                set1.add(i)
            if high in arrays[i]:
                set2.add(i)
        if set1 != set2 or len(set1) > 1:
            return high-low
        else:
            return -1

    def maxDistance(self, arrays: List[List[int]]) -> int:
        l = []
        for array in arrays: 
            l.extend([array[0], array[-1]])
        l = sorted(list(set(l)))
        res = self.isinsameset(l[0], l[-1], arrays)
        if res is not -1: return res
        else:
            return max(
                max(self.isinsameset(l[i], l[-1], arrays) for i in range(len(l)-1)),
                max(self.isinsameset(l[0], l[i], arrays) for i in range(1, len(l)))
            )

        """
        ||   ✔ Accepted
        ||   ✔ 124/124 cases passed (156 ms)
        ||   ✔ Your runtime beats 92.59 % of python3 submissions
        ||   ✔ Your memory usage beats 50 % of python3 submissions (15.8 MB)
        """
```

## lmv

```python
class Solution:     #lmv
    """
    Maximum Distance in Arrays

    Intuitive faster than 90% Python solution with comments!

    https://leetcode.com/problems/maximum-distance-in-arrays/discuss/525668

    * Lang:    python3
    * Author:  cglotr
    * Votes:   0

    Do two pass to find the maximum distance. Fix leftmost in the first pass & fix
    rightmost in the second.
    """

    def maxDistance(self, arrays: List[List[int]]) -> int:
        flat = []
        for i, arr in enumerate(arrays):
            for a in arr:
                flat.append((a, i))
        flat.sort(key=lambda a: a[0])

        maxdiff = 0

        # fixed leftmost & move from right to left
        for i in range(len(flat) - 1, 0, -1):
            v, index = flat[i]
            if index != flat[0][1]:
                leftmostval = flat[0][0]
                maxdiff = max(maxdiff, abs(v - leftmostval))
                break

        # fixed rightmost & move from left to right
        for i in range(len(flat) - 1):
            v, index = flat[i]
            if index != flat[-1][1]:
                rightmostval = flat[-1][0]
                maxdiff = max(maxdiff, abs(v - rightmostval))
                break

        return maxdiff

        """
        ||   ✔ Accepted
        ||   ✔ 124/124 cases passed (172 ms)
        ||   ✔ Your runtime beats 56.94 % of python3 submissions
        ||   ✔ Your memory usage beats 50 % of python3 submissions (16 MB)
        """
```

## internet (shortest)

```python
class Solution:     #internet
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        res, curMin, curMax = 0, 10000, -10000
        for a in arrays :
            res = max(res, max(a[-1]-curMin, curMax-a[0]))
            curMin, curMax = min(curMin, a[0]), max(curMax, a[-1])
        return res
```

<iframe width="560" height="315" src="https://www.youtube.com/embed/Rnr7vK2k788" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
