---
layout: post
title: "maximum-average-subarray-i"
published: true
created:  2020 Mar 01 11:24:04 PM
tags: [python, easy, list, leetcode, media, wumochou]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[643] Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/description/)

    || * algorithms
    || * Easy (40.74%)
    || * Likes:    599
    || * Dislikes: 99
    || * Total Accepted:    67.8K
    || * Total Submissions: 165.9K
    || * Testcase Example:  '[1,12,-5,-6,50,3]\n4'
    || * Source Code:       643.maximum-average-subarray-i.py
    ||
    || Given an array consisting of n integers, find the contiguous subarray of
    given length k that has the maximum average value. And you need to output
    the maximum average value.
    ||
    || Example 1:
    ||
    ||
    || Input: [1,12,-5,-6,50,3], k = 4
    || Output: 12.75
    || Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
    ||
    ||
    ||  
    ||
    || Note:
    ||
    ||
    || 	1 <= k <= n <= 30,000.
    || 	Elements of the given array will be in the range [-10,000, 10,000].


# ping

```python
class Solution:  #ping: wrong, can't sort
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return sum(sorted(nums)[-1:-k-1:-1])/k

class Solution:  #ping: time limit exceeded
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))/k

class Solution:  #ping: passed
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max1 = sum1 = sum(nums[0:k])    #get first k sum as a base
        for i in range(len(nums)-k):
            sum1+=nums[i+k]-nums[i]     #use base+delta as new sum
            max1=max(max1, sum1)        #keep max
        return max1/k
```

this is wrong, sum1 can't be updated in oneliner

    #res=max(sum1, max([sum1+nums[i+k]-nums[i] for i in range(len(nums)-k)] or [-sys.maxsize]))/k


# lmv: 

accumulate delta only, use base at last
also avoid max
smarter, but seems not faster ...

```python
class Solution:     #lmv
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        M = d = 0
        for i in range(len(nums)-k):
            d += nums[i+k] - nums[i]
            if d > M: M = d
        return (sum(nums[:k])+M)/k
```

<iframe frameborder="0" src="https://v.qq.com/txp/iframe/player.html?vid=v0773d62htm" allowFullScreen="true"></iframe>
