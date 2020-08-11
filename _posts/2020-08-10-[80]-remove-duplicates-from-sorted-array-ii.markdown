---
layout: post
title: "[80] Remove Duplicates from Sorted Array II"
published: true
created:  2020 Aug 10 10:16:20 AM
tags: [python, leetcode, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[80] Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/)

    || * algorithms
    || * Medium (42.35%)
    || * Likes:    882
    || * Dislikes: 636
    || * Total Accepted:    237.6K
    || * Total Submissions: 560.7K
    || * Testcase Example:  '[1,1,1,2,2,3]'
    || * Source Code:       80.remove-duplicates-from-sorted-array-ii.py
    ||
    || Given a sorted array nums, remove the duplicates in-place such that
    duplicates appeared at most twice and return the new length.
    ||
    || Do not allocate extra space for another array, you must do this by
    modifying the input array in-place with O(1) extra memory.
    ||
    || Example 1:
    ||
    || Given nums = [1,1,1,2,2,3],
    ||
    || Your function should return length = 5, with the first five elements of
    nums being 1, 1, 2, 2 and 3 respectively.
    ||
    || It doesn't matter what you leave beyond the returned length.
    ||
    || Example 2:
    ||
    || Given nums = [0,0,1,1,1,1,2,3,3],
    ||
    || Your function should return length = 7, with the first seven elements of
    nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
    ||
    || It doesn't matter what values are set beyond the returned length.
    ||
    ||
    || Clarification:
    ||
    || Confused why the returned value is an integer but your answer is an array?
    ||
    || Note that the input array is passed in by reference, which means
    modification to the input array will be known to the caller as well.
    ||
    || Internally you can think of this:
    ||
    ||
    || // nums is passed in by reference. (i.e., without making a copy)
    || int len = removeDuplicates(nums);
    ||
    || // any modification to nums in your function would be known by the caller.
    || // using the length returned by your function, it prints the first len elements.
    || for (int i = 0; i < len; i++) {
    ||     print(nums[i]);
    || }

## owen

```python
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:return 0
        if len(nums)<=2:return len(nums)
        i,j=0,1
        temp=[]
        while(j<=len(nums)-1):
            if nums[i]==nums[j] and j-i<2:
                j+=1
            elif nums[i]==nums[j] and j-i>=2:
                temp.append(j)
                j+=1
            elif nums[i]!=nums[j]:
                i=j
                j+=1
        while (len(temp)>=1):
            nums.pop(temp[0])
            temp.pop(0)
            for i in range(len(temp)):
                temp[i]-=1
        return
```
## jj

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre, p, cnt = 0, 0, 0
        for i, n in enumerate(nums):
            if n != pre:
                nums[p], pre, p, cnt = n, n, p + 1, 1
            elif cnt < 2:
                nums[p], p, cnt = n, p + 1, cnt + 1
        return p
```

## others
```python
class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
```
