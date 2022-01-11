---
layout: post
title: "[[53] Maximum Subarray]"
author: "owen"
published: true
created:  2020 Jan 13 23:34:22 PM
tags: [fb, google, python, interview, list, sys, easy, goodone]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[53] Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

    || * algorithms
    || * Easy (45.52%)
    || * Likes:    6326
    || * Dislikes: 272
    || * Total Accepted:    777.5K
    || * Total Submissions: 1.7M
    || * Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
    ||
    || Given an integer array nums, find the contiguous subarray (containing at
    least one number) which has the largest sum and return its sum.
    ||
    || Example:
    ||
    ||
    || Input: [-2,1,-3,4,-1,2,1,-5,4],
    || Output: 6
    || Explanation: [4,-1,2,1] has the largest sum = 6.
    ||
    ||
    || Follow up:
    ||
    || If you have figured out the O(n) solution, try coding another solution
    using the divide and conquer approach, which is more subtle.

* [maximum-subarray](https://www.lintcode.com/problem/maximum-subarray/description)
* https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

Find the contiguous subarray within an array, A of length N which has the
largest sum

# brute force:

```python
def maxSubArray(self, nums):
        return max(max(sum(nums[i:j+1]) for j in range(i, len(nums))) for i in range(len(nums)))
```

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
- 核心思想就是做单次循环的时候，当到达INDEX i的时候的最长子串的和等于sum(list[0-i])-min(子串合)
- O（n）时间

# solution (easest)

* https://github.com/yuzhangcmu/LeetCode/blob/master/array/MaxSubArray_1220_2014.java
* https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/maximum-subarray.html

so: just iterate and accumlate current sums. 
if a sum is negative, drop it (by set 0) when adding new num 

much easier to understand?

        assume: s[j] = the max sums from 0 to j
        and:    target = max{f[j]},1≤j≤n

        because: s[j] = max{nums[j] + s[j−1], nums[j]},1≤j≤n
        so:      for s[j-1] (max sums from 0 to j-1), if it is nagative, ignore it,
                (because it won't contribute to the result)

```python
class Solution:
    def maxSubArray(self, nums):
        sums, maxs=0, -sys.maxsize
        for num in nums:
            sums=num + (sums if sums > 0 else 0)
            maxs=max(maxs, sums)
        return maxs
```

# wangmazi (most subtle)

```python
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        #pres记录前i个数的和，
        #mins记录前i个数中总和和最小的一段（0-k）, 
        #maxs记录全局最大值，
        #sums 初始取0，或者任意值ok，因为计算中为实际数值
        #mins应该用nums[0]?
        mins, sums, maxs = 0,0, -sys.maxsize

        for num in nums:
            #1. 从0开始的当前累加值
            sums += num
            #2. 当前累加值, 减掉当前所知的，从0开始的最小累加值, 得到目前所知最大区间, 
            #随着循环不断维护这个最大区间
            maxs = max(maxs, sums - mins)
            #3. 维护一个当前所知的，从0开始累加的最小值, 为下步的2.所用
            mins = min(mins, sums)

        return maxs
```


## how it works?

即：理论上，在列表中要得出题目要求的连续区间最大累加值，可以：

* 暴力求解: 遍历所有可能的连续区间（on2)，计算其累加值，取最大
* smart算法：上面的方法。

基于两个基础的思路：

1. 任意连续的区间的和 sums(m,n)，必然可以拆解为以下公式：

        sums(m,n)=sums(0, n)-sums(0, m)
                 =sums(n) - sums(m)

   示意：

                    3           6
                    v           v
                    m           n
        1   2   3   -7  -1  5   2   -1
                    ----------       sums(m,n)
        ----------------------          sums(n): 0到n的简单累加
        ----------                      sums(m): 0到m的简单累加

   因此m，n任意区间求和转化为两个从0开始的遍历，但问题仍为on2


2. 基于1，对任意给定n=N: sums(m,N) 最大, 因为sums(N)已确定，必然sums(m)最小.

   如图：对于N=6, m 成为唯一变量, m多大的时候sums(m)最小？

                                6
                                v
        1   2   3   -7  -1  5   2   -1
        -------------------------       sums(N): 0到N的简单累加
        ------------------              mins(N): 以0开始，截止N之前，最小的sums(m)
                            -----       maxs(N): sums(N)-mins(N)

3. 基于2的结果. 2中得到的，是对任意一个n(比如6而言，找到的最大值maxs(n)。同样需
   要对所有的n做计算。最终答案，是对所有的n遍历，得到所有maxs(n)值中最大者:
   max(maxs(n))

至此，原问题（任意区间最大累计值）转化为求一个0到n之间从0开始的最小的sums(m). 表示为mins(n).
得到了mins(n), 即得到截止n的答案。
那么最终答案就是所有这些答案中的最大者。
因为不再强调“任意区间”， 而是代之以“一定从0开始”， 所以复杂度大大简化。

公式示意如下：

    for n in nums:
        pres_n += n                  #计算0开始的累加
        mins_n = min(mins_n, pres_n) #过程中维护一个mins(n)
        maxs_n = pres_n-mins_n       #根据mins(n)，计算maxs(n)
        target = max(target, maxs_n) #维护一个maxs(n)中的最大值


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

## manual execution

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

