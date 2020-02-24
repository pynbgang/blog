---
layout: post
title: "minimum-moves-to-equal-array-elements"
published: true
created:  2020 Feb 24 11:44:22 AM
tags: [lintcode, python, easy, list]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[453] Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/)

|| * algorithms
|| * Easy (49.77%)
|| * Likes:    472
|| * Dislikes: 694
|| * Total Accepted:    67.1K
|| * Total Submissions: 134.8K
|| * Testcase Example:  '[1,2,3]'
|| * Source Code:       453.minimum-moves-to-equal-array-elements.py
|| 
|| Given a non-empty integer array of size n, find the minimum number of moves
|| required to make all array elements equal, where a move is incrementing n - 1
|| elements by 1.
|| 
|| Example:
|| 
|| Input:
|| [1,2,3]
|| 
|| Output:
|| 3
|| 
|| Explanation:
|| Only three moves are needed (remember each move increments two elements):
|| 
|| [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
