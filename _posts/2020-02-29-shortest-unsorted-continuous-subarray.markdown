---
layout: post
title: "Shortest Unsorted Continuous Subarray"
published: true
created:  2020 Feb 29 09:09:28 PM
tags: [list, python, leetcode, easy, zip, media, zhoushen, guoqin]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[581] Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/)

    || * algorithms
    || * Easy (30.66%)
    || * Likes:    2116
    || * Dislikes: 106
    || * Total Accepted:    100.3K
    || * Total Submissions: 326.8K
    || * Testcase Example:  '[2,6,4,8,10,9,15]'
    || * Source Code:       581.shortest-unsorted-continuous-subarray.py
    || 
    || Given an integer array, you need to find one continuous subarray that if
    you only sort this subarray in ascending order, then the whole array will
    be sorted in ascending order, too.  
    || 
    || You need to find the shortest such subarray and output its length.
    || 
    || Example 1:
    || 
    || Input: [2, 6, 4, 8, 10, 9, 15]
    || Output: 5
    || Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
    || 
    || 
    || 
    || Note:
    || 
    || Then length of the input array is in range [1, 10,000].
    || The input array may contain duplicates, so ascending order here means . 
    || 
    || 

## ping: sort and compare two lists

```python
class Solution:     # ping: sort and compare
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums1=sorted(nums)
        start=stop=-1
        for i in range(len(nums)):
            if nums[i] is not nums1[i]:
                start = i; break
        for i in range(len(nums)-1,-1,-1):
            if nums[i] is not nums1[i]:
                stop = i; break
        return stop-start+1 if start is not -1 else 0
    """
    ||   ✔ Accepted
    ||   ✔ 307/307 cases passed (192 ms)
    ||   ✔ Your runtime beats 99.82 % of python3 submissions
    ||   ✔ Your memory usage beats 100 % of python3 submissions (13.8 MB)
    """
```

## ping: merge the two loops
```python
class Solution:     # ping: merge the two loops
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, stop, nums1 = -1, -1, sorted(nums)
        for i,j in zip(range(len(nums)), range(len(nums)-1,-1,-1)):
            if nums[i] is not nums1[i] and start==-1:
                start = i;
            if nums[j] is not nums1[j] and stop==-1:
                stop = j;
            if start != -1 and stop != -1: break
        return stop-start+1 if start is not -1 else 0

    """
    ||   ✔ Accepted
    ||   ✔ 307/307 cases passed (208 ms)
    ||   ✔ Your runtime beats 88.51 % of python3 submissions
    ||   ✔ Your memory usage beats 80 % of python3 submissions (14.1 MB)
    """
```

## lmv: nothing special
```python
class Solution:     #lmv, nothing special
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        start, end = -1, -1
        i = 0
        while(i < len(nums)):
            if nums[i] != sortedNums[i]:
                start = i
                break
            i += 1
        if start == -1: return 0 # already sorted
        i = len(nums) - 1
        while(i >= 0):
            if nums[i] != sortedNums[i]:
                end = i
                break
            i -= 1
        return end - start + 1

    """
    ||   ✔ Accepted
    ||   ✔ 307/307 cases passed (196 ms)
    ||   ✔ Your runtime beats 99.49 % of python3 submissions
    ||   ✔ Your memory usage beats 85 % of python3 submissions (14.1 MB)
    """
```

zhoushen & guoqin

<iframe allowfullscreen="" frameborder="0" height="270" src="https://www.youtube.com/embed/Ti5fdLn-ZTg" width="480"></iframe>
