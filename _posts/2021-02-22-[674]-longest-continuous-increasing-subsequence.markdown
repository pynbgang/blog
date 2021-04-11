---
layout: post
title: "[674] Longest Continuous Increasing Subsequence"
published: true
created:  2021 Feb 22 12:20:40
tags: [python, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[674] Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/)

    || * algorithms
    || * Easy (45.99%)
    || * Likes:    1076
    || * Dislikes: 136
    || * Total Accepted:    138.8K
    || * Total Submissions: 301.5K
    || * Testcase Example:  '[1,3,5,4,7]'
    || * Source Code:       674.longest-continuous-increasing-subsequence.py
    || 
    || Given an unsorted array of integers nums, return the length of the
    longest continuous increasing subsequence (i.e. subarray). The subsequence
    must be strictly increasing.
    || 
    || A continuous increasing subsequence is defined by two indices l and r (l
    < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and
    for each l <= i < r, nums[i] < nums[i + 1].
    ||  
    || Example 1:
    || 
    || Input: nums = [1,3,5,4,7]
    || Output: 3
    || Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
    || Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
    || 4.
    || 
    || Example 2:
    || 
    || Input: nums = [2,2,2,2,2]
    || Output: 1
    || Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
    || increasing.
    ||  
    || Constraints:
    || 
    || 	0 <= nums.length <= 10^4
    || 	-10^9 <= nums[i] <= 10^9

# issue


