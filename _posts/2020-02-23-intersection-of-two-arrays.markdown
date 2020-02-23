---
layout: post
title: "intersection-of-two-arrays"
published: true
created:  2020 Feb 23 03:47:28 PM
tags: [python, leetcode, easy, string]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[349] Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/)

|| * algorithms
|| * Easy (59.05%)
|| * Likes:    610
|| * Dislikes: 1020
|| * Total Accepted:    303.4K
|| * Total Submissions: 510.8K
|| * Testcase Example:  '[1,2,2,1]\n[2,2]'
|| * Source Code:       349.intersection-of-two-arrays.py
|| 
|| Given two arrays, write a function to compute their intersection.
|| 
|| Example 1:
|| 
|| Input: nums1 = [1,2,2,1], nums2 = [2,2]
|| Output: [2]
|| 
|| Example 2:
|| 
|| Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
|| Output: [9,4]
|| 
|| Note:
|| 
|| 
|| 	Each element in the result must be unique.
|| 	The result can be in any order.

## ping

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

## lmv

Intersection of Two Arrays

Four Python solutions with simple explanation

https://leetcode.com/problems/intersection-of-two-arrays/discuss/82006

* Lang:    python3
* Author:  CoderChang
* Votes:   57

### Solution 1:

use set operation in python, one-line solution.

    class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))


### Solution 2:

brute-force searching, search each element of the first list in the second
list. (to be more efficient, you can sort the second list and use binary search
to accelerate)

    class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        
        return res

### Solution 3:

use dict/hashmap to record all nums appeared in the first list, and then check if there are nums in the second list have appeared in the map.

    class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] = 0
        
        return res

### Solution 4:

sort the two list, and use two pointer to search in the lists to find common elements.

    class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if not (len(res) and nums1[i] == res[len(res)-1]):
                    res.append(nums1[i])
                i += 1
                j += 1
        
        return res

