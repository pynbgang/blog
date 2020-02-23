---
layout: post
title: "merge sorted array"
published: true
created:  2020 Feb 23 02:06:26 PM
tags: [list, python, easy, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[88] Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)

|| * algorithms
|| * Easy (37.93%)
|| * Likes:    1674
|| * Dislikes: 3572
|| * Total Accepted:    492K
|| * Total Submissions: 1.3M
|| * Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
|| 
|| Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
|| 
|| Note:
|| 
|| 
|| 	The number of elements initialized in nums1 and nums2 are m and n respectively.
|| 	You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
|| 
|| 
|| Example:
|| 
|| 
|| Input:
|| nums1 = [1,2,3,0,0,0], m = 3
|| nums2 = [2,5,6],       n = 3
|| 
|| Output: [1,2,2,3,5,6]

## ping

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for num2 in nums2:                  #for each num in nums2
            i = 0
            while i<m:                 #iterate nums1 to find insert pos
                if num2 <= nums1[i]:        #  if found ever
                    nums1.insert(i, num2)   #  insert
                    nums1.pop()             #  and pop the ending 0
                    break                   #  and that's it for this num2
                i += 1
            else:                           #otherwise, use this num2 to
                nums1[m] = num2        #  update the first 0 in the end
            m = m+1               #update nums1 len after insertion

```

## lmv

    """
    https://leetcode.com/problems/merge-sorted-array/discuss/29699

    * Lang:    python3
    * Author:  lime66
    * Votes:   31
    """

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]
