---
layout: post
title: "[73] Set Matrix Zeroes"
published: true
created:  2020 Aug 02 11:30:49 PM
tags: [python, leetcode, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[73]-set-matrix-zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/)

    || https://leetcode.com/problems/set-matrix-zeroes/description/
    || 
    || * algorithms
    || * Medium (41.83%)
    || * Likes:    2236
    || * Dislikes: 308
    || * Total Accepted:    326.1K
    || * Total Submissions: 756.8K
    || * Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
    || * Source Code:       73.set-matrix-zeroes.py
    || 
    || Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
    || 
    || Example 1:
    || 
    || Input: 
    || [
    ||   [1,1,1],
    ||   [1,0,1],
    ||   [1,1,1]
    || ]
    || Output: 
    || [
    ||   [1,0,1],
    ||   [0,0,0],
    ||   [1,0,1]
    || ]
    || 
    || Example 2:
    || 
    || Input: 
    || [
    ||   [0,1,2,0],
    ||   [3,4,5,2],
    ||   [1,3,1,5]
    || ]
    || Output: 
    || [
    ||   [0,0,0,0],
    ||   [0,4,5,0],
    ||   [0,3,1,0]
    || ]
    || 
    || 
    || Follow up:
    || 
    || 	A straight forward solution using O(mn) space is probably a bad idea.
    || 	A simple improvement uses O(m + n) space, but still not the best solution.
    || 	Could you devise a constant space solution?

# ping

# Owen 

```python
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:l.append([i,j])
        for x in l:
            for i in range(len(matrix)):
                matrix[i][x[1]]=0
            for i in range(len(matrix[0])):
                matrix[x[0]][i]=0
        return matrix
```


