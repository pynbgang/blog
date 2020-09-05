---
layout: post
title: "[130] Surrounded Regions"
published: true
created:  2020 Sep 01 05:38:56 PM
tags: [python, leetcode, medium]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[130] Surrounded Regions](https://leetcode.com/problems/surrounded-regions/description/)

    || * algorithms
    || * Medium (25.15%)
    || * Likes:    1985
    || * Dislikes: 696
    || * Total Accepted:    252.3K
    || * Total Submissions: 891.2K
    || * Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
    || * Source Code:       130.surrounded-regions.py
    ||
    || Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
    ||
    || A region is captured by flipping all 'O's into 'X's in that surrounded region.
    ||
    || Example:
    ||
    ||
    || X X X X
    || X O O X
    || X X O X
    || X O X X
    ||
    ||
    || After running your function, the board should be:
    ||
    ||
    || X X X X
    || X X X X
    || X X X X
    || X O X X
    ||
    ||
    || Explanation:
    ||
    || Surrounded regions shouldn’t be on the border, which means that:
    any 'O' on the border of the board are not flipped to 'X'. 
    Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
    Two cells are connected if they are adjacent cells connected horizontally or vertically.


## owen

```python
class Solution(object):
    def solve(self, board):
        if not board:return []
        r,c=len(board),len(board[0])
        for i in range(r):
            if board[i][0]=="O":board[i][0]="Y"
            if board[i][-1]=="O":board[i][-1]="Y"
        for i in range(c):
            if board[0][i]=="O":board[0][i]="Y"
            if board[r-1][i]=="O":board[r-1][i]="Y"
        self.helper(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="Y":board[i][j]="O"
                elif board[i][j]=="O":board[i][j]="X"
        return board
    def helper(self,board):
        count=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    if board[i-1][j]=="Y" or board[i+1][j]=="Y" or board[i][j-1]=="Y" or board[i][j+1]=="Y":
                        board[i][j]="Y"
                        count+=1
        if count!=0:self.helper(board)
        return
```

## jj

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board, self.l, self.w = board, len(board), len(board[0]) if board else 0
        for i in range(self.l):
            self.helper(i, 0) or self.helper(i, self.w - 1)
        for j in range(self.w):
            self.helper(0, j) or self.helper(self.l - 1, j)
        for i in range(self.l):
            for j in range(self.w):
                self.board[i][j] = "X" if self.board[i][j] else "O"

    def helper(self, x, y):
        if x not in range(self.l) or y not in range(self.w):
            return
        if self.board[x][y] == "O":
            self.board[x][y] = ""
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                self.helper(x + a, y + b)
```

## lmv

https://leetcode.com/problems/surrounded-regions/discuss/41630

* Lang:    python3
* Author:  StefanPochmann
* Votes:   179

Phase 1: "Save" every O-region touching the border, changing its cells to 'S'.  
Phase 2: Change every 'S' on the board to 'O' and everything else to 'X'.

```python
class Solution:
    def solve(self, board):
        if not any(board): return
        m, n = len(board), len(board[0])
        save = [ij for k in range(m+n) for ij in ((0, k), (m-1, k), (k, 0), (k, n-1))]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
```

In case you don't like my last line, you could do this instead:

        for row in board:
            for i, c in enumerate(row):
                row[i] = 'XO'[c == 'S']

### tips

* `['XO'[c == 'S']`. because `'XO'[True] == 'XO'[1] == 'O'`
* `board[:] = `.  with `board = ` it won't pass. because the var "board" now
  points to a new array, and the original board array won't be updated.


## ping

```python
class Solution:     #ping
    def solve(self, grid: List[List[str]]) -> None:
        if not grid: return
        self.rows, self.cols = len(grid), len(grid[0])

        for i in range(self.rows):           #full grid searching for O
            for j in range(self.cols):
                if grid[i][j] == 'O':   #if found in border, set N(onmutable)
                    if i in [0, self.rows-1] or j in [0, self.cols-1]:
                        grid[i][j] = 'N'
                    else:               #if found in non-border, dfs
                        self.dfs(grid,i,j,[])

        grid[:] = ['XO'[c == 'N'] for c in  for row in grid]

    def dfs(self,grid,i,j,rec):
        flipback, grid[i][j] = 0, 'X' #for O at non-border, assume OK to flip to X.
        rec.append((i,j))   #just in case (connect to border O), save its index

        for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:   # check 4 neighbors
            if (m in [0, self.rows-1] or n in [0, self.cols-1]) and grid[m][n] in ['O', 'N']:
                grid[i][j], flipback = 'N', 1
                break

            if m>0 and m<self.rows-1 and n>0 and n<self.cols-1:
                if grid[m][n] == 'O':       #if found O in non-border, dfs
                    self.dfs(grid,m,n,rec)
                if grid[m][n] == 'N':
                    grid[i][j], flipback = 'N', 1
                    break

        if flipback:
            for i,j in rec:
                grid[i][j] = 'N'
```

