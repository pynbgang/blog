---
layout: post
title: "intersection-of-two-arrays-ii"
published: true
created:  2020 Feb 23 04:04:08 PM
tags: [leetcode, python, easy, list, brute force]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[350] Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/description/)

|| * algorithms
|| * Easy (50.18%)
|| * Likes:    1042
|| * Dislikes: 344
|| * Total Accepted:    289.9K
|| * Total Submissions: 576.7K
|| * Testcase Example:  '[1,2,2,1]\n[2,2]'
|| * Source Code:       350.intersection-of-two-arrays-ii.py
|| 
|| Given two arrays, write a function to compute their intersection.
|| 
|| Example 1:
|| 
|| Input: nums1 = [1,2,2,1], nums2 = [2,2]
|| Output: [2,2]
|| 
|| Example 2:
|| 
|| Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
|| Output: [4,9]
|| 
|| Note:
|| 
|| 	Each element in the result should appear as many times as it shows in both arrays.
|| 	The result can be in any order.
|| 
|| Follow up:
|| 
|| 	What if the given array is already sorted? How would you optimize your algorithm?
|| 	What if nums1's size is small compared to nums2's size? Which algorithm is better?
|| 	What if elements of nums2 are stored on disk, and the memory is limited
        such that you cannot load all elements into the memory at once?


## ping: brute force

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            if i in nums2:
                res.append(i)
                nums2.remove(i)
        return res
```

## lmv

Three Python Solutions

https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247

* Lang:    python3
* Author:  latnokz
* Votes:   121

### **two pointers:**

    class Solution(object):
        def intersect(self, nums1, nums2):

            nums1, nums2 = sorted(nums1), sorted(nums2)
            pt1 = pt2 = 0
            res = []

            while True:
                try:
                    if nums1[pt1] > nums2[pt2]:
                        pt2 += 1
                    elif nums1[pt1] < nums2[pt2]:
                        pt1 += 1
                    else:
                        res.append(nums1[pt1])
                        pt1 += 1
                        pt2 += 1
                except IndexError:
                    break

            return res

### **use `dictionary` to count:**

    class Solution(object):
        def intersect(self, nums1, nums2):

            counts = {}
            res = []

            for num in nums1:
                counts[num] = counts.get(num, 0) + 1

            for num in nums2:
                if num in counts and counts[num] > 0:
                    res.append(num)
                    counts[num] -= 1

            return res

### **use `Counter` to make it cleaner:**

    class Solution(object):
        def intersect(self, nums1, nums2):
    
            counts = collections.Counter(nums1)
            res = []

            for num in nums2:
                if counts[num] > 0:
                    res += num,
                    counts[num] -= 1

            return res

