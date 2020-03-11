---
layout: post
title: "[463] Island Perimeter"
published: true
created:  2020 Mar 10 06:41:42 PM
tags: [python, leetcode, easy, zip, operator, map]
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

![image](https://assets.leetcode.com/uploads/2018/10/12/island.png)
<!--
![image](https://user-images.githubusercontent.com/2038044/76366270-eff1b880-62ff-11ea-960a-e81b1a2e959f.png)
-->

## ping: + and - method

```python
class Solution:     #ping
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return (sum(sum(l) for l in grid) * 4   #sum(all 1 x 4)
            -                 #minus sum(borders of 1) x 2
            sum([1 for l in grid for i in range(1, len(l)) if l[i] == l[i-1] == 1]) * 2
            -                 #minus sum(borders of 1 after matrix flip) x 2
            sum([1 for l in zip(*grid) for i in range(1, len(l)) if l[i] == l[i-1] == 1]) * 2
            )
        """
        ||   ✔ Accepted
        ||   ✔ 5833/5833 cases passed (500 ms)
        ||   ✔ Your runtime beats 90.89 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.9 MB)
        """
```
idea:

* sum all lines for each cube (x4 each)
* deduct adjacent lines for each adjacent cubes (x2 each adjacency)
    * do it horiontally
    * flip matrix, and repeat, to do it vertically

## owen (lmv): + only method and his own

```python
class Solution(object):
    def islandPerimeter(self, grid):
        numsq=0
        for i in grid:
            numsq+=i.count(1)
        count_adj=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:count_adj+=self.helper(grid,i,j)
        return numsq*4-count_adj

    def helper(self,grid,i,j):
        count=0
        if i-1>=0 and grid[i-1][j]==1:count+=1
        if i+1<=len(grid)-1 and grid[i+1][j]==1:count+=1
        if j-1>=0 and grid[i][j-1]==1:count+=1
        if j+1<=len(grid[0])-1 and grid[i][j+1]==1:count+=1
        return count
```

## LMV oneline

```python
def islandPerimeter(self, grid):
    return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))
```

idea:

* scan rows, count all flips (0->1, 1->0) horizontally, as horizontal boundaries
* flip matrix, do same, to count all flips vertically, as vertical boundaries
* sum all boundaries

break down:

```python
def islandPerimeter(self, grid):
    return (
        sum(
            sum(
                map(operator.ne, [0] + row, row + [0])
            )
            for row in grid + map(list, zip(*grid))
        )
    )
```

count all "flip"(change) in list:

    `sum( map(operator.ne, [0] + row, row + [0]) )`:

illustration:

    [1, 1, 1, 1] =>

    map(operator.ne, [0] + row, row + [0]) =>

    [0, 1, 1, 1, 1]
     A  A  A  A  A
     |  |  |  |  |
     1  0  0  0  1      => 2 flips (L:water->island, R:island->water)
     |  |  |  |  |
     v  v  v  v  v
    [1, 1, 1, 1, 0]

same as to compare each adjacent item:

    [0, 1, 1, 1, 1, 0]
    ---
    1 ---
        0 ---
            0 ----      => 2 flips
            0 ----
                1

## xiaofo (last year)

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += 4 - 1 * (i > 0 and grid[i - 1][j]) - 1 * (i < len(grid) - 1 and grid[i + 1][j]) - 1 * (j > 0 and grid[i][j - 1]) - 1 * (j < len(grid[0]) - 1 and grid[i][j + 1])
        return res
```

## lmv

```python
class Solution:     #lmv
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                    if grid[row][column]:
                        res+=4
                        if row and grid[row-1][column]:
                            res-=2
                        if column and grid[row][column-1]:
                            res-=2
        return res
        """
        ||   ✔ Accepted
        ||   ✔ 5833/5833 cases passed (468 ms)
        ||   ✔ Your runtime beats 99.75 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
        """
```

## tips

* list expansion: `*` + `zip`: zip(*list)
* `operator.ne` .le .eq .ge .gt ...
* `map` func can have multiple parameters! when it does, requiring same amount
  of iterables (list)


