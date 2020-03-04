---
layout: post
title: "[922] Sort Array By Parity II"
published: true
created:  2020 Mar 04 01:54:43 AM
tags: [python, leetcode, easy, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[922] Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/description/)

    || * algorithms
    || * Easy (67.89%)
    || * Likes:    484
    || * Dislikes: 42
    || * Total Accepted:    76.3K
    || * Total Submissions: 112.1K
    || * Testcase Example:  '[4,2,5,7]'
    || * Source Code:       922.sort-array-by-parity-ii.py
    || 
    || Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
    || 
    || Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
    || 
    || You may return any answer array that satisfies this condition.
    || 
    || Example 1:
    || Input: [4,2,5,7]
    || Output: [4,5,2,7]
    || Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
    || 
    || Note:
    || 
    || 
    || 	2 <= A.length <= 20000
    || 	A.length % 2 == 0
    || 	0 <= A[i] <= 1000
