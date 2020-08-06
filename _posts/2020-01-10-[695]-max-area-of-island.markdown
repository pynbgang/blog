---
layout: post
title: "[695]-max-area-of-island"
published: true
created:  2020 Jan 10 11:38:11 AM
tags: [wangmazi, xiaofo, map, operator, dfs, dict, complex, lintcode, leetcode, medium, global, recursion, matrix]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[695] Max Area of Island](https://leetcode.com/problems/max-area-of-island/description/)

    || * algorithms
    || * Medium (60.26%)
    || * Likes:    1605
    || * Dislikes: 72
    || * Total Accepted:    132.7K
    || * Total Submissions: 217.4K
    || * Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
    || * Source Code:       695.max-area-of-island.py
    ||
    || Given a non-empty 2D array grid of 0's and 1's, an island is a group of
    1's (representing land) connected 4-directionally (horizontal or vertical.)
    You may assume all four edges of the grid are surrounded by water.
    ||
    || Find the maximum area of an island in the given 2D array. (If there is
    no island, the maximum area is 0.)
    ||
    || Example 1:
    ||
    ||
    || [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    ||  [0,0,0,0,0,0,0,1,1,1,0,0,0],
    ||  [0,1,1,0,1,0,0,0,0,0,0,0,0],
    ||  [0,1,0,0,1,1,0,0,1,0,1,0,0],
    ||  [0,1,0,0,1,1,0,0,1,1,1,0,0],
    ||  [0,0,0,0,0,0,0,0,0,0,1,0,0],
    ||  [0,0,0,0,0,0,0,1,1,1,0,0,0],
    ||  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    ||
    || Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
    ||
    || Example 2:
    ||
    ||
    || [[0,0,0,0,0,0,0,0]]
    || Given the above grid, return 0.
    ||
    || Note: The length of each dimension in the given grid does not exceed 50.

* https://leetcode.com/problems/max-area-of-island/
* https://www.lintcode.com/problem/max-area-of-island/description

## wangmazi (最清晰)

```python
class Solution(object):

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ## 空输入就啥别说了
        if not grid: return

        ## 整个排列坐标系
        rows, cols = len(grid), len(grid[0])

        ## 全坐标暴力搜索1，找到后对它求个值（它所在连续1区间的数量）
        ## 具体求法另议
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    max_ones = max(max_ones,self.dfs(grid,i,j,1))

        return max_ones

    def dfs(self,grid,i,j,count):
        ## 针对某一个1，求”岛面积“，即所在周边所有连续1的数量。dfs递归思路

        ## 已知为1，置零
        grid[i][j] = 0

        ## 一一查看当前点的“周边”四个点
        for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            ## 如果这四个边界点在有效范围内并且也为1， 则
            if m>=0 and m<len(grid) and n>=0 and n<len(grid[0]) and grid[m][n]:
                ## 对这边界为1的点再次dfs递归，并扩展总数量
                count = 1 + self.dfs(grid,m,n,count)
        ## 最后返回总的连续1的数量
        return count
```

## jj2 (最短最精妙)

### the zb code

```python
    def maxAreaOfIsland(self, grid):
        # 生成 {坐标:值} 字典
        grid = {i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}

        # 给定坐标，求连续1的面积
        def area(z): return grid.pop(z, 0) and 1 + sum(area(z + 1j**k) for k in range(4))

        # 在包含所有坐标对应面积的列表(iterator)中，取最大值
        return max(map(area, set(grid)))
```

### about dict comprehension breakdown:

```python
grid = [[11, 12], [21, 22]]
d={i + j*1j: val for i, row in enumerate(grid) for j, val in enumerate(row)}
d
{0j: 11, 1j: 12, (1+0j): 21, (1+1j): 22}
```

equals to:

```python
grid = [[11, 12], [21, 22]]
d={}
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        d[i+j*1j]=val
d
```

### about python complex

basic form:

    [ins] In [8]: j
    Out[8]: 1

    [ins] In [7]: 1+j
    Out[7]: 2

    [ins] In [9]: 1+1j
    Out[9]: (1+1j)

    [ins] In [54]: 1+1j.
                         conjugate()
                         imag()
                         real()
    [ins] In [11]: 1+1j.conjugate()
    Out[11]: (1-1j)

`1j ** n`

    [ins] In [54]: 1j ** 0
    Out[54]: (1+0j)     #<---任意数0次方为1

    [ins] In [55]: 1j ** 1
    Out[55]: 1j         #<---任意数1次方为自身

    [ins] In [56]: 1j ** 2
    Out[56]: (-1+0j)    #<---虚数平方为-1

    [ins] In [57]: 1j ** 3
    Out[57]: (-0-1j)


it happens to be the points in coordinate sytem:

            |
            - 1j**1
            |
    ----|---+---|----------
     1j**2  |   1j**0
            - 1j**3
            |

### about python 'a and b' trick

    [ins] In [17]: 0 and print(123)
    Out[17]: 0
    [ins] In [18]: 1 and print(123)
    123

same as:

    `a if not a else b`

evaluate a first, (only) if True, evaluate b

similiarly, 'a or b':

    [ins] In [36]: 0 or print(123)
    123

    [ins] In [37]: 1 or print(123)
    Out[37]: 1


### about python precedence

    def area(z): return grid.pop(z, 0) and 1 + sum(area(z + 1j**k) for k in range(4))
                        -----a--------     b   ----------------c--------------------

how to evaluate `a and b + c` ?

<!--
        四则位移与异或
        外加比较非与或
-->

operator precedence口诀

        乘除加比特
        比较非与或

        (*/+-bit comp not and or)

so:

    `a and b + c` == `a and (b+c)` ==> `a and b` issue =>

    evaluate a, that is `grid.pop(z, 0)`: 给定坐标处是1否？only when True, =>

    evaluate b(1)+c => evaluate c (sum for k in range) => this is dfs

### about map

see other blogs

## others

### owen

#### original

```python
count=0
class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """

    def maxAreaOfIsland(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        ret, temp = 0, 0
        global count
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ret += 1
                    count=0
                    self.removeIsland(grid, i, j)
                    temp=max(temp,count)
                    print temp

        return temp

    def removeIsland(self, grid, i, j):
        global count
        count+=1
        grid[i][j] = 0
        if i > 0 and grid[i - 1][j] == 1:
            self.removeIsland(grid, i - 1, j)
        if i < len(grid) - 1 and grid[i + 1][j] == 1:
            self.removeIsland(grid, i + 1, j)
        if j > 0 and grid[i][j - 1] == 1:
            self.removeIsland(grid, i, j - 1)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
            self.removeIsland(grid, i, j + 1)
```

key:

* 递归时候简单变量的更新比较tricky。
  * 子过程中更新的简单变量，不会自动更新“回”父过程中
  * 使用返回值可以累积
* 此处使用了global。

#### after removal global

```python
class Solution:
    """
    @param grid: a 2D array
    @return: the maximum area of an island in the given 2D array
    """

    def maxAreaOfIsland(self, grid):
        # write your code here
        if not grid or not grid[0]:        #special conditions: grid == [], [[]]
            return 0
        res = 0
        for i in range(len(grid)):         #iterate every row..
            for j in range(len(grid[0])):  #..and column for any 1
                if grid[i][j] == 1:        #once found, check all its neighbors
                    count = self.removeIsland(grid, i, j, 0)  #and return count
                    res = max(res,count)   #keep tracking the max of all counts
        return res

    def removeIsland(self, grid, i, j, count): #check a node's all neighbors
        count+=1                          #and count 1s
        grid[i][j] = 0                    #flip the checked node to avoid dups
        if i > 0 and grid[i - 1][j] == 1:                       #moving up
            count=self.removeIsland(grid, i - 1, j, count)
        if i < len(grid) - 1 and grid[i + 1][j] == 1:           #moving down
            count=self.removeIsland(grid, i + 1, j, count)
        if j > 0 and grid[i][j - 1] == 1:                       #moving left
            count=self.removeIsland(grid, i, j - 1, count)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:        #moving right
            count=self.removeIsland(grid, i, j + 1, count)
        return count
```

### jj

#### solution (after peeping most voted solution)

```python
class Solution:
    from typing import List
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(g, r, c):
            if 0 <= r < len(g) and 0 <= c < len(g[0]) and g[r][c]:
                g[r][c] = 0
                return 1 + dfs(g, r + 1, c) + dfs(g, r - 1, c) + \
                           dfs(g, r, c + 1) + dfs(g, r, c - 1)
            return 0
        rtn = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rtn = max(rtn, dfs(grid, i, j))
        return rtn
```

#### takeaway

- use dfs to explore an 'island'
- set each element to 0 while exploring to avoid repeated traversal, after dfs,
  the island should have disappeared from the map


