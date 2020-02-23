---
layout: post
title: "two-sum-ii-input-array-is-sorted"
published: true
created:  2020 Feb 23 02:45:47 PM
tags: [python, list, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [two-sum-ii-input-array-is-sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

|| * algorithms
|| * Easy (52.45%)
|| * Likes:    1306
|| * Dislikes: 522
|| * Total Accepted:    346.2K
|| * Total Submissions: 658.1K
|| * Testcase Example:  '[2,7,11,15]\n9'
|| * Source Code:       167.two-sum-ii-input-array-is-sorted.py
|| 
|| Given an array of integers that is already sorted in ascending order, find
|| two numbers such that they add up to a specific target number.
|| 
|| The function twoSum should return indices of the two numbers such that they
|| add up to the target, where index1 must be less than index2.
|| 
|| Note:
|| 
|| 
|| 	Your returned answers (both index1 and index2) are not zero-based.
|| 	You may assume that each input would have exactly one solution and you may not use the same element twice.
|| 
|| 
|| Example:
|| 
|| 
|| Input: numbers = [2,7,11,15], target = 9
|| Output: [1,2]
|| Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

## ping

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target-numbers[i] in numbers[i+1:]:
                return [i+1, i+2+numbers[i+1:].index(target-numbers[i])]
        return None
```

## lmv

    """
    Two Sum II - Input array is sorted

    Python different solutions (two-pointer, dictionary, binary search).

    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249

    * Lang:    python3
    * Author:  caikehe
    * Votes:   218
    """

```python
class Solution:
    # two-pointer
    def twoSum1(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

class Solution:
    # dictionary
    def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

class Solution:
    # binary search
    def twoSum(self, numbers, target):
        for i in xrange(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1
```

# @lc code=end
