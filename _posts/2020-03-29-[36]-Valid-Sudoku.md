---
layout: post
title: "[36] Valid Sudoku"
published: true
created:  2020 Mar 29 03:32:50 PM
tags: [python, leetcode, list, medium, zip, comment]
categories: [tech]

---

TABLE OF CONTENT

* auto-gen TOC:
{:toc}

- - -

# [[36] Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

    || [36] Valid Sudoku  
    || 
    || https://leetcode.com/problems/valid-sudoku/description/
    || 
    || * algorithms
    || * Medium (46.40%)
    || * Likes:    1357
    || * Dislikes: 424
    || * Total Accepted:    326.7K
    || * Total Submissions: 692.4K
    || * Testcase Example:  
        '[
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]'

    || * Source Code:       36.valid-sudoku.py
    || 
    || Determine if a 9x9 Sudoku board is valid. Only the filled cells need to
    be validated according to the following rules:
    || 
    || 
    || 	Each row must contain the digits 1-9 without repetition.
    || 	Each column must contain the digits 1-9 without repetition.
    || 	Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    || 
    || A partially filled sudoku which is valid.

![image](https://user-images.githubusercontent.com/2038044/78719914-b60dd500-78f2-11ea-899d-1353464fa501.png)

    || The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
    || 
    || Example 1:
    || 
    || 
    || Input:
    || [
    || ⁠ ["5","3",".",".","7",".",".",".","."],
    || ⁠ ["6",".",".","1","9","5",".",".","."],
    || ⁠ [".","9","8",".",".",".",".","6","."],
    || ⁠ ["8",".",".",".","6",".",".",".","3"],
    || ⁠ ["4",".",".","8",".","3",".",".","1"],
    || ⁠ ["7",".",".",".","2",".",".",".","6"],
    || ⁠ [".","6",".",".",".",".","2","8","."],
    || ⁠ [".",".",".","4","1","9",".",".","5"],
    || ⁠ [".",".",".",".","8",".",".","7","9"]
    || ]
    || Output: true
    || 
    || 
    || Example 2:
    || 
    || 
    || Input:
    || [
    ||   ["8","3",".",".","7",".",".",".","."],
    ||   ["6",".",".","1","9","5",".",".","."],
    ||   [".","9","8",".",".",".",".","6","."],
    ||   ["8",".",".",".","6",".",".",".","3"],
    ||   ["4",".",".","8",".","3",".",".","1"],
    ||   ["7",".",".",".","2",".",".",".","6"],
    ||   [".","6",".",".",".",".","2","8","."],
    ||   [".",".",".","4","1","9",".",".","5"],
    ||   [".",".",".",".","8",".",".","7","9"]
    || ]
    || Output: false
    || Explanation: Same as Example 1, except with the 5 in the top left corner being 
    || ⁠   modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
    || 
    || 
    || Note:
    || 
    || 
    || 	A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    || 	Only the filled cells need to be validated according to the mentioned rules.
    || 	The given board contain only digits 1-9 and the character '.'.
    || 	The given board size is always 9x9.
    || 


## Brute Force Owen

```python
class Solution(object):
    def isValidSudoku(self, board):
        row,col=9,9
        for i in board:
            temp="".join(i).replace(".","")
            if len(temp)!=len(set(temp)):return False
        for j in range(len(board[0])):
            temp=""
            for i in range(len(board)):
                if board[i][j]!=".":temp+=board[i][j]
            if  len(temp)!=len(set(temp)):return False
        for z in range(3):
            temp,temp1,temp2="","",""
            for i in range(z*3,z*3+3):
                for j in range(0,3):
                    if board[i][j]!=".":temp+=board[i][j]
                    if board[i][j+3]!=".":temp1+=board[i][j+3]
                    if board[i][j+6]!=".":temp2+=board[i][j+6]
            if  len(temp)!=len(set(temp)):return False
            if  len(temp1)!=len(set(temp1)):return False
            if  len(temp2)!=len(set(temp2)):return False
        return True
```

## brute force: ping

```python
class Solution:     #ping: brute force, compacted
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        superb = (                          #compose a superboard
            board +                         #from original board, plus
            list(map(list, zip(*board))) +  #rotated board, and subbox rows
            [[board[x][y] for x in range(i, i+3) for y in range(j, j+3)] for i in (0,3,6) for j in (0,3,6)]
        )
        for l in superb:
            if "." not in l:                #if no '.', set len must be 9
                if len(set(l)) != 9:
                    return False
            else:                           #with '.', # of digits must be..
                if len(set(l)) != sorted(l, reverse=True).index('.') + 1:
                    return False
        return True
```

