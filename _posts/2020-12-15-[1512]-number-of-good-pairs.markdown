---
layout: post
title: "[1512] Number of Good Pairs"
published: true
created:  2020 Dec 15 18:01:56
tags: [python, easy, leetcode]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[1512] Number of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/description/)

    || * algorithms
    || * Easy (87.90%)
    || * Likes:    709
    || * Dislikes: 67
    || * Total Accepted:    102.1K
    || * Total Submissions: 116.2K
    || * Testcase Example:  '[1,2,3,1,1,3]'
    || * Source Code:       1512.number-of-good-pairs.py
    || 
    || Given an array of integers nums.
    || 
    || A pair (i,j) is called good if nums[i] == nums[j] and i < j.
    || 
    || Return the number of good pairs.
    || 
    || Example 1:
    || 
    || Input: nums = [1,2,3,1,1,3]
    || Output: 4
    || Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
    || 
    || Example 2:
    || 
    || Input: nums = [1,1,1,1]
    || Output: 6
    || Explanation: Each pair in the array are good.
    || 
    || 
    || Example 3:
    || 
    || 
    || Input: nums = [1,2,3]
    || Output: 0
    || 
    || 
    ||  
    || Constraints:
    || 
    || 
    || 	1 <= nums.length <= 100
    || 	1 <= nums[i] <= 100
