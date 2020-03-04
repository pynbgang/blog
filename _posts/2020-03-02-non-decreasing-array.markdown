---
layout: post
title: "non-decreasing-array"
published: true
created:  2020 Mar 02 09:43:51 PM
tags: [leetcode, python, easy, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[665] Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/description/)

    || * algorithms
    || * Easy (19.44%)
    || * Likes:    1517
    || * Dislikes: 358
    || * Total Accepted:    78.6K
    || * Total Submissions: 404.3K
    || * Testcase Example:  '[4,2,3]'
    || * Source Code:       665.non-decreasing-array.py
    || 
    || Given an array with n integers, your task is to check if it could become
    non-decreasing by modifying at most 1 element.
    || 
    || We define an array is non-decreasing if array[i]  holds for every i (1 
    || 
    || Example 1:
    || 
    || Input: [4,2,3]
    || Output: True
    || Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
    || 
    || Example 2:
    || 
    || Input: [4,2,1]
    || Output: False
    || Explanation: You can't get a non-decreasing array by modify at most one element.
    || 
    || Note:
    || The n belongs to [1, 10,000].

## ping: fail

```python
class Solution:     #ping: fail
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
            if count == 2:
                return False
        return True

        """
        ||   ✘ Wrong Answer
        ||   ✘ 312/325 cases passed (N/A)
        ||   ✘ Testcase: [4,2,3]
        ||   ✘ Answer: false
        ||   ✘ Expected Answer: true
        ||   ✘ Stdout:
        """
```

## ping: pass

```python
class Solution:     #ping: pass
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:     #search for unexpected small num(USN)
                count += 1              #and count it
                if count == 2:          #if found 2 USN, then False
                    return False        #            i-2 i-1 i  i+1
                else:                   #corner case: [3, 4, 2, 3]
                    if  i-2 >= 0        and nums[i-2] > nums[i] and \
                        i+1 < len(nums) and nums[i-1] > nums[i+1]:
                        return False
        return True

        """
        ||   ✔ Accepted
        ||   ✔ 325/325 cases passed (192 ms)
        ||   ✔ Your runtime beats 93.64 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (13.8 MB)
        """
        #[3,4,2,3] ->
        #     ^
        #     i
        #
        #    [3,4,4,3]:  false
        #         ^
        #    [3,2,2,3]:  false
        #       ^
```

## lmv

```python
class Solution(object):     #lmv
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length, flag, pos = len(nums), 0, 0
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                if flag == 0:
                    flag = 1
                    pos = i
                else:
                    return False
        if  flag == 0 or                    \
            length == pos + 2 or            \
            pos == 0 or                     \
            nums[pos-1] <= nums[pos+1] or   \
            nums[pos] <= nums[pos+2]:
            return True
        return False
```

## other

```python
class Solution:     #internet
    def checkPossibility(self, nums: List[int]) -> bool:
        chance = 1
        for x in range(len(nums)):
            if x and nums[x] < nums[x - 1]:
                if not chance:
                    return False
                chance -= 1
                if x > 1 and nums[x] <= nums[x - 2]:
                    nums[x] = nums[x - 1]
        return True
```
