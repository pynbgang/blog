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

# owen

## code

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

## 思路

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

* https://leetcode.com/problems/maximum-subarray/
* https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

## how it works?

即：理论上，在列表中要得出题目要求的连续区间最大累加值，可以：

* 暴力求解: 遍历所有可能的连续区间（on2)，计算其累加值，取最大
* smart算法：上面的方法。

基于两个基础的思路：

1. 任意连续的区间的和 sums(m,n)，必然可以拆解为以下公式：

        sums(m,n)=pres(n)-pres(m)

   示意：

        1   2   3   -7  -1  5   2   -1
                    ----------       sums(m,n)
        -------------------------       pres: 0到n的简单累加
        --------------                  pres: 0到m的简单累加

   因此m，n任意区间求和转化为两个从0开始的遍历，但问题认为on2


2. 基于1，对任意n，sums(m,n) 最大必然 ===> pres(m)最小. 

   示意：

        1   2   3   -7  -1  5   2   -1
        -------------------------       pres(n): 0到n的简单累加
        ------------------              mins(n): 以0开始，截止n之前，最小的pres: pres(m)
                            -----       maxs(n): pres(n)-mins(n)
                                        最终答案: 所有maxs(n)值中最大者: max(maxs)

至此，原问题（任意区间最大累计值）转化为求一个0到n之间从0开始的最小的pres(m). 表示为mins(n). 
得到了mins(n), 即得到截止n的答案。
那么最终答案就是所有这些答案中的最大者。
因为不再强调“任意区间”， 而是代之以“一定从0开始”， 所以复杂度大大简化。

公式示意如下：

    for n in nums:
        pres_n += n                  #计算0开始的累加
        mins_n = min(mins_n, pres_n) #过程中维护一个mins(n)
        maxs_n = pres_n-mins_n       #计算maxs(n)
        target = max(target, maxs_n) #maxs(n)中的最大值


## tricks

* init vars
 
* maxs(n) first

it does not work for all negative nums. [-1,-2,-3,-100,-1,-50]

    for any n:
        mins(n) = pres(n)          ==> 
        maxs(n) = pres(n)-mins(n) == 0 ==> wrong

corrected:

    for n in nums:
        pres_n += n                  #计算0开始的累加
        maxs_n = pres_n-mins_n       #计算maxs(n)
        mins_n = min(mins_n, pres_n) #过程中维护一个mins(n)
        target = max(target, maxs_n) #maxs(n)中的最大值

## 手run如下

    init: mins = 0 (so only update when seeing nagative sum) 
    get 1:
        pres: add 1
        maxs: set 1 (because x < -sys.maxsize)
        mins: 0 no change since 1>0
    get 2:
        pres: add 2=3
        maxs: max(last max1, pres - last min0=pres) = 3
        mins: 0 no change since 3>0
    get 3:
        pres: add 3=6
        maxs: max(last max3, pres)=6
        mins: 0 no change since 6>0
    get -7:
        pres: add -7=-1
        maxs: max(last max6, pres)=last max6, pres become smaller, so no update
        mins: update to min(last min0, pres(-1)) = -1
    get -1:
        ...


<!--
就是累积求从0到当前i的总和sum，然后sum减去从0开始到当前i之前某一位j的最小sum值
，然后用sum减去这个最小sum值就是这一段总的最大值。
-->

## another solution (best)

https://github.com/yuzhangcmu/LeetCode/blob/master/array/MaxSubArray_1220_2014.java
https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/maximum-subarray.html


    assume: s[j] = the max sums from 0 to j
    and:    target = max{f[j]},1≤j≤n

    because: s[j] = max{nums[j] + s[j−1], nums[j]},1≤j≤n
    so:      for s[j-1] (max sums from 0 to j-1), if it is nagative, ignore it,
             (because it won't contribute to the result)

so: just iterate and accumlate sums. if previous sum becomes negative, drop it (by set 0)

much easier to understand?

```python
class Solution:
    def maxSubArray(self, nums):
        sum, maxs=0, -sys.maxsize
        for num in nums:
            sum=num + (sum if sum > 0 else 0)
            maxs=max(maxs, sum)
        return maxs
```

