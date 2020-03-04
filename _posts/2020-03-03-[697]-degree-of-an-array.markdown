---
layout: post
title: "Degree of an Array"
published: true
created:  2020 Mar 03 12:45:36 AM
tags: [python, leetcode, easy, list, Counter]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[697] Degree of an Array](https://leetcode.com/problems/degree-of-an-array/description/)

    || * algorithms
    || * Easy (52.64%)
    || * Likes:    728
    || * Dislikes: 658
    || * Total Accepted:    72.2K
    || * Total Submissions: 136.4K
    || * Testcase Example:  '[1,2,2,3,1]'
    || * Source Code:       697.degree-of-an-array.py
    || 
    || Given a non-empty array of non-negative integers nums, the degree of
    this array is defined as the maximum frequency of any one of its elements.
    || Your task is to find the smallest possible length of a (contiguous)
    subarray of nums, that has the same degree as nums.
    || 
    || Example 1:
    || 
    || Input: [1, 2, 2, 3, 1]
    || Output: 2
    || Explanation: 
    || The input array has a degree of 2 because both elements 1 and 2 appear twice.
    || Of the subarrays that have the same degree:
    || [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    || The shortest length is 2. So return 2.
    || 
    || Example 2:
    || 
    || Input: [1,2,2,3,1,4,2]
    || Output: 6
    || 
    || Note:
    || nums.length will be between 1 and 50,000.
    || nums[i] will be an integer between 0 and 49,999.

## ping: brute force, Counter

```python
class Solution:     #ping: brute force, Counter
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import Counter
        nums_rev, len1, min1, d = nums[::-1], len(nums), len(nums), Counter(nums)
        freq = d.most_common(1)[0][1]
        for n in (k for k in d.keys() if d[k]==freq):
            min1 = min(min1, len1-nums_rev.index(n)-nums.index(n))
        return min1

        """
        ||   ✔ Accepted
        ||   ✔ 89/89 cases passed (796 ms)
        ||   ✔ Your runtime beats 12.91 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (13.6 MB)
"""
```

## lmv
```python
class Solution:     #lmv
    def findShortestSubArray(self, nums: List[int]) -> int:
        C = {}
        for i, n in enumerate(nums):
            if n in C: C[n].append(i)
            else: C[n] = [i]
        M = max([len(i) for i in C.values()])
        return min([i[-1]-i[0] for i in C.values() if len(i) == M]) + 1

        """
        ||   ✔ Accepted
        ||   ✔ 89/89 cases passed (228 ms)
        ||   ✔ Your runtime beats 95.61 % of python3 submissions
        ||   ✔ Your memory usage beats 9.09 % of python3 submissions (15.1 MB)
        """
```

