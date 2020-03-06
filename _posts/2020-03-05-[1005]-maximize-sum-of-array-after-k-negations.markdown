---
layout: post
title: "[1005] Maximize Sum Of Array After K Negations"
published: true
created:  2020 Mar 05 10:17:26 PM
tags: [python, leetcode, easy, string]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[1005] Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/)

    || * algorithms
    || * Easy (50.63%)
    || * Likes:    241
    || * Dislikes: 29
    || * Total Accepted:    21.3K
    || * Total Submissions: 42K
    || * Testcase Example:  '[4,2,3]\n1'
    || * Source Code:       1005.maximize-sum-of-array-after-k-negations.py
    || 
    || Given an array A of integers, we must modify the array in the following
    way: we choose an i and replace A[i] with -A[i], and we repeat this process
    K times in total.  (We may choose the same index i multiple times.)
    || 
    || Return the largest possible sum of the array after modifying it in this way.
    || 
    || Example 1:
    || Input: A = [4,2,3], K = 1
    || Output: 5
    || Explanation: Choose indices (1,) and A becomes [4,-2,3].
    || 
    || Example 2:
    || Input: A = [3,-1,0,2], K = 3
    || Output: 6
    || Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
    || 
    || Example 3:
    || Input: A = [2,-3,-1,5,-4], K = 2
    || Output: 13
    || Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
    || 
    || Note:
    || 
    || 	1 <= A.length <= 10000
    || 	1 <= K <= 10000
    || 	-100 <= A[i] <= 100
    || 
