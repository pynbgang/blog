---
layout: post
title: "Max Sum Contiguous Subarray"
author: "owen"
published: true
created:  2020 Jan 13 23:34:22 PM
tags: [fb, google, python, interview]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# Question

Find the contiguous subarray within an array, A of length N which has the largest sum
https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

# Code

```python
class Solution:
    def maxSubArray(self, nums):
        # write your code here
        n=len(nums)
        if n==1:
            return nums[0]
        min_prefix_sum=0
        max_sum=-sys.maxsize
        prefix_sum=0
        for num in nums:
            prefix_sum+=num
            max_sum=max(max_sum,prefix_sum-min_prefix_sum)
            min_prefix_sum=min(min_prefix_sum,prefix_sum)
        return max_sum
```

# 思路

  - 字符子串问题 
  - 核心思想就是做单次循环的时候，当到达INDEX i的时候的最长子串的合等于sum(list[0-i])-min(子串合)
  - O（n）时间 
