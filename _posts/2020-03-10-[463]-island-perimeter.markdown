---
layout: post
title: "[463] Island Perimeter"
published: true
created:  2020 Mar 10 06:41:42 PM
tags: [python, leetcode, easy]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -


# [[463] Island Perimeter](https://leetcode.com/problems/island-perimeter/description/)

    || * algorithms
    || * Easy (62.64%)
    || * Likes:    1483
    || * Dislikes: 97
    || * Total Accepted:    168.4K
    || * Total Submissions: 267.8K
    || * Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
    || * Source Code:       463.island-perimeter.py
    || 
    || You are given a map in form of a two-dimensional integer grid where 1
    represents land and 0 represents water.
    || 
    || Grid cells are connected horizontally/vertically (not diagonally). The
    grid is completely surrounded by water, and there is exactly one island
    (i.e., one or more connected land cells).
    || 
    || The island doesn't have "lakes" (water inside that isn't connected to
    the water around the island). One cell is a square with side length 1. The
    grid is rectangular, width and height don't exceed 100. Determine the
    perimeter of the island.
    || 
    || Example:
    || 
    || 
    || Input:
    || [[0,1,0,0],
    || ⁠[1,1,1,0],
    || ⁠[0,1,0,0],
    || ⁠[1,1,0,0]]
    || 
    || Output: 16
    || 
    || Explanation: The perimeter is the 16 yellow stripes in the image below:
