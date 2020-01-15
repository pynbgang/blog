---
layout: post
title: "Max Sum Contiguous Subarray"
author: "owen"
published: true
created:  2020 Jan 13 23:34:22 PM
tags: [fb, google, python, interview, list, sys]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [maximum-subarray](https://www.lintcode.com/problem/maximum-subarray/description)

Find the contiguous subarray within an array, A of length N which has the
largest sum

* https://leetcode.com/problems/maximum-subarray/
* https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

# owen

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
            max_sum=max(max_sum, prefix_sum - min_prefix_sum)
            min_prefix_sum=min(min_prefix_sum, prefix_sum)
        return max_sum
```

# 思路 (owen)

- 字符子串问题 
- 核心思想就是做单次循环的时候，当到达INDEX i的时候的最长子串的合等于sum(list[0-i])-min(子串合)
- O（n）时间 

# wangmazi

```python
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        #pres记录前i个数的和，mins记录前i个数中总和和最小的一段（0-k）, maxs记录全局最大值，
        mins, pres, maxs = 0,0, -sys.maxsize

        for num in nums:
            pres += num
            maxs = max(maxs, pres - mins)
            mins = min(mins, pres)

        return maxs
```

# ping


    1   2   3   -7  -1  5   2   -1
    -------------------------       pres: 0到i的简单累加
    ------------------              mins: 0到i累加过程中，发现的一段总和最小的区间
                        -----       maxs: pres-mins

推导如下：

    init: mins = 0 (so only update when seeing nagative num) 
    get 1:
        pres: set 1, 
        maxs: set 1 (because 1 < -sys.maxsize)
        mins: 0 no change
    get 2:
        pres: set 1+2=3
        maxs: max(last max1, pres - last min0=pres) = 3
        mins: 0 no change
    get 3:
        pres: set 1+2+3=6
        maxs: max(last max3, pres)=6
        mins: 0 no change
    get -7:
        pres: set 1+2+3-7=-1
        maxs: max(last max6, pres)=last max6, pres become smaller, so no update
        mins: update to min(last min0, pres(-1)) = -1
    get -1:
        ...


<!--
就是累积求从0到当前i的总和sum，然后sum减去从0开始到当前i之前某一位j的最小sum值
，然后用sum减去这个最小sum值就是这一段总的最大值。
-->

# another solution

https://github.com/yuzhangcmu/LeetCode/blob/master/array/MaxSubArray_1220_2014.java


    assume: f[j] = the max sums from 0 to j
    and:    target = max{f[j]},1≤j≤n

    because: f[j] = max{S[j] + f[j−1], S[j]},1≤j≤n
    so:      f[j-1] (max sums from 0 to j-1) if it is nagative, then ignore it,
             (because it won't contribute to the result)


```python
class Solution:
    def maxSubArray(self, nums):
        sum, maxs=0, -sys.maxsize
        for num in nums:
            sum=num + (sum if sum > 0 else 0)
            maxs=max(maxs, sum)
        return maxs
```


