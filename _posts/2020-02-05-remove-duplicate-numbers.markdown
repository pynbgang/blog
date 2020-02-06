---
layout: post
title: "remove duplicate numbers"
published: true
created:  2020 Feb 05 08:17:16 PM
tags: [list, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [remove-duplicate-numbers-in-array](https://www.lintcode.com/problem/remove-duplicate-numbers-in-array/description?_from=ladder&&fromId=99)

## use extra space

```python
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        exist = set()
        res = 0

        for num in nums:
            if num not in exist:
                nums[res] = num
                res += 1
                exist.add(num)
        return res
```

## wangmazi

```python
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        d, result = {}, 0
        for num in nums:
            if num not in d:
                d[num] = True
                nums[result] = num
                result += 1

        return result

# O(nlogn) time, O(1) extra space
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        n = len(nums)
        if n == 0:
            return 0
        nums.sort()
        result = 1
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1
        return result
```


# [remove-duplicates-from-sorted-array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## leetcode most voted

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums)-1):
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
        return(x)
```

## illustration

        2
        v
    [1, 2, 3, 3, 4, 4, 5, 6]
     ^  ^ 
        2

           3
           v
    [1, 2, 3, 3, 4, 4, 5, 6]
        ^  ^
           3

              v
    [1, 2, 3, 3, 4, 4, 5, 6]
           ^  ^

              4
              v
    [1, 2, 3, 3, 4, 4, 5, 6]
              ^  ^

                 v
    [1, 2, 3, 4, 4, 4, 5, 6]
                 ^  ^

                 5
                 v
    [1, 2, 3, 4, 4, 4, 5, 6]
                    ^  ^

                    6
                    v
    [1, 2, 3, 4, 5, 4, 5, 6]
                       ^  ^

                       v
    [1, 2, 3, 4, 5, 6, 5, 6]
                          ^  ^
                          out of range


