---
layout: post
title: "[73] Set Matrix Zeroes"
published: true
created:  2020 Aug 02 11:30:49 PM
tags: [python, leetcode, medium, matrix]
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

## ping

```python
class Solution:     #ping
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols, row0, col0 = len(matrix), len(matrix[0]), set(), set()
        for row in range(rows):             #scan whole matrix and look for
            for col in range(cols):         #the 0 elements, record it's
                if matrix[row][col] == 0:   #row/col number
                    col0.add(col)
                    row0.add(row)
        for i in row0:                      #fill zero for each row
            matrix[i] = [0] * cols
        for i in col0:                      #fill zero for each col
            for row in range(rows):
                matrix[row][i] = 0
```

## Owen 

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

## lmv

```python
class Solution:     #lmv
    def setZeroes(self, matrix):
        # First row has zero?
        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use first row/column as marker, scan the matrix
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        # Set the zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Set the zeros for the first row
        if firstRowHasZero:
            matrix[0] = [0] * n
```

## tips

* use first row to record if the corresponding column of each its number has 0


       +--------------+
       | 0| x| x| x|0 |  #<--- serving each column
       +--------------+
       | x| x| x| x|0 |
       | x| x| x| x|x |
       | 0| x| x| x|0 |


* use first column to record if the corresponding row of each its number has 0

       +--------------+
       | 0| x| 0| x|0 |
       +--------------+
       | 0| x| x| x|0 |
       | x| x| x| x|x |
       | 0| x| x| x|0 |

        ^
        |
        serving each row, but except 1st row

* first number in first row belongs to first row's role (recording existence of
    0 in it's column, not recording existence of 0 in it's row)


